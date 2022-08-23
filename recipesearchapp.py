#step 2 code block

import requests
from pprint import pprint

ingredient = input("What ingredient would you like to search for?")
url = 'https://api.edamam.com/api/recipes/v2?type=public&q={}&app_id=eb06afb3&app_key=%20dde4228b5d56d0e346c526b1787efb23'.format(ingredient)
print(url)
response = requests.get(url)

print(response)
recipes = response.json()

pprint(recipes)


#steps 3 and 4 code blocks

#this function will let the user return recipes with an ingredient of their choice using the Recipe Search API
def get_recipes_by_ingredient(ingredient):
    #this next line creates the url for the search
    url = 'https://api.edamam.com/api/recipes/v2?type=public&q={}&app_id=eb06afb3&app_key=%20dde4228b5d56d0e346c526b1787efb23'.format(
        ingredient)
    #This does a web get request using the url
    response = requests.get(url)
    #this prints the status code (e.g. 404, 400)
    print(response)
    #The next line is the data the API creates
    recipes = response.json()
    #This returns all the recipes
    return recipes

#This takes the input from the user
ingredient = input("What ingredient would you like to search for?")

#This calls the function to return the recipes and stores it in the recipe_list variable
recipe_list = get_recipes_by_ingredient(ingredient)
pprint(recipe_list)