# loop in tuples
mixed = (1,2,3,"Abdullah","Asif",17.0)
for i in mixed:
    print(i)
# tuple with one element
number = (1) # this sytex is wrong python consider it as int
number = (1,) # this is a tuple
name = ('Abdullah',)
print(type(number)) 
print(type(name)) 
# tuple without parenthesis
my_feriends = 'Akmal','Fahad','Sufyan'
print(type(my_feriends)) 
# tuple unpacking
my_feriends1,my_feriends2,my_feriends3 = (my_feriends)
print(my_feriends1)
# list in side tuple
pakistan_cities = ('Lahore',['Karachi','Islamabad'])
print(pakistan_cities[1].pop())
print(pakistan_cities)
# some fuction that we can use with tuple
# like min, max, sum
numbers = (1,5,9,14,21)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
# fuctioning returing two values
def add_multiply(num1,num2):
    add = num1 + num2
    multiply = num1 * num2
    return add, multiply
add , multiply = add_multiply(2,3)
print(add,multiply)
