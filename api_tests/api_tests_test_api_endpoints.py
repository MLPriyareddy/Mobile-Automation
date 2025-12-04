import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user_details():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200

    user = response.json()

    assert user["id"] == 1
    assert "email" in user


def test_create_post():
    payload = {
        "title": "Automation Post",
        "body": "This is created using automation",
        "userId": 10
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201

    new_post = response.json()
    assert new_post["title"] == payload["title"]
    assert new_post["userId"] == payload["userId"]
