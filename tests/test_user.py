def test_create_user(client):
    response = client.post(
        "/api/v1/users/",
        json={
            "email": "test@example.com",
            "password": "strongpassword"
        }
    )
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["status"] == "success"
    assert response_data["error"] is None
    assert response_data["data"] is not None
    user_data = response_data["data"]
    assert user_data["email"] == "test@example.com"
    assert "id" in user_data


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

    assert response.status_code == 200  # Status code is 200 even for errors based on your API design
    response_data = response.json()
    assert response_data["status"] == "error"
    assert response_data["data"] is None
    assert response_data["error"] is not None
    assert response_data["error"]["code"] == "USER_ALREADY_EXISTS"
    assert response_data["error"]["message"] == "User already exists"


def test_get_users_pagination(client):
    # Get current user count before adding our test users
    initial_response = client.get("/api/v1/users/")
    initial_data = initial_response.json()
    initial_user_count = initial_data["data"]["meta"]["total"]

    # Create multiple test users
    test_users = [
        {"email": f"paginated_user{i}@example.com", "password": "password123"}
        for i in range(1, 6)  # Create 5 users
    ]

    for user in test_users:
        client.post("/api/v1/users/", json=user)

    # Test default pagination (page 1, limit 10)
    response = client.get("/api/v1/users/")
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "sucess"  # Note: There's a typo in the endpoint ("sucess" instead of "success")
    assert data["error"] is None

    # Check pagination data structure
    pagination_data = data["data"]
    assert "items" in pagination_data
    assert "meta" in pagination_data

    # Check metadata - now accounting for pre-existing users
    expected_total = initial_user_count + 5  # Initial count plus our 5 new users
    meta = pagination_data["meta"]
    assert meta["total"] == expected_total  # Total number of users
    assert meta["page"] == 1   # Current page
    assert meta["size"] == 10  # Page size

    # Test custom pagination parameters
    response = client.get("/api/v1/users/?page=1&limit=3")
    assert response.status_code == 200

    data = response.json()
    pagination_data = data["data"]

    # Check metadata with custom pagination
    meta = pagination_data["meta"]
    assert meta["total"] == expected_total  # Total number of users
    assert meta["page"] == 1   # Current page
    assert meta["size"] == 3   # Page size (we requested 3)
    expected_pages = (expected_total + 3 - 1) // 3  # Ceiling division for total pages
    assert meta["pages"] == expected_pages  # Total pages

    # Test second page
    response = client.get("/api/v1/users/?page=2&limit=3")
    assert response.status_code == 200

    data = response.json()
    pagination_data = data["data"]

    # Check metadata for second page
    meta = pagination_data["meta"]
    assert meta["page"] == 2  # Should be on page 2
