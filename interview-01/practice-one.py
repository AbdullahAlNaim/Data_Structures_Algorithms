'''
partner - group by
click_id
timestamp
user_id
destination - group bye
'''

data = [
  {
    "partner": "Google",
    "click_id": "abc123",
    "timestamp": "2024-07-10T12:01:22Z",
    "user_id": "u1",
    "destination": "Boston"
  },
  {
    "partner": "Facebook",
    "click_id": "def456",
    "timestamp": "2024-07-10T12:05:11Z",
    "user_id": "u2",
    "destination": "New York"
  },
  {
    "partner": "Google",
    "click_id": "ghi789",
    "timestamp": "2024-07-10T12:09:45Z",
    "user_id": "u3",
    "destination": "Boston"
  }
]

example_answer = {
  "Google": {
    "Boston": 2
  },
  "Facebook": {
    "New York": 1
  }
}


# print(data[0]['partner'])

# print("Google" in example_answer)

# print("Boston" in example_answer["Google"])

# answer = {}
# 
# obj = {
#     "partner": "Google",
#     "click_id": "abc123",
#     "timestamp": "2024-07-10T12:01:22Z",
#     "user_id": "u1",
#     "destination": "Boston"
#   }

# def traffic(data):
#     answer = {}
#     for i in range(len(data)):

#         partner = data[i]["partner"]
#         destination = data[i]["destination"]

#         if partner in answer:
            
#             if destination in answer[partner]:
#                 print("found")
#                 answer[partner][destination] += 1
#             else:
#                 answer[partner][destination] = 1
        
#         else: 
#             answer[partner] = {destination: 1}
        
    
#     return answer


def traffic(trips):
    results = {}

    for trip in trips:
        if "partner" not in trip or "destination" not in trip:
            continue

        partner = trip["partner"]
        destination = trip["destination"]

        if partner not in results:
            results[partner] = {}

        if destination not in results[partner]:
            results[partner][destination] = 0

        results[partner][destination] += 1

    return results

        




