### Functions

# Q - Write a Python function that takes two numbers as input and returns their sum.
# A - Program 
num1,num2 = input("Enter Two Numbers With Comma Seperated : ").split(",")
def total(n1,n2):
    return int(n1) + int(n2)
print(f"The number one is {num1} and two is {num2} and there sum was {total(num1,num2)}")

# What is the purpose of the return keyword in a function?

# What happens if you call a function without providing all the required arguments?
# Explain the difference between a parameter and an argument in a function.