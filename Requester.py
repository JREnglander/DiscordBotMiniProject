# base request class to use to simplify code
import requests
import json

class Requester:
    def __init__(self) -> None:
        pass
    
    def makeGETRequest(fullURL, codeDictKey):
        # get the response as a python dictionary
        response = json.loads(requests.get(fullURL))
        # handle the reaponse code here ideally
        # the codeDictkey is the key in the response dictionary
        # since various APIs might call it different things, 
        # we can just input it as a variable in the various requesters
        responseCode = response[codeDictKey]
        if responseCode == 200:
            return response
        elif responseCode == 404:
            return 404
        else:
            return 500
        
    
    ## might not need further request types in this stage (pre raspberry pi recipe server)
    def makePOSTRequest():
        pass