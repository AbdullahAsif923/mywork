def number_list(l):
    numbers = []
    for i in l:
        numbers.append(i**2)
    return numbers
number = list(range(1,11))
print(number_list(number))