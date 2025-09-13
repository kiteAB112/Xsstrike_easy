import sys
import os
import re

import core.config
from urllib.parse import urlparse

target = "http://localhost:82/vul/xss/xss_reflected_get.php?message=%3Cscript%3Ealert(%22caker%22)%3C%2fscript%3E&submit=submit"
# host = urlparse(target).netloc

# print(host)

xsschecker = 'test_xss' 

def extractScripts(response):
    scripts = []
    # 正则匹配所有<script>标签内的内容（不区分大小写）
    matches = re.findall(r'(?s)<script.*?>(.*?)</script>', response.lower())
    print(matches)
    for match in matches:
        if xsschecker in match:
            scripts.append(match)
    return scripts

# 测试用的response内容
response = """
<html>
  <body>
    <script>alert('hello');</script>
    <script type="text/javascript">
      var a = 'test_xss';
      console.log(a);
    </script>
    <script>var b = 'other';</script>
  </body>
</html>
"""

# 调用函数并打印结果
print(extractScripts(response))