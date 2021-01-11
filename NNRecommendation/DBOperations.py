import json
import pandas as pd

foods = dict()
with open('db.json', 'r') as f:
    foods = json.load(f)
    foods = foods['foods']

def getFoodsFromFoodIDs(food_ids):
    food_names = []
    for food_id in food_ids:
        food_names.append(next(filter(lambda food: food['id'] == food_id, foods))['foodName'])
    
    return food_names

def getEatenFoodsOfUser(uid):
    df = pd.read_csv('new_ratings.csv')
    food_list = list(df[df.userId == uid]['foodId'])
    return getFoodsFromFoodIDs(food_list)