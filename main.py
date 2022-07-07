
import requests
from bs4 import BeautifulSoup
import sys
import re

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the download URL")

r = requests.get(url)

print("Download about to start")

soup = BeautifulSoup(r.content, features="lxml")