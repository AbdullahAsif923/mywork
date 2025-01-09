def is_palidrome(user_name):
    return user_name == user_name[::-1]
name = input("Enter Your Name : ")
print(is_palidrome(name))