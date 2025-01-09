# def number_size(num1,num2,num3):
#     if int(num1) > int(num2) and int(num1) > int(num3):
#         return f"{num1} is greater "
#     elif int(num2) > int(num1) and int(num2) > int(num3):
#         return f"{num2} is greater "
#     return f"{num3} is greater "
# first_number,second_number,third_number = input("Enter Three Number With Comma Sepreated : ").split(",")
# print(number_size(first_number,second_number,third_number))
# with help of inside function
def greater(a,b):
    if a > b:
        return a
    return b
def greatest(a,b,c):
    return greater(greater(a,b),c)
print(greatest(10,50,30))