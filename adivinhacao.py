print("*********************************")
print("Bem Vindo ao jogo de Adivinhação Númerica")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 5


for rodada in range (1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_strg = input("Digite o seu número entre 1 a 200: ")
        print("Você Digitou: ", chute_strg)
        chute = int(chute_strg)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre um e 200!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou")
            break
        else:
            if(maior):
                print("Você errou! O Seu chute foi maior que o numero secreto. ")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o numero secreto. ")

        rodada = rodada + 1



print("Final de Jogo")

