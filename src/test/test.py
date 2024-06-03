import requests
import sys
import os
sys.path.append(os.getcwd())
sys.path.append(os.path.abspath(".."))

from src.lib.WebsiteWatcher.websiteWatcher import WebsiteWatcher
from testServer import TestServer

server = TestServer(8000)
server.startServer()

watcher = WebsiteWatcher("http://localhost:8000/", "h1", ["My Website"])

assert watcher.check().success == True

requests.post("http://localhost:8000/", data=b"<html><body><h1>Changed Text!</h1></body></html>")

assert watcher.check().success == False

server.stopServer()

print("\033[92mAll tests passed!\033[0m")