from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from pathlib import Path


def generate_pdf(stats, posts):

    project_folder = Path(__file__).resolve().parent.parent

    report_folder = project_folder / "reports"

    report_folder.mkdir(exist_ok=True)

    pdf_path = report_folder / "report.pdf"

    document = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "AUTOMATED DATA ANALYSIS REPORT",
        styles["Title"]
    )

    content.append(title)

    content.append(Spacer(1, 0.3 * inch))

    content.append(Paragraph(
        "Project: Enterprise Python Automation",
        styles["Heading2"]
    ))

    content.append(Spacer(1, 0.2 * inch))

    content.append(Paragraph(
        "1. DATA SUMMARY",
        styles["Heading2"]
    ))

    summary_data = [
        ["Metric", "Value"],
        ["Total Posts", str(stats["total_posts"])],
        ["Total Users", str(stats["total_users"])],
        ["Average Title Length", str(stats["average_title_length"])]
    ]

    summary_table = Table(summary_data)

    summary_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("PADDING", (0, 0), (-1, -1), 8)
    ]))

    content.append(summary_table)

    content.append(Spacer(1, 0.3 * inch))

    content.append(Paragraph(
        "2. POST DETAILS",
        styles["Heading2"]
    ))

    post_data = [["Post ID", "Title"]]

    for post in posts:

        post_data.append([
            str(post["id"]),
            Paragraph(post["title"], styles["Normal"])
        ])

    post_table = Table(
        post_data,
        colWidths=[1 * inch, 5.5 * inch]
    )

    post_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("PADDING", (0, 0), (-1, -1), 8)
    ]))

    content.append(post_table)

    document.build(content)

    print("PDF Report Generated Successfully!")
    print("Saved at:", pdf_path)


if __name__ == "__main__":

    from api import fetch_posts
    from processor import process_posts

    posts = fetch_posts(10)

    stats = process_posts(posts)

    generate_pdf(stats, posts)