def map_by_name(dict_list):
    # your code here
    return [ele['name'] for ele in dict_list]

pets = [
  {"type": "dog", "name": "Rolo"},
  {"type": "cat", "name": "Sunny"},
  {"type": "rat", "name": "Saki"},
  {"type": "dog", "name": "Finn"},
  {"type": "cat", "name": "Buffy"}
]

print(map_by_name(pets))

countries = [
 {"name": "Japan", "continent": "Asia"},
 {"name": "Hungary", "continent": "Europe"},
 {"name": "Kenya", "continent": "Africa"},
]

print(map_by_name(countries))