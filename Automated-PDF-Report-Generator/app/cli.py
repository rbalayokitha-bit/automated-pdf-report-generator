import argparse

from app.api import fetch_posts
from app.processor import process_posts
from app.pdf_generator import generate_pdf


def main():

    parser = argparse.ArgumentParser(
        description="Automated PDF Report Generator"
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Number of posts to fetch"
    )

    args = parser.parse_args()

    print("Fetching data...")

    posts = fetch_posts(args.limit)

    print("Processing data...")

    stats = process_posts(posts)

    print("Generating PDF report...")

    generate_pdf(stats, posts)

    print("Report generation completed!")


if __name__ == "__main__":
    main()