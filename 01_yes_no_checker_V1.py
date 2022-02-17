show_instructions = ""
while show_instructions.lower() != "xxx":

    show_instructions = input("have you played this game before").lower()

    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("program continues")

    elif show_instructions == "no" or show_instructions == "n":
        show_instructions = "no"
        print("display instructions")

    else:
        print("please answer yes / no")