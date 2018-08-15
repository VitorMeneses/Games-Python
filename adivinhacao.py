import random


def jogar_adivinhacao():


    print("***********************************************************")
    print("***********************************************************")
    print("Bem Vindo!", "                                             ***")
    print("Descubra o número secreto", "                              ***")
    print("***********************************************************")

    print("Deseja iniciar o jogo?")
    print("1 (Sim)     2(Não)")
    print("***********************************************************")
    inicio = int(input(">>> "))
    print("***********************************************************")

    if inicio == 1:
        print("Iniciando [...]")
        print()
    elif inicio == 2:
        exit("Até mais")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("***********************************************************")
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    print("***********************************************************")

    nivel = int(input("Defina o nivel: "))

    while (nivel > 3):
        nivel = int(input("Informe a Dificuldade: (1) Fácil (2) Médio (3) Difícil:    "))
        if (nivel):
            print("***********************************************************")
            continue

    if (nivel == 1):
        total_de_tentativas = 20
    else:
        if (nivel == 2):
            total_de_tentativas = 10
        elif (nivel == 3):
            total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("***********************************************************")
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_strg = input("Digite o seu número entre 1 a 100: ")
        print("***********************************************************")
        print("Você Digitou: ", chute_strg)
        if not chute_strg.isdigit():
            print("Você deveria digitar um valor númerico....")
            continue

        chute = int(chute_strg)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            print("***********************************************************")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O Seu chute foi maior que o numero secreto. ")
                print("***********************************************************")

            elif (menor):
                print("Você errou! O seu chute foi menor do que o numero secreto. ")
                print("***********************************************************")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print("***********************************************************")
    print("Final de Jogo")
    print("***********************************************************")
