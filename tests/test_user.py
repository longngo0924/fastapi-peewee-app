def test_create_user(client):
    response = client.post(
        "/api/v1/users/",
        json={
            "email": "test@example.com",
            "password": "strongpassword"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data


def test_create_existing_user(client):
    # Create initial user
    client.post(
        "/api/v1/users/",
        json={"email": "existing@example.com", "password": "password"}
    )

    # Attempt to create the same user again
    response = client.post(
        "/api/v1/users/",
        json={"email": "existing@example.com", "password": "password"}
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "User already exists"
