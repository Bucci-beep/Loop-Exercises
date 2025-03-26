# Get the monthly budget from the user
budget = float(input("Enter your monthly budget: "))

# Get the number of expense categories
num_categories = int(input("How many expense categories do you have? "))

# Initialize an empty dictionary to store expenses for each category
expenses = {}

# Loop through each category and prompt the user for details
for i in range(num_categories):
    category_name = input(f"Enter the name for expense category {i+1}: ")
    amount_spent = float(input(f"Enter the amount spent on {category_name}: "))
    expenses[category_name] = amount_spent

# Calculate the total expenses
total_spent = sum(expenses.values())

# Calculate and display the remaining balance
remaining_balance = budget - total_spent

# Display the results
print("\n--- Monthly Expense Summary ----")
print(f"Total spent: ${total_spent:.2f}")
print(f"Remaining balance: ${remaining_balance:.2f}")

