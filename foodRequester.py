# this file will access various Recipe APIs
import requests
import os
from dotenv import load_dotenv
import json

class foodRequester:
    def __init__(self) -> None:
        # get all the api keys
        load_dotenv()
        # for noew make separate class attributes per api
        self.edamamKey = os.getenv('EDAMAM_SEARCH_API_KEY') 
        self.edamamID = os.getenv('EDAMAM_SEARCH_APP_ID')
        