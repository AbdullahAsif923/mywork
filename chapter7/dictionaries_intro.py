# dictionaries intro
# Q- Why we use dictionaries?
# A - Because of limitions of lists, list are not enough to represent real data

user_info = ["Abdullah", 17 , ["Baryine","Chicken Shawarma"],["badmintin","Cricket"]]
# this list conatin user name , user age, fav food & fav spports
# you can do this with the help of list but this is not a good way

# Q - what are dictionaries
# A - Unordered collection of data in key: value pair.

# how to craete dictionaries?
user = {'name' : 'Abdullah', 'age' : 17}
print(user)
print(type(user))

# second method of creating dictionaries
user1 = dict(name = "Akmal", age = 20)
print(user1)

# how to access data from dictionary
# NOTE - There is no indexing because  unordered collection of data
print(user1['name'])

# what type of data can store in dictionaries 
# anything string, integer, list, tuples
user_info = {
    'name' : "Abdullah",
    "age" : 17,
    "fav_food" : ["Baryine","Chicken Shawarma"],
    "fav_sport" : ["badmintin","Cricket"]
}
print(user_info["fav_sport"])

# dictionaries inside dictionaries
users = {
    "user1" : {
        'name' : "Abdullah",
        "age" : 17
    },
    "user2" : {
        'name' : "Akmal",
        "age" : 20
    }
}
print(users["user2"])

# how to add data to a empty dictionay
user_info2 = {}
user_info2['name'] = "Fahad"
print(user_info2)