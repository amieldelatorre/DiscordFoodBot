import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()
RANDOM_FOOD_API = os.getenv('RANDOM_FOOD_API')
RANDOM_DRINK_API = os.getenv('RANDOM_DRINK_API')

# service functions for the bot 
class Service:
    @staticmethod
    def get_random_food():
        response = requests.get(RANDOM_FOOD_API)
        json_data = json.loads(response.text)
        return {'name':json_data['meals'][0]['strMeal'], 'image':json_data['meals'][0]['strMealThumb']}

    @staticmethod
    def get_random_drink():
        response = requests.get(RANDOM_DRINK_API)
        json_data = json.loads(response.text)
        return {'name': json_data['drinks'][0]['strDrink'], 'image':json_data['drinks'][0]['strDrinkThumb']}
