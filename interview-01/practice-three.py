import json

with open("marketing_data.json", "r") as f:
    data =  json.load(f)
    


def traffic(trips):
    results = {}

    for trip in trips:
        
        partner = trip.get('partner')
        destination = trip.get('destination')
        user = trip.get('user_id')
        
        if partner not in results:
            results[partner] = {}
            

        if destination not in results[partner]:
            results[partner][destination] = set()
            
        
        results[partner][destination].add(user)

    for partner in results:
        for destination in results[partner]:
            results[partner][destination] = len(results[partner][destination])
    
    return results

answer = traffic(data)
print(answer)