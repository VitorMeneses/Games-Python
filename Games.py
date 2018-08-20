import divination
import gallows

print("***********************************************************")
print("***********************************************************")
print("***********************************************************")


print ("Choose your game")
print("(1) Gallows     (2) Divination")
print("***********************************************************")

jogo = int(input(">>>"))

if (jogo == 1):
    print("Starting Gallows")
    gallows.play_gallows()
elif (jogo == 2):
    print("Starting Divination")
    divination.play_divination()
