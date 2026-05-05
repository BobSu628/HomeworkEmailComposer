from app.sheets import fetch_sheet_data
from app.emailer import send_email
from app.template import generate_email

def run_job():
    print("Running job...")

    rows = fetch_sheet_data()

    for row in rows:
        if not row.get("email"):
            continue

        html = generate_email(row)

        send_email(
            row["email"],
            "Weekly Reminder",
            html
        )
