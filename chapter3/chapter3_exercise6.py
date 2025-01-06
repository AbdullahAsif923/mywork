import random
winning_number =  random.randint(1,25)
for loop_times in range(0,11):
    user_number = int(input("Enter A number between 1 to 25 : "))
    if user_number == winning_number:
        print(f"you win, and you guessed this number in {loop_times} times")
        break
    elif user_number < winning_number:
        print("too low!")
    else:
        print("too high!")
    continue
