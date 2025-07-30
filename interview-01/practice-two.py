example = {
  "USD": 1.0,
  "EUR": 0.91,
  "JPY": 141.2,
  "CAD": 1.33
}

import random
import json

def fetch_exchange_rates():
    if random.random() < 0.7:  # 70% chance of failure
        raise Exception("API failure")
    return {
        "USD": 1.0,
        "EUR": 0.91,
        "JPY": 141.2,
        "CAD": 1.33
    }


with open("fallback_rate.json", "r") as f:
    fallback_rates = json.load(f)

# fallback_calls = 0

def convert(amount, from_currency, to_currency):

    try:
        rates = fetch_exchange_rates()
    except Exception as e:
        if str(e) == "API failure":
            rates = fallback_rates
            # fallback_calls += 1

    if from_currency not in rates or to_currency not in rates:
        raise Exception("No currency found")

    if to_currency == "USD":
        res =  amount / rates[from_currency]
    
    if from_currency == "USD":
        res = amount * rates[to_currency]
    
    if from_currency != "USD" and to_currency != "USD":
        res = (amount / rates[from_currency]) * rates[to_currency]
    
    res = round(res, 2)
    print(res)

    return res
    # return res, fallback_calls
    
