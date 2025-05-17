from abc import ABC, abstractmethod

class Dispatcher(ABC):
    @abstractmethod
    def send(self, notif): ...
