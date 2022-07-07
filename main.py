
import requests

import sys 

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the download URL")
