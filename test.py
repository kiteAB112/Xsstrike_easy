import sys
import os

import core.config
from urllib.parse import urlparse

target = "http://localhost:82/vul/xss/xss_reflected_get.php?message=%3Cscript%3Ealert(%22caker%22)%3C%2fscript%3E&submit=submit"
host = urlparse(target).netloc

print(host)

