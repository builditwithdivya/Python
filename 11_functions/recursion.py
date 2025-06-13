'''
Fibonacci sequence
0 1 1 2 3 5 8 13 21 34 ...
0 1 2 3 4 5 6 7 8 9 10

fib (0) = 0
fib (1) = 1
fib (2) = fib(1) + fib(0) = 1
fib (3) = fib(2) + fib(1) = 2
fib (n) = fib(n-1) + fib(n-2) for n > 1
'''


def fib(n):
    #Base case of recursion
    # If n is 0 or 1, return n
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    
print(fib(6))


'''
fib(6)
fib (5) + fib(4)
fib(5) + fib(3) + fib(2)
fib(5) + fib(3) + fib(1) + fib(0)
fib(5) + fib(3) + 1 + 0
fib(5) + fib(2) + fib(1) + 1 + 0
fib(5) + fib(2) + 1 + 1 + 0
fib(5) + fib(1) + fib(0) + 1 + 1 + 0
fib(5) + 1 + 1 + 1 + 1 + 1 + 0
fib(4) + fib(3) + 1 + 1 + 1 + 1 + 0
8 + 5
13 = fib(6)
'''
