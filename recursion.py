def fib(n):
    fibn = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1
    return fibn