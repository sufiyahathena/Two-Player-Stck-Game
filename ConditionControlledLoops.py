#condition controlled loops
#two-player game

sticks = input("How many sticks to start with (10-100)? ")
while float(sticks) < 10:
    sticks = input("Sorry, that's too few sticks. Try again: ")
while float(sticks) > 100:
    sticks = input("Sorry, that's too many sticks. Try again: ")
if float(sticks) <= 100 and float(sticks) >= 10:
    print("Great, let's play...")
print()
while float(sticks) <= 100:
    print()
    print("Turn: Player 1")
    print("There are ", sticks, " sticks on the table.")
    stickadd1 = input("How many sticks do you want to take (1, 2 or 3)? ")
    while float(stickadd1) > 3:
        stickadd1 = input("Sorry, that's not a valid number. Try again: ")
    while float(stickadd1) < 1:
        stickadd1 = input("Sorry, that's not a valid number. Try again: ")
    sticks = float(sticks) - float(stickadd1)
    print("There are ", sticks, " sticks on the table.")
    if sticks <= 3:
        print()
        print("Player 2 you can only take the number of sticks available on the table")
        if sticks == 2:
            print("You can take 1 or 2 sticks")
            stickadd1 = input("How many sticks do you want to take (1 or 2)? ")
            while float(stickadd1) > 2:
                stickadd1 = input("Sorry, that's not a valid number. Try again: ")
            while float(stickadd1) < 1:
                stickadd1 = input("Sorry, that's not a valid number. Try again: ")
            sticks = float(sticks) - float(stickadd1)
            print("There are ", sticks, " sticks on the table.")
            if sticks == 1:
                print()
                print("Player 1 you can only take the last remaining stick")
                stickadd1 = input("How many sticks do you want to take (1)? ")
                while float(stickadd1) != 1:
                    stickadd1 = input("Sorry, that's not a valid number. Try again: ")
                sticks = float(sticks) - float(stickadd1)
                print("There are ", sticks, " sticks on the table.")
                print()
                print("Player 2 is the winner")
        if sticks == 0:
            break
        elif sticks == 1:
            print()
            print("Player 2 you can only take the last remaining stick")
            stickadd1 = input("How many sticks do you want to take (1)? ")
            while float(stickadd1) != 1:
                stickadd1 = input("Sorry, that's not a valid number. Try again: ")
            sticks = float(sticks) - float(stickadd1)
            print("There are ", sticks, " sticks on the table.")
            print()
            print("Player 1 is the winner")
            if sticks == 0:
               break
    if sticks == 0:
        break  
    print()
    print("Turn: Player 2")
    print("There are ", sticks, " sticks on the table.")
    stickadd2 = input("How many sticks do you want to take (1, 2 or 3)? ")
    while float(stickadd2) > 3:
        stickadd2 = input("Sorry, that's not a valid number. Try again: ")
    while float(stickadd2) < 1:
        stickadd1 = input("Sorry, that's not a valid number. Try again: ")
    sticks = float(sticks) - float(stickadd2)
    print("There are ", sticks, " sticks on the table.")
    if sticks <= 3:
        print()
        print("Player 1 you can only take the number of sticks available on the table")
        if sticks == 2:
            print("You can take 1 or 2 sticks")
            stickadd2 = input("How many sticks do you want to take (1 or 2)? ")
            while float(stickadd2) > 2:
                stickadd2 = input("Sorry, that's not a valid number. Try again: ")
            while float(stickadd2) < 1:
                stickadd2 = input("Sorry, that's not a valid number. Try again: ")
            sticks = float(sticks) - float(stickadd2)
            print("There are ", sticks, " sticks on the table.")
            if sticks == 1:
                print()
                print("Player 2 you can only take the last remaining stick")
                stickadd2 = input("How many sticks do you want to take (1)? ")
                while float(stickadd2) != 1:
                    stickadd2 = input("Sorry, that's not a valid number. Try again: ")
                sticks = float(sticks) - float(stickadd2)
                print("There are ", sticks, " sticks on the table.")
                print()
                print("Player 1 is the winner")
            if sticks == 0:
               break
        elif sticks == 1:
            print()
            print("Player 1 you can only take the last remaining stick")
            stickadd2 = input("How many sticks do you want to take (1)? ")
            while float(stickadd2) != 1:
                stickadd2 = input("Sorry, that's not a valid number. Try again: ")
            sticks = float(sticks) - float(stickadd2)
            print("There are ", sticks, " sticks on the table.")
            print()
            print("Player 2 is the winner")
        if sticks == 0:
            break
    if sticks == 0:
        break  
    
print()            
print("There are no sticks left on the table. Game over.")
print("The player who did not take the last stick is the winner.")


