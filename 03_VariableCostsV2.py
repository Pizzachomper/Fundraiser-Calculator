import pandas
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

        quantity = num_check("Quantity: ",
                            "The amount must be a whole number more than zero", int)
        
        price = num_check("How much for a single item? $",
                        "The price must be a number more than zero", float)
        
        # Add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')
        

# Main routine

# Get user data
product_name = not_blank("Product name: ",
                         "The product name can't be blank.")


variable_frame = pandas.DataFrame(variable_dict)
variable_frame = variable_frame.set_index('Item')

# Calculate the cost of each component
variable_frame['Cost'] = variable_frame ['Quantity'] * variable_frame['Price']

# Find sub total
variable_sub = variable_frame['Cost'].sum()

# Currency Formatting
add_dollars = ['Price', 'Cost']
for item in add_dollars:
    variable_frame[item] = variable_frame[item].apply(currency)

# Printing area
print(variable_frame)
print()
print(F"Variable Costs: ${variable_sub}")