import random
from time import sleep


# Creating a function to stop redundacncy

def new_game():
    another_game = str(input("Enter Yes to play again or No to stop playing."))

    if another_game.lower() in ["y", "Y", "yes", "Yes"]:
        print("Awesome! Let's Play again!")
        return True

    else:
        space()
        print("Fine! No game for you!")
        sleep(4)
        space()
        print("Why are you still here??")
        space()
        sleep(4)
        print("The game is over...")
        sleep(4)
        space()
        print("dude stop staring........")
        space()
        sleep(4)
        print("Go away...")
        return False

# This function is to stop reduncandcy as well


def space():
    print()
    print()


magic_number = random.randint(1, 20)
keep_playing = True
turns = 0

while keep_playing:
    guessed_number = int(input("Guess the number: "))
    turns += 1

    if turns == 5:
        print("Game over, you Lost!")
        keep_playing = new_game()
        # the variable turn in the if statements are so that once the game starts over so do the number of turns you get
        turns = 0
        magic_number = random.randint(1, 20)

    if guessed_number == magic_number:
        print("You guessed the right number!")
        keep_playing = new_game()
        turns = 0
        magic_number = random.randint(1, 20)

    elif guessed_number < magic_number:
        random_message = ['Keep Guessing Higher!', "Try a Higher number!"]
        print(random.choice(random_message))

    elif guessed_number > magic_number:
        random_message = ['Keep Guessing Lower!', "Try a Lower number!"]
        print(random.choice(random_message))
