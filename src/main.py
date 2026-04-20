from session.session_manager import create_session
from config.settings import TARGET_USER, LIMIT
from scraper.user_scraper import extract_user_data
from scraper.relationships_scraper import extract_users


def get_user_input(default_user, default_limit):
    user = input(f"Usuario (Enter={default_user}): ").strip() or default_user

    option = input("1=followers, 2=following, 3=ambos: ").strip()

    limit_input = input(f"Cantidad (Enter={default_limit} o 'all'): ").strip()

    if not limit_input:
        limit = default_limit
    elif limit_input.lower() == "all":
        limit = None
    else:
        try:
            limit = int(limit_input)
        except:
            print("Valor inválido, usando default.")
            limit = default_limit

    return user, option, limit


def main():
    session = create_session()

    # 🔥 INPUT DINÁMICO
    user, option, limit = get_user_input(TARGET_USER, LIMIT)

    # 🔹 Obtener info del usuario
    url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={user}"
    response = session.get(url)

    if response.status_code != 200:
        print(f"Error al obtener usuario: {response.status_code}")
        return

    data = response.json()
    user_data = extract_user_data(data)

    print("\n=== USER DATA ===")
    for key, value in user_data.items():
        print(f"{key}: {value}")

    # 🔹 Obtener user_id
    user_id = user_data.get("id")

    if not user_id:
        print("No se pudo obtener el user_id")
        return

    # 🔥 LÓGICA SEGÚN OPCIÓN

    if option == "1":
        print("\n=== FOLLOWERS ===")
        users = extract_users(session, user_id, mode="followers", limit=limit)

        for u in users:
            print(u)

    elif option == "2":
        print("\n=== FOLLOWING ===")
        users = extract_users(session, user_id, mode="following", limit=limit)

        for u in users:
            print(u)

    elif option == "3":
        print("\n=== FOLLOWERS ===")
        followers = extract_users(session, user_id, mode="followers", limit=limit)

        for f in followers:
            print(f)

        print("\n=== FOLLOWING ===")
        following = extract_users(session, user_id, mode="following", limit=limit)

        for f in following:
            print(f)

    else:
        print("Opción inválida")


if __name__ == "__main__":
    main()