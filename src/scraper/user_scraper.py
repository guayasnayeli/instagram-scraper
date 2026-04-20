def extract_user_data(json_data):
    user = json_data.get("data", {}).get("user", {})

    return {
        "id": user.get("id"),
        "username": user.get("username"),
        "full_name": user.get("full_name"),
        "bio": user.get("biography"),
        "followers": user.get("edge_followed_by", {}).get("count"),
        "following": user.get("edge_follow", {}).get("count"),
    }