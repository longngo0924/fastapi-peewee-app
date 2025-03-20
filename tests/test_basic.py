def test_app_startup(client):
    """Test that the client fixture is working properly."""
    response = client.get("/")
    # The default route might return 404, but that's OK for this test
    # We're just checking that the client is properly set up
    assert response.status_code in (200, 404) 