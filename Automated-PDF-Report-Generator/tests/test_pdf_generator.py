from pathlib import Path
from app.pdf_generator import generate_pdf


def test_generate_pdf():

    stats = {
        "total_posts": 2,
        "total_users": 2,
        "average_title_length": 14.5
    }

    posts = [
        {"id": 1, "userId": 1, "title": "Hello World"},
        {"id": 2, "userId": 2, "title": "Python Programming"}
    ]

    generate_pdf(stats, posts)

    project_folder = Path(__file__).resolve().parent.parent

    pdf_path = project_folder / "reports" / "report.pdf"

    assert pdf_path.exists()
    assert pdf_path.stat().st_size > 0