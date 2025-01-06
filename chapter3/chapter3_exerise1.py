import random
winning_number = random.randint(0,20)
user_guess_number = int(input("Guess a number b/w 0 to 20 : "))
if user_guess_number == winning_number:
    print("You Win!!!")
else:
    if user_guess_number < winning_number:
        print("Two Low")
    else:
        print("Two High") 