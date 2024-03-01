def fibonacci(limit):
    """Generate Fibonacci numbers up to the given limit."""
    num1, num2 = 0, 1
    while num1 <= limit:
        yield num1
        num1, num2 = num2, num1 + num2

#numbers upto 100
fibs = fibonacci(100)

#lazy evaluation
for fib in fibs:
    print(fib)
