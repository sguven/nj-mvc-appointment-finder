"""Email yourself the days until the soonest NJ MVC initial-permit appointment.

Set these environment variables (use a Gmail app password, never your real password):
    GMAIL_USER          sender Gmail address
    GMAIL_APP_PASSWORD  16-character app password
    ALERT_TO            comma-separated recipients (defaults to GMAIL_USER)

Run on a schedule (cron, Task Scheduler) to get a daily update:
    python scripts/email_alert.py
"""
import os
import smtplib
import sys
from email.message import EmailMessage
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from nj_mvc import APPOINTMENT_TYPES, nearest_appointments  # noqa: E402

TYPE_ID = APPOINTMENT_TYPES["Initial permit (before knowledge test)"]


def main() -> None:
    user = os.environ["GMAIL_USER"]
    password = os.environ["GMAIL_APP_PASSWORD"]
    recipients = os.environ.get("ALERT_TO", user)

    try:
        days, places = nearest_appointments(TYPE_ID)
        body = f"{days} day(s) to the nearest appointment at {', '.join(places)}."
    except LookupError:
        body = "No initial-permit appointments are available right now."

    msg = EmailMessage()
    msg["From"], msg["To"], msg["Subject"] = user, recipients, "NJ MVC: nearest initial-permit appointment"
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(user, password)
        smtp.send_message(msg)
    print("Email sent:", body)


if __name__ == "__main__":
    main()
