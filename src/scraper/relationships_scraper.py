from datetime import datetime
import time
from scraper.user_details_scraper import get_user_details

def extract_users(session, user_id, mode="followers", limit=None, deep=False):
    """
    mode: 'followers' | 'following'
    """

    if mode not in ["followers", "following"]:
        raise ValueError("Modo inválido")

    users_list = []
    next_max_id = None

    while True:
        url = f"https://i.instagram.com/api/v1/friendships/{user_id}/{mode}/"

        params = {}
        if next_max_id:
            params["max_id"] = next_max_id

        response = session.get(url, params=params)

        if response.status_code != 200:
            print(f"Error en request: {response.status_code}")
            break

        data = response.json()
        users = data.get("users", [])

        for user in users:

            if limit and len(users_list) >= limit:
                return users_list

            # 🔥 1. CREAR OBJETO
            user_data = {
                "id": user.get("pk"),
                "username": user.get("username") or "",
                "full_name": user.get("full_name"),
                "is_private": user.get("is_private"),
                "is_verified": user.get("is_verified"),
                "profile_pic": user.get("profile_pic_url"),
                "is_business": user.get("is_business"),
                "is_professional": user.get("is_professional_account"),
                "scraped_at": datetime.now().isoformat()
            }

            # 🔥 2. ENRIQUECER (SI deep)
            if deep:
                extra = get_user_details(session, user.get("username"))
                user_data.update(extra)
                time.sleep(1)

            # 🔥 3. GUARDAR UNA SOLA VEZ
            users_list.append(user_data)

        next_max_id = data.get("next_max_id")

        if not next_max_id:
            break
        # 🔥 anti-bloqueo
        time.sleep(1)

    return users_list