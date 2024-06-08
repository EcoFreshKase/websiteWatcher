from email.message import EmailMessage
from abc import ABC, abstractmethod

from lib.EventHandling.EventHandler import EventHandler
from lib.EventHandling.Events.sendEmailEvent import SendEmailEvent
from lib.EventHandling.onEvent import onEvent
from lib.config import SEND_EMAIL_SIGNAL

class EmailNotifier(ABC, EventHandler):
    def __init__(self) -> None:
        self.startEventListener()

    @abstractmethod
    def sendMail(self, mail: EmailMessage) -> None:
        pass

    @onEvent(SEND_EMAIL_SIGNAL)
    def notify(self, event: SendEmailEvent) -> None:
        self.sendMail(self.createEmail(event))

    @abstractmethod
    def createEmail(self, emailEvent: SendEmailEvent) -> EmailMessage:
        pass
