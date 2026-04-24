def extract_posts(session, user_id, limit=5):
    posts = []
    next_max_id = None

    while True:
        url = f"https://i.instagram.com/api/v1/feed/user/{user_id}/"
        params = {"max_id": next_max_id} if next_max_id else {}

        r = session.get(url, params=params)
        if r.status_code != 200:
            print("Error posts:", r.status_code)
            break

        data = r.json()
        items = data.get("items", [])

        for item in items:
            if limit and len(posts) >= limit:
                return posts

            posts.append({
                "post_id": item.get("id"),
                "likes": item.get("like_count", 0),
                "comments": item.get("comment_count", 0),
                "caption": (item.get("caption") or {}).get("text", "")
            })

        next_max_id = data.get("next_max_id")
        if not next_max_id:
            break

    return posts