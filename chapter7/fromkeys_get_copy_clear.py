# fromkeys 
d = dict.fromkeys(['name','age','education'],'unknown')
print(d)

# get method (useful)
my_info = {
    "name" : 'Abdullah',
    'age' : 17,
    'age' : 20
}
print(my_info.get("names" , 'Not Found ! '))
# print(my_info)

# clear method 
d.clear()
print(d)

# copy method
d1 = d.copy()
print(d1)
# print( d1 == d)