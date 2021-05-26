# this file will access various Recipe APIs
import os
from dotenv import load_dotenv
import Requester

class foodRequester(Requester):
    def __init__(self) -> None:
        # get all the api keys
        load_dotenv()
        # for now make separate class attributes per api
        self.edamamKey = os.getenv('EDAMAM_SEARCH_API_KEY') 
        self.edamamID = os.getenv('EDAMAM_SEARCH_APP_ID')

    # get recipes from edamam specifically 
    # TODO: understand search query parameters to make a get request
    # there are alot
    # issue #7 Github    
    def requestEdamam():
        pass
    
    
