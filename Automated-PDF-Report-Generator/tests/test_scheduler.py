import app.scheduler


def test_scheduler_main(monkeypatch):

    class FakeScheduler:

        def add_job(self, function, trigger, minutes):

            assert function == app.scheduler.generate_report
            assert trigger == "interval"
            assert minutes == 1

        def start(self):

            raise KeyboardInterrupt

    monkeypatch.setattr(
        app.scheduler,
        "BlockingScheduler",
        FakeScheduler
    )

    app.scheduler.main()


def test_generate_report(monkeypatch):

    posts = [
        {"id": 1, "userId": 1, "title": "Test Post"}
    ]

    stats = {
        "total_posts": 1,
        "total_users": 1,
        "average_title_length": 9
    }

    monkeypatch.setattr(
        app.scheduler,
        "fetch_posts",
        lambda limit: posts
    )

    monkeypatch.setattr(
        app.scheduler,
        "process_posts",
        lambda data: stats
    )

    monkeypatch.setattr(
        app.scheduler,
        "generate_pdf",
        lambda result, data: None
    )

    app.scheduler.generate_report()