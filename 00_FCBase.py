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


# Main routine goes here
want_instructions = yes_no("Do you want to read the instructions? ").lower()

if want_instructions == "yes" or want_instructions == "y":
    print("Instructions go here")

print("program continues...")
print()

get_int = num_check("How many do you need? ",
                    "Please enter an amount more than 0\n", int)

get_cost = num_check("How much does it cost? $",
                     "Please enter a number more than 0\n", float)

print()
print(F"You need: {get_int}")
print(F"It costs {get_cost}")