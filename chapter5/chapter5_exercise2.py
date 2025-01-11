def take_list(l):
    # l.reverse()
    # return l[::-1]
    revirse_list = []
    for i in range(len(l)):
        poppped_item = l.pop()
        revirse_list.append(poppped_item)
    return  revirse_list
list_items = [1,2,3,4]
print(take_list(list_items))