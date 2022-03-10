import random

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
    print("(1): type how much money you want to play with (must be between $0 and $10). press enter ")
    print()
    print("(2): press enter as many times as you can")
    print()
    print("(3): see how many rounds you get to play ")
    print()
    print("Good Luck!!!")
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


def statement_generator(statement, decoration, style):
    sides = decoration * 3 

    statement = "{} {} {}".format(sides, statement, sides)

    top_bottom = decoration * len(statement)

    if style == 3:

        print(top_bottom)
        print(statement)
        print(top_bottom)

    else:
        print(statement)

    return ""


# ***** Main Routine goes here ****

played_before = yes_no("have you played the game before?")

if played_before == "no": 
    instructions()

print()

how_much = num_check("how much would you like to play with? ", 0, 10)

balance = how_much

rounds_played = 0 

play_again = input("Press <enter> to play...").lower()
while play_again == "":

    #inrease num of rounds played
    rounds_played += 1 

    rounds_heading = "** Round #{} **".format(rounds_played)
    statement_generator(rounds_heading, "-", 3)
        
    chosen_num = random.randint(1,100)

    #adjust balance
    #if the random number is between 1 and 5,
    #user gets a unicorn (add $4 to balance)
    if 1<= chosen_num <= 5: 
        chosen = "unicorn"
        decoration = "*"
        balance += 4
    #if the random number is between 6 and 36
    #user gets a donkey(subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        decoration = "D"
        balance -= 1
    #the token is either a horse or a zebra...
    #in both cases subtract $0.50 from the balance
    else:
        #if the number is even, set the chosen item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            decoration = "H"
        #otherwise set it to a zebra
        else:
            chosen = "zebra"
            decoration = "Z"
        balance -= 0.5

    result = "You got a {}.  Your current balance is ${:.2f}".format(chosen, balance)

    print()
    statement_generator(result, decoration, 1)
    print()

    if balance <1:
        play_again = "xxx"
        print("sorry you have run out of money")
    else:
        play_again = input("press <Enter> to play again or <xxx> to quit")
    
    

print()
print("Final balance: ${:.2f}".format(balance))

