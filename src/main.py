from session.session_manager import create_session
from config.settings import TARGET_USER
from scraper.user_scraper import extract_user_data

def main():
    session = create_session()

    url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={TARGET_USER}"
    response = session.get(url)

    data = response.json()

    user_data = extract_user_data(data)

    print("\n=== USER DATA ===")
    for key, value in user_data.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()