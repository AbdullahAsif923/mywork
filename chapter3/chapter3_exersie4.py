user_number = input("Enter A Number Containing more then one digit.")
print(f"length of the number that you enter is {len(user_number)}")
sum,i = 0,0
while i < len(user_number):
    sum = sum + int(user_number[i])
    i +=1
print(sum)