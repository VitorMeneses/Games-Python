def jogar_forca():

    print("***********************************************************")
    print("***********************************************************")
    print("Bem Vindo ao jogo da Forca!", "                                             ***")
    print("***********************************************************")

    print ("Deseja iniciar o jogo?")
    print("1 (Sim)     2(Não)")
    print("***********************************************************")
    inicio = int(input(">>> "))
    print("***********************************************************")

    if inicio == 1:
        print("Iniciando [...]")
        print()
    elif inicio == 2:
        exit("Até mais")

    palavra_secreta = "banana".upper()
    acertos = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0

    print(acertos)

    while(not enforcou and not acertou):

        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    acertos[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in acertos
        print(acertos)


    if(acertou):
        print("Você Ganhou!!!")
    else:
        print("Você perdeu!! :(")


if(__name__ == "__main__"):
    jogar_forca()

print("***********************************************************")
print("Final de Jogo")
print("***********************************************************")