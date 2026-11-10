from app.api import fetch_posts
from app.processor import process_posts
from app.pdf_generator import generate_pdf


def main():

    print("AUTOMATED PDF REPORT GENERATOR")
    print("------------------------------")

    print("Step 1: Fetching data...")

    posts = fetch_posts(10)

    print("Step 2: Processing data...")

    stats = process_posts(posts)

    print("Step 3: Generating PDF...")

    generate_pdf(stats, posts)

    print("All tasks completed successfully!")


if __name__ == "__main__":
    main()