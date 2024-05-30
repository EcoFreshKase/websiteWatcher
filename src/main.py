import json
from WebsiteWatcher import WebsiteWatcher

config = json.load(open("config.json"))

watchers = [WebsiteWatcher(website.get("url"), website.get("elementQuery"), website.get("expectedExpressions")) for website in config.get("websites")]

for watcher in watchers:
    print(watcher.check())
