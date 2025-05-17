from .base import Dispatcher
import logging, time

log = logging.getLogger(__name__)


class SMSDispatcher(Dispatcher):
    def send(self, notif):
        # Fake SMS send
        log.info("SMS sent to user %s: %s", notif.user_id, notif.message)
        time.sleep(0.2)
