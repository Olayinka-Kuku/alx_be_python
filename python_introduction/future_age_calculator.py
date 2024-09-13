# Prompt the user to enter their current age
user_input = input("How old are you? ")
print(f"Debug: Received input - {user_input}")

try:
    current_age = int(user_input)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

# Calculate the age in the year 2050
age_in_2050 = current_age + (2050 - 2023)

# Print the result
print(f"In 2050, you will be {age_in_2050} years old.")