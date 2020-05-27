import random


def start_game():
    # write your code inside this function.

    Min = 0
    Max = 15
    play_again = "Y"
    high_score = 0

    print("hello ! and good luck ;)")

    while (play_again.lower() == "y"):

        right_guess = random.randint(Min, Max)
        answer = Max + 1
        nb_attempts = 0

        if high_score != 0:
            print("You have to do better than {} attempts".format(high_score))

        while (answer != right_guess):
            try:
                answer = int(input("what's the right number ? :"))
            except ValueError:
                print("You have to choose a number, try again")
                continue
            nb_attempts += 1

            if answer > Max:
                print("It's out of the range, you should choose a lower number ")

            elif answer < Min:
                print("It's out of the range, you should choose a higher number ")

            elif answer < right_guess:
                print("It's higher")

            elif answer > right_guess:
                print("It's lower")

        print("Got it")

        print("it took you {} attempts".format(nb_attempts))

        if not high_score:
            high_score = nb_attempts
        elif high_score > nb_attempts:
            high_score = nb_attempts

        play_again = input("Do you want to play again (Y/N) ?")

    print("Thanks for playing, see you soon !")


# Kick off the program by calling the start_game function.
start_game()