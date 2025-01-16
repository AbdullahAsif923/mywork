### About Conditionals and Loops

# Q - Write a Python program to check if a number is even or odd.
# A - Program
number = 8
if number%2==0:
    print("Number is Even.")
else:
    print("Number is Odd")

# Q - What is the difference between a for loop and a while loop?
# A - There is no major differnce between them except their Syntex and while loop manuly use when we now the total number of iterations but foor loop widly use on list,tuple,string or range.  

# Q - Write a program that prints numbers from 1 to 10 using a loop.
# A - Using While Loop Program
num = 1
while num <=10:
    print(num)
    num += 1
# Using For Loop
for i in range(1,11):
    print(i)

# Q - What will happen if the condition in a while loop never becomes False?
# A - it will start a infinate loop


