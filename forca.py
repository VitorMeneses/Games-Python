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

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input("Qual a letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1


        print("jogando....")




    print("Fim de Jogo")

if(__name__ == "__main__"):
    jogar_forca()




















print("***********************************************************")
print("Final de Jogo")
print("***********************************************************")