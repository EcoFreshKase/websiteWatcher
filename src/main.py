import json
from time import sleep
from lib.WebsiteWatcher.websiteWatcher import WebsiteWatcher
from lib.EventHandling.debugListener import debug_listener
from lib.NotifyHandler.emailNotifier.googleSmtpService import GoogleSmtpService
from lib.EventHandling.emitAsEvent import emitAsEvent
from lib.config import SEND_EMAIL_SIGNAL
from lib.EventHandling.Events.sendEmailEvent import SendEmailEvent

config = json.load(open("config.json"))

emailSender = config.get("emailNotification").get("googleSmtp").get("sender")
googleAppPassword = config.get("emailNotification").get("googleSmtp").get("appPassword")

watchers = [WebsiteWatcher(website.get("url"), website.get("elementQuery"), website.get("expectedExpressions")) for website in config.get("websites")]
notifier = GoogleSmtpService(emailSender, googleAppPassword)

# for watcher in watchers:
#     watcher.startChecking()
#     print("started watching", watcher)

@emitAsEvent(SEND_EMAIL_SIGNAL)
def sendEmailEvent():
    return SendEmailEvent(emailSender, "Website changed", "Hello, this is a test")

print("sending email event")
sendEmailEvent()

sleep(10)
