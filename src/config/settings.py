from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Leer variables
SESSIONID = os.getenv("INSTAGRAM_SESSIONID")
TARGET_USER = os.getenv("TARGET_USER")
LIMIT = int(os.getenv("LIMIT", "50"))