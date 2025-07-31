raw_feed = [
  {
    "from_city": "  BOSTON  ",
    "to_city": "new york",
    "trip_date": "07/29/2025",
    "carrier": "MegaBus"
  },
  {
    "from_city": "los angeles",
    "to_city": "san francisco",
    "trip_date": "2025-07-30",
    "carrier": "mega_bus"
  }
]

[
  {
    "origin": "Boston",
    "destination": "New York",
    "date": "2025-07-29",
    "carrier": "MegaBus"
  },
  {
    "origin": "Los Angeles",
    "destination": "San Francisco",
    "date": "2025-07-30",
    "carrier": "MegaBus"
  }
]

from datetime import datetime

# origin
# destination
# date
# carrier

def normalize_trips(feeds):
    results = []

    for feed in feeds:
        from_city = feed.get("from_city")
        to_city = feed.get("to_city")
        trip_date = feed.get("trip_date")
        carrier = feed.get("carrier")

        if type(from_city) != str:
            from_city = "Unknown"
        else:
            from_city = from_city.strip()
            from_city = from_city.title()

        if type(to_city) != str:
            to_city = "Unknown"
        else:
            to_city = to_city.strip()
            to_city = to_city.title()

        try:
            format = "%Y-%m-d"
            date = trip_date
            cleaned_date = datetime.strptime(date, format)
        except:
            cleaned_date = "Unknown"
        
        if type(carrier) != str:
            carrier = "Unknown"
        else:
            carrier = carrier.strip()
            carrier = carrier.title()

        results.append({
            "origin": from_city,
            "destination": to_city,
            "date": cleaned_date,
            "carrier": carrier
        })
            
    return results

normalize_trips(raw_feed)
