import requests
from win10toast import ToastNotifier
import json
import time

def update():
    r = requests.get("https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true")
    data = r.json()
    text = f"Total Cases : {data['totalCases']} \nDeaths : {data['deaths']} \nRecovers : {data['recovered']} \nActive Cases: {data['activeCases']}"

    toast = ToastNotifier()
    toast.show_toast("Covid-19 Updates",text,duration=20)

        