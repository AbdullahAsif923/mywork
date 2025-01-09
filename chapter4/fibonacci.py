def fibonacci_seq(number):
    a = 0
    b = 1
    if number == 1:
        print(a)
    elif number == 2:
        print(a, b)
    else:
        print(a, b,end=" ")
        for i in range(number-2):
            c = a + b
            a = b
            b = c
            print(b ,end=" " )
num = int(input("Enter a number for fiboacci series : "))
fibonacci_seq(num)
