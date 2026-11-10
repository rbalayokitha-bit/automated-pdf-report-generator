import app.cli


def test_cli(monkeypatch):

    monkeypatch.setattr(
        "sys.argv",
        ["cli.py", "--limit", "5"]
    )

    def mock_fetch_posts(limit):
        assert limit == 5
        return [{"id": 1, "userId": 1, "title": "Test"}]

    def mock_process_posts(posts):
        return {
            "total_posts": 1,
            "total_users": 1,
            "average_title_length": 4
        }

    def mock_generate_pdf(stats, posts):
        assert stats["total_posts"] == 1

    monkeypatch.setattr(
        app.cli, "fetch_posts", mock_fetch_posts
    )

    monkeypatch.setattr(
        app.cli, "process_posts", mock_process_posts
    )

    monkeypatch.setattr(
        app.cli, "generate_pdf", mock_generate_pdf
    )

    app.cli.main()