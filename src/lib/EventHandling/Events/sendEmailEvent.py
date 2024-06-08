from .baseEvent import Event

class SendEmailEvent(Event):
    def __init__(self, recipient: str, subject: str, body: str):
        self.recipient = recipient
        self.subject = subject
        self.body = body
