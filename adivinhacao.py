print("*********************************")
print("Bem Vindo ao jogo de Adivinhação")
print("*********************************")

numero_secreto = 42

chute_strg = input("Digite o seu numero: ")


print("Você Digitou: ", chute_strg)

chute = int (chute_strg)

if(numero_secreto == chute):
    print("Você acertou")
else:
    print("Erroooooooooooou")

