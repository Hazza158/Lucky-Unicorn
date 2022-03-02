# checks for yes / no, returns "yes" / "no"
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        
        if response == "yes" or response == "y":
            return "yes"
            
        
        elif response == "no" or response == "n":
            return "no"
        
        else:
            print("please answer yes / no")

# Displays instructions, returns ""        
def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
    return "" 


def num_check(question, low, high) :
    error = "please enter a whole number between 1 and 10\n"

    valid = False 
    while not valid:
        try:
            response = int(input(question)) 

            if low < response <= high:
                return response


            else:
                print(error)

        except ValueError:
                print(error)


# ***** Main Routine goes here ****

played_before = yes_no("have you played the game before?")

if played_before == "no": 
    instructions()


how_much = num_check("how much would you like to play with? ", 0, 10)

print("You are playing with ${:.2f}".format(how_much))

