def filter_odd_even(l):
    even_list = []
    odd_list = []
    final_list = [even_list,odd_list]
    for i in l:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return final_list
ending_number = int(input("Enter a List ending number : "))
input_list = list(range(1,ending_number))
print(filter_odd_even(input_list))