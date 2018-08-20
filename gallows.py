import random
import illustration

def play_gallows():

    print("***********************************************************")
    print("***********************************************************")
    print("Welcome to the gallows game.!", "                            ***")
    print("***********************************************************")

    print ("Do you want to start the game?")
    print("1 (Yes)     2 (No)")
    print("***********************************************************")
    start = int(input(">>> "))
    print("***********************************************************")

    if start == 1:
        print("Loading [...]")
        print()
    elif start == 2:
        exit("See You")


    archive = open("words.txt", "r", encoding="utf8")
    words = []

    for line in archive:
        line = line.strip()
        words.append(line)


    archive.close()

    number = random.randrange(0, len(words))
    secret_words = words[number].upper()


    hits = ["_" for lyrics in secret_words]


    hanged = False
    hit = False
    error = 0

    print(hits)
    print("The word has {} letters".format(len(secret_words)))

    while(not hanged and not hit):

        kick = input("What is the letter? ")
        kick = kick.strip().upper()

        if(kick in secret_words):
            index = 0
            for lyrics in secret_words:
                if(kick == lyrics):
                    hits[index] = lyrics
                index += 1
        else:
            error += 1
            print("Oops, you screwed up! Missing {} attempts.".format(7-error))
            illustration.illustration_gallows(error)


        hanged = error == 7
        hit = "_" not in hits
        print(hits)


    if(hit):
        illustration.illustration_trophy()

    else:
        illustration.illustration_skull()
        print("You lost!! :( and the word was {}".format(secret_words))

print("***********************************************************")
print("End")
print("***********************************************************")

if(__name__ == "__main__"):
    play_gallows()

