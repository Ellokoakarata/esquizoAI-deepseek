import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent / '.env')

DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
BASE_URL = "https://api.deepseek.com"  # Se ajusta automáticamente
MODEL_NAME = "deepseek-reasoner"
TEMPERATURE = 0.7
MAX_TOKENS = 3000
STREAM = True

# Paths para los diferentes modos
REBEL_JSON_PATH = str(Path(__file__).parent / 'rebel.json')
NETHACKER_JSON_PATH = str(Path(__file__).parent / 'nethacker.json')

# Configuración de modos
MODES = {
    "esquizo": {
        "name": "EsquizoAI",
        "config_path": REBEL_JSON_PATH,
        "banner_color": "MAGENTA",
        "prompt_color": "YELLOW"
    },
    "nethacker": {
        "name": "NetHacker-X",
        "config_path": NETHACKER_JSON_PATH,
        "banner_color": "GREEN",
        "prompt_color": "CYAN"
    }
}