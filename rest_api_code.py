import json
import os
import requests

apiQuery = 'https://api.openbrewerydb.org/v1/breweries'
locationSearchIndicator = False
typeSearchIndicator = False
queryNum = 0
repeat = True

def printQueryMenu():
    print("\n\nPlease enter the number of your choice:")
    print("\n 1. Search by location")
    print("\n 2. Search by brewery type")

def addFirstChar():
    global apiQuery
    if queryNum == 0:
        apiQuery += '?'
    else:
        apiQuery += '&'

def searchLocation():
    global apiQuery, locationSearchIndicator, queryNum
    if locationSearchIndicator == False:
        print("\nPlease enter the number of your choice:")
        print(" 1. Search by state")
        print(" 2. Search by city")
        print(" 3. Search by postal code")

        locationMenuInput = int(input("> "))
        addFirstChar()
        if locationMenuInput == 1:
            apiQuery += 'by_state='
        elif locationMenuInput == 2:
            apiQuery += 'by_city='
        elif locationMenuInput == 3:
            apiQuery += 'by_postal='

        print("\nPlease enter your desired search location.")
        locationInput = input("> ")

        apiQuery += locationInput.replace(" ", "_")
        locationSearchIndicator = True
        queryNum += 1
    else:
        print("**ERROR: Already added a location to search**")

def searchType():
    global apiQuery, typeSearchIndicator, queryNum
    if typeSearchIndicator == False:
        print("Please enter the number of the brewery type you wish to search for:")
        print("For multiple types, enter each number with one space between, in any order (ex. 1 4 2)")
        print(" 1. Micro")
        print(" 2. Nano")
        print(" 3. Regional")
        print(" 4. Brewpub")
        print(" 5. Large")

        typeInput = int(input("> "))
        addFirstChar()
        apiQuery += 'by_type='
        if typeInput == 1:
            apiQuery += 'micro'
        elif typeInput == 2:
            apiQuery += 'nano'
        elif typeInput == 3:
            apiQuery += 'regional'  
        elif typeInput == 4:
            apiQuery += 'brewpub'
        elif typeInput == 5:
            apiQuery += 'large'
        typeSearchIndicator = True
        queryNum += 1
    else:
        print("**ERROR: Already added a type to search for**")

def queryInputSwitch(input):
    if input == 1:
        searchLocation()
    elif input == 2:
        searchType()

def getNumResults():
    global apiQuery
    print("How many results do you want?")
    numInput = input("> ")
    addFirstChar()
    apiQuery += f'per_page={numInput}'

def setQueryString():
    global repeat
    while repeat == True:
        printQueryMenu()
        queryInput = int(input("> "))
        queryInputSwitch(queryInput)

        print("Add another parameter?  Y/N")
        repeatInput = input("> ")
        if repeatInput.lower() in {'n', 'no'}:
            repeat = False

    getNumResults()

def printResults(json_data):
    print(f"{'Brewery':<40}{'City':<50}{'Type':<15}")
    print('-' * 80)

    for brewery in json_data:
        brewery_name = brewery.get("name", "N/A")
        city = brewery.get("city", "N/A")
        state = brewery.get("state", "N/A")
        location = f"{city}, {state}"
        brewery_type = brewery.get("brewery_type", "N/A").capitalize()

        print(f"{brewery_name:<40}{location:<50}{brewery_type:<15}")

setQueryString()
response = requests.get(apiQuery)
# Encodes response into a python json dictionary 
json_data = response.json()
print(f"API Query: {apiQuery}")
printResults(json_data)