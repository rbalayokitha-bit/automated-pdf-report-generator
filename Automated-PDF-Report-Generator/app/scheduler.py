from apscheduler.schedulers.blocking import BlockingScheduler

from app.api import fetch_posts
from app.processor import process_posts
from app.pdf_generator import generate_pdf
def generate_report():

    print("\nStarting automated report generation...")

    posts = fetch_posts(10)

    stats = process_posts(posts)

    generate_pdf(stats, posts)

    print("Automated report completed!")


def main():

    scheduler = BlockingScheduler()

    scheduler.add_job(
        generate_report,
        trigger="interval",
        minutes=1
    )

    print("Automated Report Scheduler Started!")
    print("A new PDF will be generated every 1 minute.")

    try:
        scheduler.start()

    except (KeyboardInterrupt, SystemExit):
        print("Scheduler stopped.")


if __name__ == "__main__":
    main()