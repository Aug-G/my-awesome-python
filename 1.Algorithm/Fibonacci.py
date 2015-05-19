#coding:utf-8
# Fibonacci 数列的Python实现

#lambda 实现
fib = lambda n: 1 if n < 2 else fib(n - 1) + fib(n - 2)


# decorator 经典实现
def memo(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

def fib2(i):
    if i < 2:
        return 1
    return fib2(i - 1) + fib(i - 2)


if __name__ == "__main__":
    print fib(10)
    print fib2(10)
