def get_user_details(session, username):
    url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"

    res = session.get(url)

    if res.status_code != 200:
        return {}

    user = res.json().get("data", {}).get("user", {})

    return {
        "bio": user.get("biography"),
        "followers_count": user.get("edge_followed_by", {}).get("count"),
        "following_count": user.get("edge_follow", {}).get("count"),
        "posts_count": user.get("edge_owner_to_timeline_media", {}).get("count"),
    }