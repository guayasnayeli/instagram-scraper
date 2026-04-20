from session.session_manager import create_session
from config.settings import TARGET_USER

def main():
    session = create_session()

    url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={TARGET_USER}"

    response = session.get(url)

    print("Status:", response.status_code)

    try:
        data = response.json()
        print("Respuesta recibida correctamente")
        print(data)
    except:
        print("Error al obtener JSON")
        print(response.text)


if __name__ == "__main__":
    main()