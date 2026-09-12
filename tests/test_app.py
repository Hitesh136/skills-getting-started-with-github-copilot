from fastapi.testclient import TestClient

from src.app import app, activities

client = TestClient(app)


def setup_function():
    activities["Chess Club"]["participants"] = ["michael@mergington.edu", "daniel@mergington.edu"]


def test_unregister_participant_removes_email():
    response = client.delete("/activities/Chess Club/participants?email=daniel@mergington.edu")

    assert response.status_code == 200
    assert response.json() == {"message": "Unregistered daniel@mergington.edu from Chess Club"}
    assert "daniel@mergington.edu" not in activities["Chess Club"]["participants"]


def test_unregister_participant_missing_email_returns_404():
    response = client.delete("/activities/Chess Club/participants?email=missing@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not registered for this activity"
