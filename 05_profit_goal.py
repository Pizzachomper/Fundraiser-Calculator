# functions go here

# Asks user a yes or no question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter either yes or no")

# Work out profit goal and total sales required
def profit_goal(total_costs):
    
    # Initialise variables and error message
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:
        
        # Ask for profit goal
        print()
        response = input("What is your profit goal? (eg $500 or 50%): ")

        # Check if first charecter is $
        if response[0] == "$":
            profit_type = "$"
            # Get amount (Everything after the $)
            amount = response[1:]

        # Check if last charecter is $
        elif response[-1] == "%":
            profit_type = "%"
            # Get amount (everything before the %)
            amount = response[:-1]

        # Set response to amount for now
        else:
            profit_type = "unknown"
            amount = response

        # Check amount is a number more than zero
        try:
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no(F"Do you mean ${amount:.2f}, example: ${amount:.2f} dollars?: ")

            # Set profit type based on users answer above
            if dollar_type == "yes" or "y":
                profit = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no(F"Do you mean {amount:.2f}% ? (Yes/No): ")
            if percent_type =="yes" or "y":
                profit_type = "%"
            else:
                profit_type = "$"

        # Return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal


# Main routine goes here
all_costs = 200

# Loop for quick testing
for item in range(0, 6):
    profit_target = profit_goal(all_costs)
    print(F"Profit Target: ${profit_target:.2f}")
    print(F"Total Sales: ${(all_costs + profit_target):.2f}")