import time

def extract_users(session, user_id, mode="followers", limit=None):
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
            # 🔥 CONTROL CORRECTO DEL LÍMITE
            if limit and len(users_list) >= limit:
                return users_list

            users_list.append({
                "id": user.get("pk"),
                "username": user.get("username"),
                "full_name": user.get("full_name"),
                "is_private": user.get("is_private"),
                "is_verified": user.get("is_verified"),
            })

        next_max_id = data.get("next_max_id")

        if not next_max_id:
            break

        # 🔥 anti-bloqueo
        time.sleep(1)

    return users_list