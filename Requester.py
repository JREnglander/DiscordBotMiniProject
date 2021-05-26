# base request class to use to simplify code
from typing_extensions import ParamSpec
import requests
import json

class Requester:
    def __init__(self) -> None:
        pass
    
    def makeGETRequest(apiBaseURL, headers=None, params=None, codeDictKey=0):
        """
        apiBaseURL: base url to make get requests
        headers: values to add to header of request
        params: values to add to body of request
        """
        # get the response as a python dictionary
        response = None
        if headers == None or params == None:
            if headers == None:
                response = json.loads(requests.get(apiBaseURL,params=params))
            elif params == None:
                # raise error since request cannot have no params
                raise noParamsRequestError
        else:
            response = json.loads(requests.get(apiBaseURL, headers, params))
        # handle the reaponse code here ideally
        # the codeDictkey is the key in the response dictionary
        # since various APIs might call it different things, 
        # we can just input it as a variable in the various requesters
        responseCode = response[codeDictKey]
        if responseCode == 200:
            return response
        elif responseCode == 404:
            return 404
        elif responseCode >= 500:
            return 500
        else: 
            # could not find the response code
            return 0
        
    
    ## might not need further request types in this stage (post raspberry pi recipe server)
    def makePOSTRequest():
        pass

class noParamsRequestError(Exception):
    """
    Raised when no params are given for a request
    """
    pass