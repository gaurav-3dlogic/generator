def fibonacci(n):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    # Generate Fibonacci numbers up to n
    while a <= n:
        yield a
        a, b = b, a + b

# Generate the Fibonacci series up to 100
for num in fibonacci(10):
    print(num)


