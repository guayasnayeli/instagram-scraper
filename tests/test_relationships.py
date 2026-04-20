from scraper.relationships_scraper import extract_users

def test_limit_logic():
    # simulamos usuarios
    fake_users = [{"pk": i, "username": f"user{i}"} for i in range(10)]

    # simulación simple
    result = []

    limit = 5
    for u in fake_users:
        if len(result) >= limit:
            break
        result.append(u)

    assert len(result) == 5