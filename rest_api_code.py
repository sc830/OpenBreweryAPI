import json
import os
import requests
# Comment out the next two lines if you are storing an API key in a .env file
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())  

# What is the base (sometimes called end-point) URL for the queries?
# Example: BASE_URL_FOR_APIS = 'https://api.themoviedb.org/3/trending/movie/week?'
BASE_URL_FOR_APIS = 'https://api.openbrewerydb.org/v1/breweries/'
TEXAS_BREWERIES_QUERY = '?by_state=texas'
MICRO_BREWERY_QUERY = '&by_type=micro'
PER_PAGE_QUERY = '&per_page=3'

TEXAS_MICROBREWERIES_URL = BASE_URL_FOR_APIS + TEXAS_BREWERIES_QUERY + MICRO_BREWERY_QUERY + PER_PAGE_QUERY

response = requests.get(
    TEXAS_MICROBREWERIES_URL,
     params={
         # The following are examples and should be replaced with your params.
        'key1': 'value1',
        'key2': 'value2'
     }
)

# Encodes response into a python json dictionary 
json_data = response.json()

print(f"{'Brewery':<40}{'City':<25}{'Type':<15}")
print('-' * 80)


for brewery in json_data:
    brewery_name = brewery.get("name", "N/A")
    city = brewery.get("city", "N/A")
    brewery_type = brewery.get("brewery_type", "N/A").capitalize()

    print(f"{brewery_name:<40}{city:<25}{brewery_type:<15}")

# Convert json_data to a formatted pretty
# json string that is easy for humans to read.
#pretty_json_data = json.dumps(json_data, indent=4, sort_keys=True)
#print(pretty_json_data)
