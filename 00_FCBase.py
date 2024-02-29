# Functions go here
# Checks users enter an integer to a given question
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

# Main routine goes here
get_int = num_check("How many do you need? ",
                    "Please enter an amount more than 0\n", int)

get_cost = num_check("How much does it cost? $",
                     "Please enter a number more than 0\n", float)

print()
print(F"You need: {get_int}")
print(F"It costs {get_cost}")