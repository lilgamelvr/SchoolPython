number = int(input("Enter number: "))
tempvari = number
reverse = 0
while number > 0:
    dig = number % 10
    reverse = reverse * 10 + dig
    number = number // 10
if tempvari == reverse:
    print("The number is a palindrome")
else:
    print("The number isn't a palindrome")
