# set up the random
import random
from random import randint

print("Welcome to the number guessing game!")

the_seed_value = (input("Enter random seed: "))
random.seed(the_seed_value)

# the game itself
play_again = "yes"
# first loop for yes or no playing
while play_again == "yes":

    num = randint(1, 100)
    guess = int(input("\nPlease enter a guess: "))
    number_of_guesses = 1

    # second loop for guessing
    while guess != num:
        if guess < num:
            print("Higher")
            guess = int(input("\nPlease enter a guess: "))
            number_of_guesses += 1
        if guess > num:
            print("Lower")
            guess = int(input("\nPlease enter a guess: "))
            number_of_guesses += 1
    # end of the second loop

    print("Congratulations. You guessed it!")
    print("It took you {} guesses.".format(number_of_guesses))

    # if the user input anything but "yes", the first loop will finish after printing "Thank you. Good by."
    play_again = input("\nWould you like to play again (yes/no)? ")

    if play_again == "no":
        print("Thank you. Goodbye.")



