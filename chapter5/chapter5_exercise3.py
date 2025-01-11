def take_list(l):
    reverse_list = []
    for i in l:
        reverse_list.append(i[::-1])
        # reverse_list.append(first_index)
    return reverse_list
names = ["Abdullah","Asif","Ahsan"]
print(take_list(names))