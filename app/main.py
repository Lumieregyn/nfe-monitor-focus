from fastapi import FastAPI, Request
from .scheduler import start_scheduler
from .storage import init_db, salvar_nfe

app = FastAPI(title="Monitor NF-e Focus API")

@app.on_event("startup")
def startup_event():
    init_db()
    start_scheduler()

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Monitoramento NF-e Focus ativo"}

@app.post("/webhook/nfe")
async def receber_webhook(request: Request):
    payload = await request.json()

    # Salva no banco
    salvar_nfe(payload)

    print(f"✅ NF-e salva: {payload.get('chave_nfe')} de {payload.get('nome_emitente')}")
    return {"status": "ok", "message": "Webhook recebido e salvo com sucesso"}
from .storage import listar_nfes

@app.get("/nfes")
def listar_notas():
    notas = listar_nfes()
    return {"total": len(notas), "notas": notas}
