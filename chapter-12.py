def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

choice = input("Choose an operation - 'factorial' or 'fibonacci': ").strip().lower()

if choice == 'factorial':
    number = int(input("Enter a number to calculate its factorial: "))
    print(f"The factorial of {number} is {factorial(number)}")
elif choice == 'fibonacci':
    number = int(input("Enter a number to calculate its Fibonacci sequence: "))
    print(f"The {number}th Fibonacci number is {fibonacci(number)}")
else:
    print("Invalid choice!")