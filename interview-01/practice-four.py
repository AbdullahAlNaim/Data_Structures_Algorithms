import json
from datetime import datetime

with open("trips_data.json") as f:
    traffic_data = json.load(f)


def traffic(searches):
    results = {}

    for search in searches:
        partner = search.get("partner")
        origin = search.get("origin")
        destination = search.get("destination")
        date_searched = search.get("searched_at")

        date_format = "%Y-%m-%dT%H:%M:%SZ"
        full_date = datetime.strptime(date_searched, date_format)
        cleaned_date_searched = str(full_date.date())

        searched_trip = origin + '->' + destination

        if partner not in results:
            results[partner] = {}

        if cleaned_date_searched not in results[partner]:
            results[partner][cleaned_date_searched] = {}

        if searched_trip not in results[partner][cleaned_date_searched]:
            results[partner][cleaned_date_searched][searched_trip] = 0

        results[partner][cleaned_date_searched][searched_trip] += 1


    print(results)
    return results
        


traffic(traffic_data)
