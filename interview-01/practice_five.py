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


# usd -> target = amount * rate
# source -> usd = amount / rate
# source -> rate = amount * target / source


with open("fallback_rate.json") as f:
    data = json.load(f)


def convert(amount, source, target):
    try:
        rates = fetch_exchange_rates()

    except Exception:
        rates = data
    
    if source not in rates or target not in rates:
        raise Exception("Currency not found.")
    elif source == "USD" and target != "USD":
        ans = amount * rates[target]
    elif source != "USD" and target == "USD":
        ans = amount / rates[source]
    else:
        ans = amount * rates[target] / rates[source]
        

    ans = round(ans, 2)
    print(ans)
    return ans

convert(300, "EUR", "USD")

name = "bob"

name = name.upper()
print(name)



