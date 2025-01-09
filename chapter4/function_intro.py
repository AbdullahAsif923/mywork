# firstname,lastname = input("Enter Your First And Last name with comma sepreated : ").split(",")
# def user_name(firstname,lastname):
#     return firstname + lastname
# print(f"Your Complete Name is {user_name(firstname,lastname)}")
# differance between return and print statememt
# def add_three_num(num1,num2,num3):
#     print(num1+num2+num3)
# add_three_num(5,5,5)
# function practice
# name = input("Enter Your Name : ")
# def last_character(name):
#     return name[-1]
# print(last_character(name))
# def fun_odd_even(number):
#     if number%2 == 0:
#         return "even"
#     else:
#         return 'odd'
# print(fun_odd_even(10))
# def fun_odd_even(number):
#     if number%2 == 0:
#         return "even"
#     return 'odd'
# print(fun_odd_even(9))
# pure pythonic type of creating a  function
# def even_odd(num):
#     return num%2==0
# print(even_odd(11))
# def hi_func():
#     return "Hey How are you?"
# print(hi_func())
# def user_info(first_name,last_name,age = input("Enter Your First Name, Last Name And Age : ").split(",")):
def user_info(first_name=input("Enter Your First Name : ") , last_name=input('Enter Your Last Name : '), age=int(input("Enter Your Age : "))):
    print(f"My First Name is {first_name}")
    print(f"My Last Name is {last_name}")
    print(f"My Age is {age}")
user_info()