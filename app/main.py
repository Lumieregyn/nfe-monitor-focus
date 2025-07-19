from fastapi import FastAPI
from .scheduler import start_scheduler

app = FastAPI(title="Monitor NF-e Focus API")

@app.on_event("startup")
def startup_event():
    start_scheduler()

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Monitoramento NF-e Focus ativo"}
