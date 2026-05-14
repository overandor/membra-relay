"""MEMBRA Relay — local handoff, storage-to-delivery, and proof-route control plane.

Hugging Face/FastAPI runtime for creating relay jobs, pricing route modes,
tracking proof events, exporting job registers, and receiving Stripe webhooks.
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import os
import sqlite3
import uuid
from pathlib import Path
from typing import Any

import gradio as gr
import stripe
import uvicorn
from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

APP_NAME = "MEMBRA Relay"
DB_PATH = Path(os.getenv("DB_PATH", "/tmp/membra_relay.sqlite3"))
APP_BASE_URL = os.getenv("APP_BASE_URL", "http://localhost:7860").rstrip("/")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "")
STRIPE_PRICE_ID = os.getenv("STRIPE_PRICE_ID", "")
stripe.api_key = STRIPE_SECRET_KEY or None
api = FastAPI(title=APP_NAME)

class RelayJobIn(BaseModel):
    requester_email: str
    item_label: str
    pickup_node: str
    dropoff_node: str
    mode: str = "local_delivery"
    distance_miles: float = Field(default=1.0, ge=0)
    estimated_minutes: int = Field(default=20, ge=0)
    proof_requirements: str = "pickup proof, dropoff proof, timestamp, optional geo proof"
    notes: str = ""

class CheckoutIn(BaseModel):
    email: str
    relay_id: str | None = None


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH, timeout=30, isolation_level=None)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with db() as conn:
        conn.executescript("""
        CREATE TABLE IF NOT EXISTS relay_jobs(
          relay_id TEXT PRIMARY KEY,
          requester_email TEXT,
          item_label TEXT,
          pickup_node TEXT,
          dropoff_node TEXT,
          mode TEXT,
          distance_miles REAL,
          estimated_minutes INTEGER,
          estimated_price_usd REAL,
          agent_payout_usd REAL,
          proof_requirements TEXT,
          notes TEXT,
          status TEXT,
          stripe_session_id TEXT,
          created_at TEXT
        );
        CREATE TABLE IF NOT EXISTS proof_events(event_id TEXT PRIMARY KEY, relay_id TEXT, event_type TEXT, payload_json TEXT, created_at TEXT);
        """)

init_db()


def price_route(distance: float, mode: str) -> tuple[float, float]:
    if mode == "pickup_only":
        price = 0.0
    elif mode == "meet_halfway":
        price = min(5.0, max(2.0, distance * 2.5))
    elif distance <= 0.5:
        price = 6.0
    elif distance <= 2:
        price = 9.0 + distance * 1.5
    elif distance <= 5:
        price = 14.0 + distance * 2.0
    else:
        price = 25.0 + distance * 2.5
    payout = round(price * 0.68, 2)
    return round(price, 2), payout


def build_job(data: RelayJobIn) -> dict[str, Any]:
    relay_id = "relay_" + uuid.uuid4().hex[:12]
    price, payout = price_route(data.distance_miles, data.mode)
    job = {
        "relay_id": relay_id,
        "requester_email": data.requester_email,
        "item_label": data.item_label,
        "pickup_node": data.pickup_node,
        "dropoff_node": data.dropoff_node,
        "mode": data.mode,
        "distance_miles": data.distance_miles,
        "estimated_minutes": data.estimated_minutes,
        "estimated_price_usd": price,
        "agent_payout_usd": payout,
        "proof_requirements": data.proof_requirements,
        "status": "draft_pending_acceptance_and_funding",
        "notes": data.notes,
        "created_at": now(),
    }
    with db() as conn:
        conn.execute("INSERT INTO relay_jobs VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (relay_id, data.requester_email, data.item_label, data.pickup_node, data.dropoff_node, data.mode, data.distance_miles, data.estimated_minutes, price, payout, data.proof_requirements, data.notes, job["status"], None, job["created_at"]))
    return job


def job_rows() -> list[dict[str, Any]]:
    with db() as conn:
        rows = conn.execute("SELECT relay_id,item_label,pickup_node,dropoff_node,mode,distance_miles,estimated_price_usd,agent_payout_usd,status,created_at FROM relay_jobs ORDER BY created_at DESC LIMIT 200").fetchall()
    return [dict(r) for r in rows]


def export_jobs() -> str:
    rows = job_rows()
    path = "/tmp/membra_relay_jobs.csv"
    if rows:
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader(); writer.writerows(rows)
    else:
        Path(path).write_text("relay_id,item_label,status\n", encoding="utf-8")
    return path


def ui_create(email, item, pickup, dropoff, mode, distance, minutes, proof, notes):
    try:
        job = build_job(RelayJobIn(requester_email=email, item_label=item, pickup_node=pickup, dropoff_node=dropoff, mode=mode, distance_miles=float(distance or 0), estimated_minutes=int(minutes or 0), proof_requirements=proof, notes=notes))
        return json.dumps(job, indent=2), job_rows(), export_jobs()
    except Exception as exc:
        return f"Error: {exc}", job_rows(), None


def ui_checkout(email, relay_id):
    if not STRIPE_SECRET_KEY or not STRIPE_PRICE_ID:
        return "Stripe is not configured."
    session = stripe.checkout.Session.create(mode="payment", customer_email=email, line_items=[{"price": STRIPE_PRICE_ID, "quantity": 1}], success_url=f"{APP_BASE_URL}/?checkout=success", cancel_url=f"{APP_BASE_URL}/?checkout=cancelled", metadata={"relay_id": relay_id or ""})
    if relay_id:
        with db() as conn:
            conn.execute("UPDATE relay_jobs SET stripe_session_id=?, status=? WHERE relay_id=?", (session.id, "funding_checkout_created", relay_id))
    return session.url

@api.get("/api/health")
def health():
    return {"ok": True, "app": APP_NAME, "stripe_configured": bool(STRIPE_SECRET_KEY and STRIPE_WEBHOOK_SECRET and STRIPE_PRICE_ID)}

@api.get("/api/jobs")
def list_jobs():
    return {"jobs": job_rows()}

@api.post("/api/jobs")
def create_job(data: RelayJobIn):
    return build_job(data)

@api.post("/api/stripe/create-checkout-session")
def checkout(data: CheckoutIn):
    return {"url": ui_checkout(data.email, data.relay_id or "")}

@api.post("/api/stripe/webhook")
async def stripe_webhook(request: Request, stripe_signature: str | None = Header(default=None)):
    if not STRIPE_WEBHOOK_SECRET:
        raise HTTPException(500, "STRIPE_WEBHOOK_SECRET is not configured")
    body = await request.body()
    try:
        event = stripe.Webhook.construct_event(body, stripe_signature, STRIPE_WEBHOOK_SECRET)
    except Exception as exc:
        raise HTTPException(400, str(exc))
    obj = event["data"]["object"]
    relay_id = obj.get("metadata", {}).get("relay_id")
    if relay_id and event["type"] == "checkout.session.completed":
        with db() as conn:
            conn.execute("UPDATE relay_jobs SET status=? WHERE relay_id=?", ("funded_pending_agent_acceptance", relay_id))
            conn.execute("INSERT INTO proof_events VALUES(?,?,?,?,?)", ("evt_" + uuid.uuid4().hex[:12], relay_id, event["type"], json.dumps(obj, default=str), now()))
    return JSONResponse({"received": True})

with gr.Blocks(title=APP_NAME) as demo:
    gr.Markdown("# MEMBRA Relay\nRoute/job control plane for local handoff, return runs, hub transfers, and proof-based fulfillment.")
    with gr.Row():
        email = gr.Textbox(label="Requester email")
        item = gr.Textbox(label="Item label")
    with gr.Row():
        pickup = gr.Textbox(label="Pickup node")
        dropoff = gr.Textbox(label="Dropoff node")
    with gr.Row():
        mode = gr.Dropdown(["pickup_only", "meet_halfway", "local_delivery", "return_run", "hub_transfer", "errand_relay", "batch_route"], value="local_delivery", label="Mode")
        distance = gr.Number(label="Distance miles", value=1.2)
        minutes = gr.Number(label="Estimated minutes", value=18)
    proof = gr.Textbox(label="Proof requirements", value="pickup proof, dropoff proof, timestamp, optional geo proof")
    notes = gr.Textbox(label="Notes", lines=3)
    create = gr.Button("Create relay job", variant="primary")
    manifest = gr.Code(label="Relay job manifest", language="json")
    table = gr.Dataframe(label="Relay job register", value=job_rows, interactive=False)
    export = gr.File(label="CSV export")
    with gr.Row():
        checkout_email = gr.Textbox(label="Checkout email")
        checkout_relay = gr.Textbox(label="Relay ID")
    checkout_btn = gr.Button("Create Stripe checkout")
    checkout_url = gr.Textbox(label="Checkout URL")
    create.click(ui_create, [email, item, pickup, dropoff, mode, distance, minutes, proof, notes], [manifest, table, export])
    checkout_btn.click(ui_checkout, [checkout_email, checkout_relay], [checkout_url])

app = gr.mount_gradio_app(api, demo, path="/")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "7860")))
