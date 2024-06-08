from .baseEvent import Event

class WebsiteWatcherEvent(Event):
    def __init__(self, websiteUrl: str, success: bool):
        self.websiteUrl = websiteUrl
        self.success = success
