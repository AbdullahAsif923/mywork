user_info = {
    "name" : input("Enter Your Name : "),
    "Age" : int(input("Enter Your Age")),
    "fav_food" : list(input("Enter Your Favourite Food Name : ").split(",")),
    "fav_sport" : list(input("Enter Your Favourite Sport Name : ").split(","))
}
for key, values in user_info.items():
    print(f"{key} : {values}")
