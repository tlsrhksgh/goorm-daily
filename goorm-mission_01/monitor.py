import os
import time
import smtplib
from email.message import EmailMessage
from datetime import datetime
from dotenv import load_dotenv
import docker_check as dc

load_dotenv()

CONTAINER_NAME = os.getenv("DOCKER_CONTAINER_NAME", "")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "5"))

GMAIL_USER = os.getenv("GMAIL_USER", "")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD", "")
MAIL_TO = os.getenv("MAIL_TO", "")

def send_mail(subject: str, body: str):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = GMAIL_USER
    msg['To'] = MAIL_TO
    msg.set_content(body)

    with smtplib.SMTP('smtp.gmail.com', 587, timeout=15) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        smtp.send_message(msg)


def now_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
   while True:
        error_containers = dc.check_error_container()
        if error_containers != None:
            subject = f"[Docker Alert] {error_containers['name']} status: {error_containers['status']}"
            body = "\n".join([
                            f"time: {now_time()}",
                            f"container: {error_containers['name']}",
                            f"status: {error_containers['status']}",
                        ])

            send_mail(subject, body)

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()