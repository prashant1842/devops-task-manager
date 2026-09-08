import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_add_task():
    client = app.test_client()

    response = client.post(
        "/add",
        data={"task": "Test CI/CD"}
    )

    assert response.status_code == 302


def test_complete_task():
    client = app.test_client()

    response = client.get("/complete/1")

    assert response.status_code == 302


def test_delete_task():
    client = app.test_client()

    response = client.get("/delete/1")

    assert response.status_code == 302