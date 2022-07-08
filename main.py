
from multiprocessing.sharedctypes import Value
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

# Match mp4 file
# find the script that contains talkpage.init param then store the Value.
# this script contains the mp4 files for the 
for val in soup.findAll("script"):
    if(re.search("talkPage.init",str(val))) is not None:
        result = str(val)

result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")