# this file will access various APIs
from logging import currentframe
import os
from dotenv import load_dotenv
from Requester import Requester

class foodRequester():
    def __init__(self) -> None:
        # get all the api keys
        load_dotenv()
        self.rapidAPIKey = os.getenv('RAPID_API_KEY')
        # dictionaries containing api urls and host urls from rapid api 
        self.apiURLs = {
            # each key maps to a  list with the first idex containing the api url and
            # the second containing the host url
            "edamam": [os.getenv('EDAMAM_URL'), os.getenv('EDAMAM_HOST_URL')],
            # ... More to add
        }

        self.requester = Requester()

        # state maintining variables
        # selected recipe
        # set this when discord bot calls the api requester
        self.currentRecipe = None 
    

    def getAPIURLs(self, key: str):
        """
        Get the host url and the api url from the class for making requests through rapid api
        Make sure the api and host urls have the same keys for the same api
        """
        hostURL = self.apiURLs[key][1]
        apiURL = self.apiURLs[key][0]
        return hostURL, apiURL

    # get recipes from edamam specifically 
    # TODO: understand search query parameters to make a get request
    # there are alot
    # issue #7 Github    
    # this is called by discord bot to set a current recipe
    def requestEdamam(self, queryOrId: str, startIndex=0, endIndex=20, 
                      numIngreds=0, dietLabel='', healthLabel='', 
                      cuisineType='', mealType='', dishType='', 
                      calories=0, time=30, excluded=''):
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
        params = {
            "q":queryOrId,
            "from": startIndex,
            "to": endIndex,
            "ingr": numIngreds,
            # ... below will be the other params for when we know how to use each
        }

        edamamHURL, edamamAURL = self.getAPIURLs("edamam")
        response = self.requester.makeGETRequest(edamamAURL, edamamHURL, params=params)
        print(response['hits'])
        # parse the response for a select amount of information
        # what information do i need:
        recipe = response['hits'][0]['recipe']
        self.currentRecipe = {
            "name": recipe['label'],
            "ingredients": recipe['ingredients'],
            "source": recipe['url']
        }
    
    # this is what the discord bot calls to get stuff
    def getCurrentRecipe(self):
        return self.currentRecipe
    




if __name__ == "__main__":
    fr = foodRequester()
    fr.requestEdamam("ham", 10, 11, 6)