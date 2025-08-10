import requests
import warnings

import core.config
from core.log import logger

logger = logger(__name__)

warnings.filterwarnings("ignore") # Disable SSl related warnings


def requester(url,data,headers):
    



    try:
        response = requests.get(url,data=data,headers=headers)
    except:
        response = requests.post(url,data=data,headers=headers)
    return response






