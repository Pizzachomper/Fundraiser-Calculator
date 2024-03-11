import math

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

# rounding function
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to

how_many = num_check("How many items? ", "Cant be 0", int)
total = num_check("Total costs? ", "More than 0", float)
profit_goal = num_check("Profit Goal? ", "More than 0", float)
round_to = num_check("Round to nearest ...?", "Cant be 0", int)

sales_needed = total + profit_goal

print(F"Total: ${total:.2f}")
print(F"Profit: ${profit_goal:.2f}")

selling_price = sales_needed / how_many
print(F"Selling price (unrounded): ${selling_price}")

recommended_price = round_up(selling_price, round_to)
print(F"Reommended price: ${selling_price}")
