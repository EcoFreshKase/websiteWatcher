import re
from bs4 import BeautifulSoup
import requests


class WebsiteWatcher:
    def __init__(self, url, elementQuery, expectedExpressions):
        self.url = url
        self.elementQuery = elementQuery
        self.expectedExpressions = [re.compile(expectedText) for expectedText in expectedExpressions]

    def check(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')

        texts = [element.get_text() for element in soup.select(self.elementQuery)]

        for expression in self.expectedExpressions:
            for text in texts:
                if expression.search(text):
                    return True

        print(f"Expression not found on '{self.url}' with selector: '{self.elementQuery}': \n\t{expression.pattern}")
        return False
    
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"WebsiteWatcher(url='{self.url}', elementQuery='{self.elementQuery}', expectedExpressions={self.expectedExpressions})"
    