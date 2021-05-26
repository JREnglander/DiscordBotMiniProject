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
    def requestEdamam(queryOrId, startIndex, endIndex, 
                      numIngreds, dietLabel, healthLabel, 
                      cuisineType, mealType, dishType, 
                      calories, time, excluded):
        """
        queryOrId: the search term to define the request (required)
        all of other parameters are optional:
        startIndex and endIndex: parameters to define where to pull recipes (prevents pulling entire database each time)
        numIngreds: number of ingredients to make recipe
        the following params are enums with string labels defined on edamam docs
        dietLabel, healthLabel, cuisineType, mealType, dishType
        The following params have a range type which comes in three forms:
        MIN+, MIN-MAX, or MAX  
        calories
        time
        excluded: param that takes strings of ingredients to exclude from search
        """

        # TODO: handle each parameter 
        # TODO: Required parameters: queryOdrId, startIndex, endIndex
        # TODO: Handle list/enum Params: label, type params
        # TODO: Handle Range Params
        # TODO: excluded should be a list and you generate a string with the list 
        # TODO: generate final URL 
        # TODO: make request

        # TODO: create config file for params to keep constant in requests

        pass
    
    
