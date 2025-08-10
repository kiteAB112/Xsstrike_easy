globalVariables = {} # holds variables during runtime


proxy = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
} # proxy to use for requests,change here

# timeout for requests
timeout = 10 # in seconds

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
} # default headers for requests

# payloads to use for testing
payloads = (
    "<script>alert(1)</script>",
)



