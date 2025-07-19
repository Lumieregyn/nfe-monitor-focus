from apscheduler.schedulers.background import BackgroundScheduler
from .focus_client import listar_nfe_recebidas

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(listar_nfe_recebidas, 'interval', minutes=15)
    scheduler.start()
    print("⏰ Agendador iniciado (consulta a cada 15 minutos).")
