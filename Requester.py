# base request class to use to simplify code
import requests
import json
from dotenv import load_dotenv
import os

class Requester:
    def __init__(self) -> None:
        load_dotenv()
        self.rapidApiKey = os.getenv('RAPID_API_KEY')
    
    def makeGETRequest(self, apiBaseURL, hostURL, params, codeDictKey):
        """
        apiBaseURL: base url to make get requests
        headers: values to add to header of request
        params: values to add to body of request
        """
        # get the response as a python dictionary
        header = {
            'x-rapidapi-key': self.rapidApiKey,
            'x-rapidapi-host': hostURL
        }
        response = requests.request("GET", apiBaseURL,headers=header,params=params)
        print(response.text)
        response = json.loads(response.text)
        # handle the reaponse code here ideally
        # the codeDictkey is the key in the response dictionary
        # since various APIs might call it different things, 
        # we can just input it as a variable in the various requesters
        responseCode = response[codeDictKey]
        if type(responseCode) == str:
            responseCode = int(responseCode)
        
        if responseCode == 200:
            return 200, response
        elif responseCode >= 400:
            return 400, response
        elif responseCode >= 500:
            return 500, response
        else: 
            # could not find the response code
            return 0, response
        
    
    ## might not need further request types in this stage (post raspberry pi recipe server)
    def makePOSTRequest():
        pass

if __name__ == "__main__":
    # testing using weather API
    req = Requester()
    load_dotenv()
    baseURL = os.getenv('RAPID_API_WEATHER_URL')
    city = 'London'
    hostURL = os.getenv('RAPID_API_WEATHER_HOST_URL')

    params = {
        "q":"london",
        "cnt":"1",
        "mode":"null",
        "lon":"0",
        "type":"link, accurate",
        "lat":"0",
        "units":"imperial, metric"
    }

    response = req.makeGETRequest(baseURL,hostURL, params=params,codeDictKey='cod')

    