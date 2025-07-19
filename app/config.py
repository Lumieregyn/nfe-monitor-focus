import os
from dotenv import load_dotenv

load_dotenv()

FOCUS_API_BASE = "https://api.focusnfe.com.br/v2"
FOCUS_API_TOKEN = os.getenv("FOCUS_API_TOKEN")
CNPJ_EMPRESA = os.getenv("CNPJ_EMPRESA")
