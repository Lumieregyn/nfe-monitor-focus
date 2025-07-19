from fastapi import FastAPI, Request
from .scheduler import start_scheduler

app = FastAPI(title="Monitor NF-e Focus API")

@app.on_event("startup")
def startup_event():
    start_scheduler()

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Monitoramento NF-e Focus ativo"}

@app.post("/webhook/nfe")
async def receber_webhook(request: Request):
    payload = await request.json()
    print("🚨 Webhook recebido da Focus NFe:")
    print(payload)
    return {"received": True}
