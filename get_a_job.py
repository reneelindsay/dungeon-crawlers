# # # # # # # # # # # #
#                     #
# A DIALOGUE BEGINS   #
#                     #
# ME:                 #
#                     #
# Read the program    #
# Play the game       #
# Add a step          #
# Don't make it lame  #
#                     #
# Hints are fine      #
# But not too many    #
# The purpose is      #
# To tell a story     #
#                     #
# JOHN:               #
#                     #
# Alas, a maze;       #
# a fetid warren      #
# but don't give up   #
# I am implorin'      #
#                     #
# ME:                 #
#                     #
# Yet even out,       #
# One is not done     #
# I'm scared to talk  #
# To anyone!          #
#                     #
# # # # # # # # # # # #

import random

# this code was written by me
def guess():
    print("How many interviews will Renee fail before she lands the job?")
    correct_number = random.randint(1, 20)
    found = False

    while not found:
        johns_guess = int(input("Make your best guess. "))
        if johns_guess == correct_number:
            print("You guessed it! Is it luck or skill?")
            found = True
        elif johns_guess > correct_number:
            print("What? Too many. Renee can do better than that!")
        else:
            print("Too few. She's still green, you know.")

# this code was written by John
def maze():
    there = [[1, 4, 5], [0, 2, 6], [1, 3, 7], [2, 4, 8], [0, 3, 9], [0, 6, 9], [1, 5, 7], [2, 6, 8], [3, 7, 9],
             [4, 5, 8]]
    stuff = [0, 0, 0, 0, 1, 2, 2, 2, 3, 4]

    def reset():
        random.shuffle(stuff)
        print("\n...You find yourself in a maze of twisty job applications, all alike.")

    reset()
    here = stuff.index(1)
    while True:
        room = there[here]
        print("\nStanding in room " + str(here) + ", you see hyperlinks leading to rooms " + str(room[0]) + ", " + str(
            room[1]) + ", (oxford comma) and " + str(room[2]) + ".")
        if 4 in [stuff[x] for x in room]:
            print("I smell a Wumpus.")
        if stuff[here] == 2:
            print("There are recruiter leavings on the ground here. gross.")
        if stuff[here] == 3:
            print("There is a ruler here. Measure twice, cut once, and all that.")

        # (John gives me a hint)
        # if only there were a way out...

        command = input("> ")
        if command in [str(x) for x in room]:
            print(random.choice(
                ["With some trepidation", "Listlessly", "Eagerly", "With a battlecry"]) + ", you click the link.")
            here = int(command)
            if stuff[here] == 4:
                print("Phew. For a moment I thought you were going to navigate straight into a ravenous Wumpus.")
                print("It turns out you have found an equally rank but somewhat less ravenous Setbackbeast.")
                print("It's a relief not to be eaten, but the walls just started swimming in a most peculiar-")
                print("*BOOF*")
                reset()

            # (I make my first attempt to find a way out)
            # if only my way out didn't end the whole program...this game isn't over yet!

            elif stuff[here] == 1:
                print("\n...as the door opens, you spy a small table. On it rests your resume and a vintage telephone.")
                print("\nThe telephone rings.")
                break
        elif str.isdigit(command):
            print("Your head makes a coconut noise against the wall. Ouch.")
        else:
            print("I'm afraid I don't follow you.")

# (my second attempt to find a way out)
# a night's sleep clears the head

def phone():
    answer_yes = "yes"
    answer_no = "no"
    print("\n...you stare at the ringing phone with a feeling of impending dread.")
    print("It rings three times, four, five...")
    print("\nDo you pick it up? Type 'yes' if you do, 'no' if you do not.")

    # running into trouble here
    # "yes" and "no" inputs are not recognized
    
    while True:
        command = input("> ")
        if command is answer_yes:
            print("\nWith a deep breath, you reach out to the heavy receiver and pick it up.")
            print("\n...Hello?")
        elif command is answer_no:
            print("\nYou stand rooted to the spot, unable to move. The phone rings several more times...")
            print("\nthen stops. You close your eyes in silent shame.")

        else:
            print("The phone is still ringing. Only 'yes' or 'no' will make it stop.")

if __name__ == ("__main__"):

    guess()
    maze()
    phone()