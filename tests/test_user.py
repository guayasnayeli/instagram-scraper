from scraper.user_scraper import extract_user_data

def test_extract_user_data():
    fake_response = {
        "data": {
            "user": {
                "id": "123",
                "username": "testuser",
                "full_name": "Test User",
                "biography": "Hola"
            }
        }
    }

    result = extract_user_data(fake_response)

    assert result["username"] == "testuser"
    assert result["full_name"] == "Test User"