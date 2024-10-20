# import dependencies
from dotenv import load_dotenv
from pprint import pprint
import requests
import os

# loads the API key stored in .env
load_dotenv()

# Runs with default value of city 'Indore' if no parameter is provided
def get_current_weather(city="Indore"):
    
    request_url=f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    
    weather_data = requests.get(request_url).json()
    
    return weather_data

if __name__ == "__main__":
    print('\n*** Get Weather Conditions ***\n')
    
    city = input("Please enter a city name: ")
    
    # Check for empty string or string with only spaces
    
    if not bool(city.strip()):
        city = "Indore"
        
    weather_data = get_current_weather(city)
    
    print("\n")
    pprint(weather_data)