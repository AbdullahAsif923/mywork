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
def fun_odd_even(number):
    if number%2 == 0:
        return "even"
    return 'odd'
print(fun_odd_even(9))