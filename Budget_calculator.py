# Budget Breakdown Calculator

# Prompt the user to enter their total monthly budget (net income)
total_budget = float(input("Enter your total monthly budget (net income): "))

# Prompt the user to enter expenses for different categories
housing = float(input("Enter your Housing cost: "))
utilities = float(input("Enter your Utilities cost: "))
groceries = float(input("Enter your Groceries cost: "))
transportation = float(input("Enter your Transportation cost: "))
health_care = float(input("Enter your Health Care cost: "))
personal_care = float(input("Enter your Personal Care cost: "))
clothing = float(input("Enter your Clothing cost: "))
debt = float(input("Enter your Debt payments: "))

# Calculate percentage of total budget for each category


def calculate_percentage(amount, total):
    return (amount / total) * 100 if total > 0 else 0


# Display the budget breakdown in a user-friendly format
print("\n--- Budget Breakdown ---")
print(f"Housing: {calculate_percentage(housing, total_budget):.2f}%")
print(f"Utilities: {calculate_percentage(utilities, total_budget):.2f}%")
print(f"Groceries: {calculate_percentage(groceries, total_budget):.2f}%")
print(
    f"Transportation: {calculate_percentage(transportation, total_budget):.2f}%")
print(f"Health Care: {calculate_percentage(health_care, total_budget):.2f}%")
print(
    f"Personal Care: {calculate_percentage(personal_care, total_budget):.2f}%")
print(f"Clothing: {calculate_percentage(clothing, total_budget):.2f}%")
print(f"Debt: {calculate_percentage(debt, total_budget):.2f}%")

# Calculate total expenses and remaining budget
total_expenses = housing + utilities + groceries + \
    transportation + health_care + personal_care + clothing + debt
remaining_budget = total_budget - total_expenses

# Display total expenses and remaining budget
print(f"\nTotal Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")

# Provide a financial health message based on remaining budget
if remaining_budget > 0:
    print("Great job! You are within your budget.")
elif remaining_budget == 0:
    print("You have used your entire budget. Plan carefully! ")
else:
    print("Warning: You have exceeded your budget! Consider adjusting expenses.")
