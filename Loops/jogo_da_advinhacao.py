import random

acertou = False 

numero_aleatorio = random.randint(0, 100)

while not acertou:
    numero = int(input("Digite um número inteiro de 0 a 100: "))

    if numero < numero_aleatorio:
        print("O número informado é MENOR que o número especial.")
    elif numero > numero_aleatorio:
        print("O número informado é MAIOR que o número especial.")
    else:
        print(f"Parabéns, você acertou o número aleatório, que é {numero_aleatorio}!")
        acertou = True  
