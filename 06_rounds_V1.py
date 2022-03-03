balance = 5 


rounds_played = 0 

play_again = input("Press <enter> to play...").lower()
while play_again == "":

    #inrease num of rounds played
    rounds_played += 1 

    print("** Round #{} **".format(rounds_played))
    balance -= 1 
    print("balance: ", balance)
    print()

    if balance <1:
        play_again = "xxx"
        print("sorry you have run out of money")
    else:
        play_again = input("press <Enter> to play again or <xxx> to quit")