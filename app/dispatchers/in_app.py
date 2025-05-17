from .base import Dispatcher
import logging, time

log = logging.getLogger(__name__)


class InAppDispatcher(Dispatcher):
    def send(self, notif):
        # Stub: store to in-app table or websocket
        log.info("In-app notification for user %s: %s", notif.user_id, notif.message)
        time.sleep(0.1)
