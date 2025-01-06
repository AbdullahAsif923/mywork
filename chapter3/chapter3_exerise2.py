name,age = input("Enter Your Name And Age With Comma Seperated : ").split(",")
if (name[0] == 'a' or name[0] == 'A') and int(age) >= 10:
    print("You Can Watch Coco Movie.")
else:
    print("Sorry! you cannot watch coco movie.")