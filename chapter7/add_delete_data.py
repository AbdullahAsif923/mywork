# add and deleta data
user_info = {
    "name" : "Abdullah",
    "Age" : 17,
    "fav_food" : ["Biryani","Chiken Savarma"],
    "fav_sport" : ["Bdmintin","Cricket"]
}

# how to add data
user_info['fav_person'] = ["Hazrat Muhammad", "Hazrat Abu Bakr", "Hazrat Umar"]
print(user_info)

# pop method
popped_key = user_info.pop("fav_sport")
print(f"popped item is {popped_key}")
print(user_info)

# popitem method
print(user_info.popitem())

# update method

more_info = {"name" : "Abdullah Asif","state":"Punjab","Hobbies":['coding','eating','sleaping']}
user_info.update(more_info)
print(user_info)