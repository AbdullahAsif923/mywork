import random
# print statement
# print("My Name Is Abdullah Asif")
# print(17)
# Escape Sequences
# print("My Name Is \"Abdullah Asif\"  \n& My Age Is \"17\".")
# comments in pyhton
# if we want to create a comment in python for this use hash(#) symbol at the start of the line  
# Escape Sequence As normal text
# print("My Name Is \\'Abdullah\\' ")
# print(r"My Name is \"Abdullah Asif\" \t ") this is an raw string which print output as it written in print statment
# exercise 01
# print("This is \\\\ backslash")
# print("this is /\\/\\/\\/\\/\\ mountain")
# print("he is \t awsome")
# print(" \\\" \\n  \\t \\\'")
# print("\U0001F600") this is an example for printing emoji
# print(5+9) for addition
# print(5-9) for subtraction
# print(5*9) for multiplacition
# print(5/9) for divsion
# print(5//9) for integer divsion without point
# print(5%9) for finding reamining in divsion
# print(5**9) for taking power of a number
# variable in pyhton 
# name,age = "Abdullah", str(17)
# print("My name is " + name + " & My Age is " + age)
# user input 
# print(input("Enter Your Name")) input fuction is used for taking input from user 
# int() function converts a string to integer and str() function is used to converts intger to string
# two or more input in one line 
# name , age , date_of_birth = input("Please Enter Your Name, Age and Date of Birth with comma sepreated: ").split(",")
# print("My name is " + name + " & My Age Is " + age + " & Date Of Birth is " + date_of_birth)
# string formatting 
# There Are two types of string formating in python3
# print("My name is " + name + " & My Age Is " + age + " & Date Of Birth is " + date_of_birth) # number one this type
# print(f"My name is {name} and age is {age} and date of birth is {date_of_birth}") # Second Type Of String Formating
# exsersie
# num1,num2,num3 = input("Please Enter Three Number with comma Sepreated : ").split(",")
# average = int(num1) + int(num2) + int(num3)
# print(f"Average of three number is {average/3}")
# string indexing & string slicing & String Step Argument
# name = 'Abdullah Asif'
# print(name[7]) string indexing
# print(name[0:8]) string slicing
# print(name[0:8:2]) string Step Argument
# exersise
# name = input("Please Enter Your Name : ")
# print(f"Your name is {name} and in reverse your name is {name[::]}")
# exersise
# name, single_character = input("Enter Your Name And A single character with comma sepreated : ").split(",")
# print(f"Your Name Lenth is {len(name)} and {name.lower().count(single_character.strip())}")
# find and replace method
# name = "Abdullah Asif"
# print("new name is " + str(name.replace("Abdullah","Ahsan")) + " and Asif is indexed at " + str(name.find("Asif")) + " in old name")
# name, = "Abdullah", 
# print(name.center(12,"*"))
# age = int(input("enter your age : "))
# if age >= 18:
#     print("You can play the game")
# else: 
#     print("You Cannot Play The Game")
# exercise
# winning_number = random.randint(0,10)
# user_number = int(input("Please Enter a number : "))
# if user_number == winning_number:
#     print("You Win!!!")
# else:
#     if user_number > winning_number:
#         print("Too High!")
#     else:
#         print("Too Low!")
# name,age = "Abdullah", 17
# if name == "Abdullah" and age == 17:
#     print(f"You're wlcome {name} Asif")
# else:
#     print("You are not a our user.")
# exercise
# name_start , age = input("Enter Your Name starting alphabat and age : ").split(",")
# if (name_start == 'a' or name_start == 'A') and int(age) >= 10:
#     print("you can watch coco movie.")
# else:
#     print("Sorry! You Cannot Watch Coco movie.")
# name = input("Enter Your Name : ")
# if name:
#     print(name)
# else:
#     print("You Not Enter Your Name")
# number,total,user_required = 1,0, int(input("Enter A number : "))
# while number <= user_required:
#     total += number
#     number += 1
# print(total)
# exercise
# number,i,total = input("Please Enter A number conataining more than one character : "),0,0
# while i < len(number):
#     total = total + int(number[i])
#     i += 1
# print(total)
# exercise
# user_name,i,remove_irration = input("Enter Your Name : "),0,""
# while i < len(user_name):
#     if user_name[i] not in remove_irration:
#         remove_irration = remove_irration + user_name[i]
#         print(f"{user_name[i]} : {user_name.lower().count(user_name[i])}")
#     i += 1
# for number in range(0,11):
#     print(f"Hello Abdullah {number}")