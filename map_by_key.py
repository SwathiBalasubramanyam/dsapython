def map_by_key(dict_list, key):
    # your code here

    return [ele[key] for ele in dict_list]

locations = [
  {"city": "New York City", "state": "New York", "coast": "East"},
  {"city": "San Francisco", "state": "California", "coast": "West"},
  {"city": "Portland", "state": "Oregon", "coast": "West"},
]

print(map_by_key(locations, "state")) #["New York", "California", "Oregon"]
print(map_by_key(locations, "city")) #["New York City", "San Francisco", "Portland"]