from app.processor import process_posts


def test_process_posts():

    posts = [
        {"id": 1, "userId": 1, "title": "Hello World"},
        {"id": 2, "userId": 2, "title": "Python Programming"}
    ]

    result = process_posts(posts)

    assert result["total_posts"] == 2
    assert result["total_users"] == 2
    assert result["average_title_length"] == 14.5


def test_empty_posts():

    posts = []

    result = process_posts(posts)

    assert result["total_posts"] == 0
    assert result["total_users"] == 0
    assert result["average_title_length"] == 0