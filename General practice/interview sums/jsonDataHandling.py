import json

with open('library_inventory.json', mode='r') as file: # Open the JSON file in read mode ('r')
    data = json.load(file) # Load the JSON data into a Python dictionary
    for book in data['books']: # Loop through each book in the 'books' list
        print(f"Title: {book['title']}, Author: {book['author']}, Available: {book['available']}")