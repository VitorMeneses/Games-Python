import divination
import gallows

print("***********************************************************")
print("***********************************************************")
print("***********************************************************")


print ("Choose your game")
print("(1) Gallows     (2) Divination")
print("***********************************************************")

game = int(input(">>>"))

if (game == 1):
    print("Starting Gallows")
    gallows.play_gallows()
elif (game == 2):
    print("Starting Divination")
    divination.play_divination()
