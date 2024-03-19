import pandas
import math

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
            if dollar_type == "yes" or "y":
                profit = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no(F"Do you mean {amount:.2f}%? (Yes/No): ")
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

# rounding function
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to


# Main routine goes here
want_instructions = yes_no("Do you want to read the instructions? ").lower()

if want_instructions == "yes" or want_instructions == "y":
    print()
    print("--- Instructions ---")
    print()
    print("The fundraising claculator can be used to find if you have reached a porfit goal ")
    print("You will need to provide the product name, item name, quantity, price")
    print("Fixed costs are also optional after you have finished your variable costs")
    print()
    
# Get user data
product_name = not_blank("Product name: ",
                        "The product name can't be blank.")

how_many = num_check("How many items will you be producing? ", "The number of items must be a whole number more than 0", int)

# Get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

# Change frames to string
variable_txt = pandas.DataFrame.to_string(variable_frame)

print()
have_fixed = yes_no ("Do you have fixed costs?: ")

if have_fixed == "yes" or have_fixed == "y":
    # Get fixed costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]

    fixed_txt = pandas.DataFrame.to_string(fixed_frame)

else:
    fixed_sub = 0

# Work out total costs and profit target
all_costs = variable_sub + fixed_sub
profit_target = profit_goal(all_costs)

# Calculate total sales needed to reach goal
sales_needed = all_costs + profit_target

# Ask user for rounding 
round_to = num_check("Round to nearest ...?: ", "Cant be 0", int)

# Calculate recommended price
selling_price = sales_needed / how_many
print(F"Selling price (unrounded): ${selling_price:.2f}")

recommended_price = round_up(selling_price)

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
print(F"Total sales: ${(all_costs + profit_target):.2f}")
print()

print("*** Pricing ***")
print(F"Minimum price: ${selling_price:.2f}")
print(F"Recomended price: ${recommended_price:.2f}")

to_write = [product_name, variable_txt, fixed_txt, profit_target, required_sales, recommended_price]

# Write to file
# Create file to hold data
file_name = F"{product_name}.txt"
text_file = open(file_name, "w+")

# Heading
for item in to_write:
    text_file.write(item)
    text_file.write("\n\n")

# Close file
text_file.close()

# Printing
for item in to_write:
    print(item)
    print()