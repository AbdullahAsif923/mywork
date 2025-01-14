# in keyword and iterations in dictionaries
user_info = {
    "name" : "Abdullah",
    "Age" : 17,
    "fav_food" : ["Biryani","Chiken Savarma"],
    "fav_sport" : ["Bdmintin","Cricket"]
}

# Chick if key exist in dictionary
if 'names' in user_info:
    print("present")
else: 
    print("not present")

# Chick if value exist in dictionary
if 17 in user_info.values():
    print("present")
else:
    print("not present")

# loops in dictionaries
for i in user_info.values():
    print(i)

# values method in dictionaries
user_info_values = user_info.values()
print(user_info_values)
print(type(user_info_values))

# keys method in dictionaries
user_info_keys = user_info.keys()
print(user_info_keys)
print(type(user_info_keys))

for i in user_info:
    print(user_info[i])

# items method in dictionaries
user_info_items = user_info.items()
print(user_info_items)
print(type(user_info_items))

for key,value in user_info.items():
    print(f"key is {key} and value is {value}")
