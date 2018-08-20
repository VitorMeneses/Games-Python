import random


def play_divination():


    print("***********************************************************")
    print("***********************************************************")
    print("Welcome!", "                                             ***")
    print("Discover the secret number", "                           ***")
    print("***********************************************************")

    print("Do you want to start the game?")
    print("1 (Yes)     2(No)")
    print("***********************************************************")
    start = int(input(">>> "))
    print("***********************************************************")

    if start == 1:
        print("Loading [...]")
        print()
    elif start == 2:
        exit("See You")

    secret_number = random.randrange(1, 101)
    total_of_attempts = 0
    points = 1000

    print("***********************************************************")
    print("What is the level of difficulty?")
    print("(1) Easy (2) Medium (3) Hard")
    print("***********************************************************")

    level = int(input("Set the level: "))

    while (level > 3):
        level = int(input("Report the difficulty: (1) Easy (2) Medium (3) Hard:    "))
        if (level):
            print("***********************************************************")
            continue

    if (level == 1):
        total_of_attempts = 20
    else:
        if (level == 2):
            total_of_attempts = 10
        elif (level == 3):
            total_of_attempts = 5

    for rodada in range(1, total_of_attempts + 1):
        print("***********************************************************")
        print("Attempts {} of {}".format(rodada, total_of_attempts))
        kick_strg = input("Enter your number from 1 to 100: ")
        print("***********************************************************")
        print("You typed: ", kick_strg)
        if not kick_strg.isdigit():
            print("You should enter a numerical value....")
            continue

        kick = int(kick_strg)

        if (kick < 1 or kick > 100):
            print("You must enter a number between 1 and 100!!")
            print("***********************************************************")
            continue

        hit = secret_number == kick
        bigger = kick > secret_number
        smaller = kick < secret_number

        if (hit):
            print("You hit and you made {} points!".format(points))
            break
        else:
            if (bigger):
                print("You missed! You kick was bigger than the secret number. ")
                print("***********************************************************")

            elif (smaller):
                print("You missed! You kick was less than the secret number. ")
                print("***********************************************************")
                lost_points = abs(secret_number - kick)
                points = points - lost_points

        rodada = rodada + 1

    print("***********************************************************")
    print("The End")
    print("***********************************************************")

if(__name__ == "__main__"):
    play_divination()