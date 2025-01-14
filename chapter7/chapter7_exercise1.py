def cube(n):
    d = {}
    for i in range(1,n +1):
        d[i] = i**3
    return d
print(cube(5))

# def char_counter(c):
#     count = {}
#     for i in c:
#         count[i] = c.count(i)
#     return count
# print(char_counter('Abdullah'))