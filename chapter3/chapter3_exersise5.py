name = input("Enter Your name :")
i = 0
tem_variable = ""
while 1 < len(name):
    if name[i] not in tem_variable:
        tem_variable += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1

