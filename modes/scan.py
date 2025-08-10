import core.config
from core.log import setup_logger

logger = setup_logger(__name__)

def scan(target,paramData):
    GET,POST = (False,True) if paramData else (True,False)
    # If the user hasn't supplied the root url with http(s),we will handle it
    if not target.startswith('http'):
        try:
            response = requester('http://'+target)
        except:
            target = 'https://' + target

    logger.debug(f"Scanning {target}")
    response = requester(target,)

        











