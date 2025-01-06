user_name,single_char = input("Please Enter Your Name & Single Character between your name : ").split(",")
print(f"Your name length is {len(user_name.strip())} and the character you are entered are used in {user_name.strip().lower().count(single_char.strip().lower())} times.")

