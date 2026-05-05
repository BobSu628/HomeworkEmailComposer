import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_email(to, subject, html):
    response = requests.post(
        "https://api.resend.com/emails",
        headers={
            "Authorization": f"Bearer {os.getenv('RESEND_API_KEY')}",
            "Content-Type": "application/json",
        },
        json={
            "from": os.getenv("FROM_EMAIL"),
            "to": [to],
            "subject": subject,
            "html": html,
        },
    )

    return response.json()
