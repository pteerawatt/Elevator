# In this exercise we demonstrait a program that simulates riding an elevator.
#simple version
# this is 2nd draft
# refractored
import time
import sys

def print_pause(message): #add print_pause() to refractor
    print(message)
    sys.stdout.flush()
    time.sleep(2)



print_pause("You have just arrived at your new job!")
print_pause("You are in the elevator.")


while True:
    print_pause("Please enter the number for the floor "
                "you would like to visit:")
    floor = input("1. Lobby\n"  #switch out each print_pause to just making it intput
                "2. Human resources\n" #also switch out variable name to floor from response
                "3.Engineering department\n")

    if floor == "1":    #switch out if in to if ==
        print_pause("You push the button for the first floor.")
        print_pause("You find yourself in the lobby")
    elif floor == "2":
        print_pause("You push the button for second floor.")
        print_pause("You find yourself in the human resources department.")
    elif floor == "3":
        print_pause("You push the button for third floor.")
        print_pause("you find yourself in the engineering department.")

    print_pause("where would you like to go next?") # remove where would you like to go next at each choice and just add to the end of loop instead.
    
