# get requests module
import requests
import os
from dotenv import load_dotenv
import json

class weatherRequester:
    def __init__(self) -> None:
        # get the weather api url
        load_dotenv()
        self.weatherURL = os.getenv('WEATHER_URL')
        self.apiKey = os.getenv('WEATHER_API_KEY')
    
    
    def requestWeather(self,city='',state='',country=''):
        """
        Makes a request to the openweathermap api for current weather
        :param city [str] the city to get weather for
        :param state [str] optional: the state to differentiate between cities with the same name
        :param country [str] optional: the country to differentiate between same name cities in different countries
        returns the temperture humidity and weather description of the given location
        """
        # make request URL:
        weatherRequestURL = self.weatherURL + 'q=' + city + state + country + '&apikey=' + self.apiKey
        request = requests.get(weatherRequestURL)
        
        # parse the response into python dict
        parsedRequest = json.loads(request.text)
        print(parsedRequest)
        responseCode = parsedRequest['cod']

        if responseCode == 200:
            # temperature
            tempAndHum = parsedRequest['main']
            temp = self.convertTempKToF(tempAndHum['temp'])
            # humidity
            hum = tempAndHum['humidity']
            # weather description
            weatherdata = parsedRequest['weather'][0]
            weatherDescription = weatherdata['description']
            
            return [temp, hum, weatherDescription]
        elif responseCode == 404:
            return parsedRequest['message']
        else:
            return 'API server error has occured'
    
    def convertTempKToF(self, kelvins):
        celsius = kelvins - 273.15
        farenheit = (celsius * (9/5)) + 32
        return farenheit

if __name__ == "__main__":
    # TESTING 
    wr = weatherRequester()
    city = 'Falls Church'
    # state = 'US-DC'
    # country = 'US'
    wr.requestWeather(city)
    
