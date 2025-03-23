# Returning a result from a Function
def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


# get user input for each one
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time in years: "))

# Calculate interest
interest = calculate_interest(principal, rate, time)

# the result
print(
    f"The simple interest for ${principal:,.2f} at {rate}% over {time} years is ${interest:,.2f}.")
