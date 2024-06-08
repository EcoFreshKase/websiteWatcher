import re
import requests
from bs4 import BeautifulSoup
from ..EventHandling.Events.websiteWatcherEvent import WebsiteWatcherEvent
from ..config import WEBSITE_WATCHER_SIGNAL, WEBSITE_CHECKING_INTERVAL
from ..EventHandling.repeatEvery import repeatEvery
from ..EventHandling.emitAsEvent import emitAsEvent

class WebsiteWatcher:
    def __init__(self, url: str, elementQuery: str, expectedExpressions: list[str]):
        self.url = url
        self.elementQuery = elementQuery
        self.expectedExpressions = [re.compile(expectedText) for expectedText in expectedExpressions]
        self.checking = False

    def startChecking(self):
        """Start checking the website non blocking for the expected expressions in a specific interval. 
        """

        if not self.checking:
            self.checking = True
            self.__innerStartChecking()

    @repeatEvery(WEBSITE_CHECKING_INTERVAL)
    def __innerStartChecking(self):
        self.check()

    @emitAsEvent(signal=WEBSITE_WATCHER_SIGNAL)
    def check(self) -> WebsiteWatcherEvent:
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')

        texts = [element.get_text() for element in soup.select(self.elementQuery)]

        for expression in self.expectedExpressions:
            for text in texts:
                if expression.search(text):
                    return WebsiteWatcherEvent(self.url, True)

        print(f"Expression not found on '{self.url}' with selector: '{self.elementQuery}': \n\t{expression.pattern}")
        return WebsiteWatcherEvent(self.url, False)
    
    def __str__(self):
        return f"WebsiteWatcher(url='{self.url}', elementQuery='{self.elementQuery}', expectedExpressions={self.expectedExpressions})"
