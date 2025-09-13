import requests
import warnings

# import core.config
# from core.log import logger

# logger = logger(__name__)

warnings.filterwarnings("ignore") # Disable SSl related warnings


def requester(url,data,GET):
    
    try:
        if GET:
            response = requests.get(url)
        else:
            response = requests.post(url,data=data)

        return response
    except:
        print('Unable to connect to the target.')
        return requests.Response()






