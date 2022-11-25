import pandas as pd
import requests

api_key = "A1shZUUaf4D_WTo2UQCmZ4Ut5yezRhWnSDdJTY3qz3w"


def locals(locality):
    qq = locality
    x = f"https://geocode.search.hereapi.com/v1/geocode?q={qq}&apiKey={api_key}"
    results = requests.get(x)
    d = results.json()
    lat = d["items"][0]["position"]["lat"]
    lng = d["items"][0]["position"]["lng"]
    return lat, lng
