def product(*args):
    if not args:
        return 1
    result = 1
    for num in args:
        if not isinstance(num, int):
            raise ValueError("All arguments must be integers")
        result *= num
    return result


# Test cases
test_cases = [
    (2, 4, 6),
    (3, 6, 9),
    (5, 10, 15, 20),
    (10, 20, 30, 40, 50),
    (),
]

for args in test_cases:
    try:
        result = product(*args)
        print(f"The product of {args} is {result}")
    except ValueError as e:
        print(f"Error: {e}")
