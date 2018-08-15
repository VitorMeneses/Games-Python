
chute_strg = input("Digite o seu número entre 1 a 100: ")
print("***********************************************************")
print("Você Digitou: ", chute_strg)



dificuldade = input("Defina o nivel: ")

while (dificuldade != int):
    dificuldade = input("Defina o nivel: ")
    if not dificuldade.isdigit():
        print("Você deve digitar um número...")
        continue

nivel = int(dificuldade)

while(nivel > 3):
    nivel = int(input("Informe a Dificuldade: (1) Fácil (2) Médio (3) Difícil:    "))
    if (nivel):
        print("***********************************************************")
        continue