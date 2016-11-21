def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


# fib(2000)
f = fib
f(100)

# 没有return 语句的函数会返回一个 None
print(fib(0))
