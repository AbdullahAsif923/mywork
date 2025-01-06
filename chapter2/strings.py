# Strings are collections of characters inside single quotes or double quotes
# firstname = "Abdullah"
# lastname = "Asif\n"
# fullname = firstname + " " + lastname
# print(fullname *5)
# Bio = "He is beautiful and he is a good poet and cricter also."
# print(Bio.lower().replace("he is","they are", 1))
# first_is_position = Bio.find("and")
# print(Bio.find("and",first_is_position + 1))
# user_name = input("Enter Your Name : ")
# print(f"Your Name Lenth Is {len(user_name)} and {user_name.strip().center(len(user_name) + 8, '*')}")
# name = "Abdullah Asif"
# replaced_name = name.replace(name[1],"B",)
# print(replaced_name)
name,age = "Abdullah",17
name += " Asif"
age += 1
print(f"My Name Is {name} and age is {age}")