import json
from time import sleep
from lib.WebsiteWatcher import WebsiteWatcher
from pydispatch import dispatcher
from lib.EventHandling.debugListener import debug_listener

config = json.load(open("config.json"))

watchers = [WebsiteWatcher(website.get("url"), website.get("elementQuery"), website.get("expectedExpressions")) for website in config.get("websites")]

dispatcher.connect(
    debug_listener,
    signal=dispatcher.Any,
    sender=dispatcher.Any
)

while True:
    for watcher in watchers:
        print(watcher.check())
    sleep(10)

