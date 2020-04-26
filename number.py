def factorial(n):   # return factorial value of n
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def fibonacci(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result