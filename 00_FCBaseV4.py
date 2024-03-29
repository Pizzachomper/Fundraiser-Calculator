import pandas

# Functions go here
# Checks users entered an integer to a given question
def num_check(question, error, num_type):

    while True:
        try:
            response = num_type(input(question))
            
            if response <= 0:
                print(error)

            else:
                return response

        except ValueError:
            print("Please enter an integer")
            print()

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

# Checks that user response is not blank
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        # If response is blank output error
        if response == "":
            print(error)
            continue

        
        return response

# Currency formatting function
def currency(x):
    return f"${x:.2f}"

# Get expenses, return list which has the data frame and sub total
def get_expenses(var_fixed):
    # Set up dictionaries and list

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # loop to get component, quantity, item
    item_name = ""
    while item_name.lower() != "xxx":
        print()

        # Get name, quantity, and item
        item_name = not_blank("Item name: ",
                            "The item name can't be blank.")
        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":
            quantity = num_check("Quantity: ",
                            "The amount must be a whole number more than zero", int)
        else:
            quantity = 1
        
        price = num_check("How much for a single item? $",
                        "The price must be a number more than zero", float)
        
        # Add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate the cost of each component
    expense_frame['Cost'] = expense_frame ['Quantity'] * expense_frame['Price']

    # Find sub total
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]
        
# Prints expense frames
def expense_print(heading, frame, subtotal):
    
    # Printing area
    print()
    print(F"*** {heading} Costs ***")
    print(frame)
    print()
    print(F"{heading} Costs: ${subtotal:.2f}")
    return ""

# Work out profit goal and total sales required
def profit_goal(total_costs):
    
    # Initialise variables and error message
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:
        
        # Ask for profit goal
        response = input("What is your profit goal?: ")

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
            if dollar_type == "yes":
                profit = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no(F"Do you mean %{amount:.2f}? (Yes/No): ")
            if percent_type =="yes":
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
want_instructions = yes_no("Do you want to read the instructions? ").lower()

if want_instructions == "yes" or want_instructions == "y":
    print()
    print("Instructions go here")
    print()

# Get user data
product_name = not_blank("Product name: ",
                        "The product name can't be blank.")

# Get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = yes_no ("Do you have fixed costs?: ")

if have_fixed == "yes" or have_fixed == "y":
    # Get fixed costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]

else:
    fixed_sub = 0

# Work out total costs and profit target
all_costs = variable_sub + fixed_sub
profit_target = profit_goal(all_costs)

# Calculate recommended price
selling_price = 0

# Ask user for profit goal
print()
print(F"*** Fund Raising - {product_name} ***")
print()
expense_print("Variable", variable_frame, variable_sub)

if have_fixed == "yes":
    expense_print("Fixed", fixed_frame [['Cost']], fixed_sub)

print()
print(F"***** Total Costs: ${all_costs:.2f} *****")
print()
print("*** Profit & Sales Target ***")
print(F"Profit target: ${profit_target:.2f}")
print(F"Total Sales: ${(all_costs + profit_target):.2f}")
print()
print(F"Recommended selling price: {selling_price:.2f}")