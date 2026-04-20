import requests
from config.settings import SESSIONID

def create_session():
    session = requests.Session()

    # Headers para simular navegador
    session.headers.update({
        "User-Agent": "Mozilla/5.0",
        "x-ig-app-id": "936619743392459"
    })

    # Si tienes cookie, la agregas
    if SESSIONID:
        session.cookies.set("sessionid", SESSIONID)

    return session