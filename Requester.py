# base request class to use to simplify code
import requests
import json
from dotenv import load_dotenv
import os

class Requester:
    def __init__(self) -> None:
        load_dotenv()
        # this is the key for any api on rapid api
        self.rapidApiKey = os.getenv('RAPID_API_KEY')
    
    # the following functions are for apis that are hosted on rapid api
    # might need to have another function for apis not on rapid api
    def makeGETRequest(self, apiBaseURL: str, hostURL: str, params: dict):
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
        responseCode = response.status_code
        response = json.loads(response.text)
        # handle the reaponse code here ideally
        if responseCode == 200:
            return response
        elif 400 <= responseCode <= 499:
            raise Exception('The response is a 400 status code')
        else:
            raise Exception('The response is a 500 status code')
        
    ## might not need further request types in this stage (post raspberry pi recipe server)
    def makePOSTRequest():
        pass


if __name__ == "__main__":
    # testing using weather API
    req = Requester()
    load_dotenv()
    baseURL = os.getenv('WEATHER_URL')
    city = 'London'
    hostURL = os.getenv('WEATHER_HOST_URL')

    params = {
        "q":"falls church",
        "cnt":"1",
        "mode":"null",
        "lon":"0",
        "type":"link, accurate",
        "lat":"0",
        "units":"imperial, metric"
    }

    code, response = req.makeGETRequest(baseURL, hostURL, params=params)
    print(response)
    print(code)

    
