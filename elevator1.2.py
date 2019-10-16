# In this exercise we demonstrait a program that simulates riding an elevator.
#simple version
# this is 1st draft
import time
import sys

print("You have just arrived at your new job!")
sys.stdout.flush()
time.sleep(2)
print("You are in the elevator.")
sys.stdout.flush()
time.sleep(2)

while True:
    print("Please enter the number for the floor you would like to visit:")
    sys.stdout.flush()
    time.sleep(2)
    print("1. Lobby")
    sys.stdout.flush()
    time.sleep(2)
    print("2. Human resources")
    sys.stdout.flush()
    time.sleep(2)
    print("3.Engineering department")
    sys.stdout.flush()
    time.sleep(2)

    response = input()
    if "1" in response:
        print("You push the button for the first floor.")
        sys.stdout.flush()
        time.sleep(2)
        print("You find yourself in the lobby")
        sys.stdout.flush()
        time.sleep(2)
        print("Where would you like to go next?")
    elif "2" in response:
        print("You push the button for second floor.")
        sys.stdout.flush()
        time.sleep(2)
        print("You find yourself in the human resources department.")
        sys.stdout.flush()
        time.sleep(2)
        print("Where would you like to go next?")
    elif "3" in response:
        print("You push the button for third floor.")
        sys.stdout.flush()
        time.sleep(2)
        print("you find yourself in the engineering department.")
        sys.stdout.flush()
        time.sleep(2)
        print("where would you like to go next?")
