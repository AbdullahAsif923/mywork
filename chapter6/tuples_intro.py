# tuples are also data structure as lists
# tuples can store any data type
# most important tuples are immutable, once tuple are created you can't update
# data inside tuples
example = ("Abdullah","Asif",17)
# no appand, no insert , no pop , no remove
# we use tuples when we don't need to change or update data
Days = ("Monday",'Tuesday', 'wednesday')
# tuples are faster than lists
# methods which we use in tuples are 
# count, Index
# len function
# slicing
print(example.count("Abdullah"))
print(example.index(17))
print(len(example))
print(example[::-1])