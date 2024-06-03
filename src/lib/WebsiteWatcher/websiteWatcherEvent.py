class WebsiteWatcherEvent:
    def __init__(self, websiteUrl: str, success: bool):
        self.websiteUrl = websiteUrl
        self.success = success
        
    def __str__(self):
        return f"WebsiteWatcherEvent(website='{self.websiteUrl}', checkResult='{self.success}')"
