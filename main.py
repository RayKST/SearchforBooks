import requests
import json

book = input("Insert a book to be search by the api: ")

res = requests.get(f"http://openlibrary.org/search.json?q={book.replace(' ', '+').lower()}")

with open("api/response.json", "w") as data_file:
    res = json.dump(res.json(), data_file, indent=4)  #Save response at API folder