import requests
import json

url = "https://www.latin-is-simple.com/api/vocabulary/search"

while True:
    query = input("Word >")
    type = input("Type noun, verb, adjective, adverb, pronoun, None for all\n >") #noun, verb, adjective, adverb

    resp = requests.get(url, params={"query": query})
    js = resp.json()

    for i in js:
        if type != '':
            if i["intern_type"] == type:
                print(i["short_name"])
                defi = i["translations_unstructured"]
                print(defi["en"])
                print("\n")
                if input("(c to exit)...").lower() == "c":
                    break 
        else:
            print(i["short_name"])
            print(i["intern_type"])
            defi = i["translations_unstructured"]
            print(defi["en"])
            print("\n")
            if input("(c to exit)...").lower() == "c":
                break