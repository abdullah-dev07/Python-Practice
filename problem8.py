def fibonacci_generator(n):
    a,b = 0,1
    yield a
    yield b
    while b <= n:
        sum = a + b
        yield sum
        a = b
        b = sum


fib = fibonacci_generator(5)

for n in fib:
    print(n)

