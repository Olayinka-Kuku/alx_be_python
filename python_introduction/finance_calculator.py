# Prompt the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses
total_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - total_expenses

# Calculate projected annual savings with a 5% interest rate
annual_savings = monthly_savings * 12
interest_rate = 0.05
projected_savings = annual_savings + (annual_savings * interest_rate)

# Output results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
