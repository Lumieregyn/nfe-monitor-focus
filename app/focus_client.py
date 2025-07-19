import requests
from .config import FOCUS_API_BASE, FOCUS_API_TOKEN, CNPJ_EMPRESA

def listar_nfe_recebidas():
    url = f"{FOCUS_API_BASE}/nfe/recebidas?cnpj={CNPJ_EMPRESA}"
    headers = {"Authorization": f"Token {FOCUS_API_TOKEN}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        notas = response.json()
        print(f"✔ {len(notas)} nota(s) fiscal(is) recebida(s).")
        return notas
    except requests.exceptions.RequestException as e:
        print("❌ Erro ao consultar NF-e:", e)
        return []
