def fib(n):
    a = 1
    b = 1
    c = a + b
    if n == 1:
        print(1)
    elif n == 2:
        print(1, 1)
    elif n > 2:
        print(1,1, end = " ")
        for item in range(2, n):
            c = a + b
            a = b
            b = c
            print(c, end = " ")

n = int(input("Input the length of Fibonacci sequence (n>=1): "))
