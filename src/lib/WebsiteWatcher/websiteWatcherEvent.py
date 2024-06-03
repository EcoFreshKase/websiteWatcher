class WebsiteWatcherEvent:
    def __init__(self, websiteUrl: str, checkResult: bool):
        self.websiteUrl = websiteUrl
        self.checkResult = checkResult
        
    def __str__(self):
        return f"WebsiteWatcherEvent(website='{self.websiteUrl}', checkResult='{self.checkResult}')"
