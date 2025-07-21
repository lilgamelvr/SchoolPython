counter = 0
total = 0

while True:
    try:
        gallons = float(input("Enter the gallons used, (-1 to end): "))
        if gallons == -1:
            overall_average = total / counter
            print(f"The overall average miles/gallon was {overall_average}")
            exit()

        miles = float(input("Enter the miles driven: "))
        tank_average = miles / gallons
        print(f"The miles per gallon for this tank was {tank_average}")

        total += tank_average
        counter += 1

    except ValueError:
        print("Invalid input. Please enter a valid number.")
