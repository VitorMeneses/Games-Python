import adivinhacao
import forca

print("***********************************************************")
print("***********************************************************")
print("******************Escolha seu Jogo*************************")
print("***********************************************************")


print ("Escolha seu Jogo")
print("(1) Forca     (2) Adivinhação")
print("***********************************************************")

jogo = int(input(">>>"))

if (jogo == 1):
    print("Iniciando Forca")
    forca.jogar_forca()
elif (jogo == 2):
    print("iniciando Adivinhação")
    adivinhacao.play_divination()
