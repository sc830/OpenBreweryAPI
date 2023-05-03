import json
import os
import requests
# Comment out the next two lines if you are storing an API key in a .env file
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())  

# What is the base (sometimes called end-point) URL for the queries?
# Example: BASE_URL_FOR_APIS = 'https://api.themoviedb.org/3/trending/movie/week?'
BASE_URL_FOR_APIS = ''

response = requests.get(
    BASE_URL_FOR_APIS,
     params={
         # The following are examples and should be replaced with your params.
        'key1': 'value1',
        'key2': 'value2'
     }
)

# Encodes response into a python json dictionary 
json_data = response.json()

# Convert json_data to a formatted pretty
# json string that is easy for humans to read.
pretty_json_data = json.dumps(json_data, indent=4, sort_keys=True)
print(pretty_json_data)
