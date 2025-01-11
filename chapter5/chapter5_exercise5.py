def common_number(list1,list2):
    output = []
    for i in list2:
        if i in list1:
            output.append(i)
    return output
number1 = [1,2,3,4,5]
number2 = [1,2,3,4,5,6,7]
print(common_number(number1,number2))
numbers= [2,60,30]
print(min(numbers))
print(max(numbers))