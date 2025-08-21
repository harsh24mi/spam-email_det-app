import pytest
from app import create_app

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # Create the app with a specific testing configuration if needed
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


def test_predict_success(client):
    """
    Test the /api/predict endpoint with a valid request.
    It should return a 200 OK status and a valid JSON response.
    """
    # GIVEN a test client
    # WHEN a POST request is made to /api/predict with valid data
    response = client.post(
        "/api/predict",
        json={"email_text": "This is a fantastic product!"}
    )
    
    # THEN check the response
    assert response.status_code == 200
    json_data = response.get_json()
    assert "prediction" in json_data
    assert json_data["prediction"] in ["spam", "not spam"]


def test_predict_empty_text(client):
    """
    Test the /api/predict endpoint with an empty request.
    It should return a 400 Bad Request error.
    """
    # GIVEN a test client
    # WHEN a POST request is made with empty text
    response = client.post(
        "/api/predict",
        json={"email_text": ""}
    )
    
    # THEN check for the correct error response
    assert response.status_code == 400
    json_data = response.get_json()
    assert "error" in json_data
    assert "cannot be empty" in json_data["error"]