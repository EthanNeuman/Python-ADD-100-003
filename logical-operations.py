num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

print("Both numbers are positive: ", num1 > 0 and num2 > 0)
print("Both numbers are multiples of 3: ", num1 % 3 == 0 and num2 % 3 == 0)

print("Either number is greater than 10?: ", num1 > 10 or num2 > 10)
print("Either number is divisible by 5?: ", num1 % 5 == 0 or num2 % 5 == 0)

print("num1 is not greater than num2: ", not (num1 > num2))
print("num2 is not divisible by 2: ", not (num2 % 2 == 0))
