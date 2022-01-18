# Print a greeting to the user
print("Welcome to the Tip Calculator.")

# Get input from the user
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percetange tip would you like to give? 10, 12 or 15 "))
number_of_people = int(input("How many people to split the bill? "))

# Perform calculation
tip_as_percent = tip / 100
total_tip_amount = total_bill * tip_as_percent
total_bill_with_tip = total_bill + total_tip_amount
individual_share = total_bill_with_tip / number_of_people

# Ensure final result to have 2 decimal places
individual_share = "{:.2f}".format(individual_share)

# Print result on console / command-line / terminal
print(f"Each person should pay: ${individual_share}")
