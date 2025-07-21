result = 1

try:
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Please enter a NON-negative integer.")
    else:
        for i in range(1, n + 1):
            result *= i
        print(f"The factorial of Number {n} is {result}")
except ValueError:
    print("Invalid input. Please enter a valid non-negative integer.")
