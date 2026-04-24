def extract_comments(session, post_id, limit=3):
    url = f"https://i.instagram.com/api/v1/media/{post_id}/comments/"
    r = session.get(url)

    results = []

    if r.status_code != 200:
        return results

    data = r.json()
    comments = data.get("comments", [])

    for c in comments[:limit]:
        results.append({
            "username": c.get("user", {}).get("username"),
            "text": c.get("text")
        })

    return results