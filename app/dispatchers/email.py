from .base import Dispatcher
import smtplib, logging
from email.message import EmailMessage
from ..settings import settings

log = logging.getLogger(__name__)


class EmailDispatcher(Dispatcher):
    def send(self, notif):
        msg = EmailMessage()
        msg["From"] = settings.EMAIL_FROM
        msg["To"] = f"user-{notif.user_id}@example.com"
        msg["Subject"] = notif.subject or "Notification"
        msg.set_content(notif.message)
        with smtplib.SMTP("mailhog", 1025) as smtp:
            smtp.send_message(msg)
        log.info("Email sent -> %s", msg["To"])
