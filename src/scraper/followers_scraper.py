def extract_followers(session, user_id, limit=None):
    followers = []
    has_next_page = True
    end_cursor = None

    while has_next_page:
        url = "https://i.instagram.com/api/v1/friendships/{}/followers/".format(user_id)

        params = {}
        if end_cursor:
            params["max_id"] = end_cursor

        response = session.get(url, params=params)

        if response.status_code != 200:
            print("Error en request:", response.status_code)
            break

        data = response.json()

        users = data.get("users", [])

        for user in users:
            followers.append({
                "id": user.get("pk"),
                "username": user.get("username"),
                "full_name": user.get("full_name")
            })

            # aplicar límite
            if limit and len(followers) >= limit:
                return followers

        # paginación
        has_next_page = data.get("next_max_id") is not None
        end_cursor = data.get("next_max_id")

    return followers