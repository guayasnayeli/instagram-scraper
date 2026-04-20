from session.session_manager import create_session
from config.settings import TARGET_USER
from scraper.user_scraper import extract_user_data
from scraper.followers_scraper import extract_followers

def main():
    session = create_session()

    # 1. Obtener info del usuario
    url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={TARGET_USER}"
    response = session.get(url)

    data = response.json()

    user_data = extract_user_data(data)

    print("\n=== USER DATA ===")
    for key, value in user_data.items():
        print(f"{key}: {value}")

    # 🔥 2. Obtener user_id
    user_id = user_data.get("id")

    if not user_id:
        print("No se pudo obtener el user_id")
        return

    # 🔥 3. Obtener followers
    followers = extract_followers(session, user_id, limit=5)

    print("\n=== FOLLOWERS ===")
    for f in followers:
        print(f)

if __name__ == "__main__":
    main()