def list_in_list(l):
    list_total = 0
    for i in l:
        if type(i) == list:
            list_total +=1
    return list_total
numbers = [1,2,3,[4,5],[6,7]]
print(list_in_list(numbers))