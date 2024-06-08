from email.message import EmailMessage
import smtplib
from .emailNotifier import EmailNotifier

class GoogleSmtpService(EmailNotifier):
    """A class that represents a Google SMTP service for sending emails.
    
    (You can get the your app password from https://myaccount.google.com/apppasswords)

    Args:
        EmailNotifier (type): The base class for email notifiers.

    Attributes:
        sender (str): The email address of the sender.
        appPassword (str): The application password for authentication.

    """

    def __init__(self, sender: str, appPassword: str) -> None:
        super().__init__()
        self.sender = sender
        self.appPassword = appPassword

    def sendMail(self, mail):
        """Sends an email using the Google SMTP service.

        Args:
            mail: The email message to be sent.

        """
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s:
            s.login(self.sender, self.appPassword)
            s.send_message(mail)

    def createEmail(self, emailEvent):
        """Creates an email message.

        Args:
            emailEvent: The event containing the email details.

        Returns:
            EmailMessage: The created email message.

        """
        msg = EmailMessage()
        msg.set_content(f"{emailEvent.body}\nThis is an automated message. Do not reply.")
        msg['Subject'] = emailEvent.subject
        msg['From'] = self.sender
        msg['To'] = emailEvent.recipient
        return msg
