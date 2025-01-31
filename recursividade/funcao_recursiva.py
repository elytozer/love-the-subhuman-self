# x = 6!
# 0+1+1+2
def fibonacci(n):
    result = 1
    for numero in range(1, n+1)
        result *= numero
    return result

def fibonacci_r(n):
    if n == 0 or n == 1:
        return 1
    return n * fibonacci_r(n - 1) 

def fibonacci_s(n):
    if n == 0:
        return n
    if n == 1:
        return n
    else:
        n * fibonacci_s(n - 1)