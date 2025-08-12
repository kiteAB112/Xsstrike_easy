from urllib.parse import urlparse
import sys
import os

import core.config  
from core.log import setup_logger

logger = setup_logger(__name__)

def scan(target,paramData):
    GET,POST = (False,True) if paramData else (True,False)
    # # If the user hasn't supplied the root url with http(s),we will handle it
    # if not target.startswith('http'):
    #     try:
    #         response = requester('http://'+target)
    #     except:
    #         target = 'https://' + target

    logger.debug(f"Scanning {target}")

    host = urlparse(target).netloc # 



target = "http://localhost:82/vul/xss/xss_reflected_get.php?message=%3Cscript%3Ealert(%22caker%22)%3C%2fscript%3E&submit=submit"
host = urlparse(target).netloc

print(host)



    











