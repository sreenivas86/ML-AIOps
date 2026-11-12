
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# Sample valid housing data
VALID_HOUSE_DATA = {
    "MedInc": 8.3252,
    "HouseAge": 41.0,
    "AveRooms": 6.984127,
    "AveBedrms": 1.023810,
    "Population": 322.0,
    "AveOccup": 2.555556,
    "Latitude": 37.88,
    "Longitude": -122.23
}


def test_health_endpoint():

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json()["status"] == "healthy"

    assert response.json()["model_loaded"] is True


def test_predict_valid_input():

    response = client.post(
        "/predict",
        json=VALID_HOUSE_DATA
    )

    assert response.status_code == 200

    result = response.json()

    assert "predicted_value_usd" in result

    assert "predicted_value_100k_usd" in result

    assert result["predicted_value_usd"] > 0

    assert result["currency"] == "USD"


def test_predict_invalid_medinc():

    invalid_data = VALID_HOUSE_DATA.copy()

    invalid_data["MedInc"] = "invalid"

    response = client.post(
        "/predict",
        json=invalid_data
    )

    assert response.status_code == 422


def test_predict_negative_medinc():

    invalid_data = VALID_HOUSE_DATA.copy()

    invalid_data["MedInc"] = -5

    response = client.post(
        "/predict",
        json=invalid_data
    )

    assert response.status_code == 422


def test_predict_missing_feature():

    invalid_data = VALID_HOUSE_DATA.copy()

    del invalid_data["Longitude"]

    response = client.post(
        "/predict",
        json=invalid_data
    )

    assert response.status_code == 422
