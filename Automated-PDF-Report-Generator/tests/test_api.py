from app.api import fetch_posts
import app.api
import requests


def test_fetch_posts(monkeypatch):

    expected_data = [
        {"id": 1, "userId": 1, "title": "Test Post"}
    ]

    class MockResponse:

        def raise_for_status(self):
            pass

        def json(self):
            return expected_data

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(app.api.requests, "get", mock_get)

    result = fetch_posts(1)

    assert result == expected_data


def test_fetch_posts_error(monkeypatch):

    def mock_get(*args, **kwargs):
        raise requests.exceptions.ConnectionError("Connection failed")

    monkeypatch.setattr(app.api.requests, "get", mock_get)

    try:
        fetch_posts(1)
        assert False, "Expected RuntimeError"

    except RuntimeError as error:
        assert "API Error" in str(error)