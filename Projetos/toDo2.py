"""
import random

def adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            palpite = int(input("Tente adivinhar o número (1-100): "))

            if not 1 <= palpite <= 100:
                raise ValueError("Número fora do intervalo! Digite um número entre 1 e 100.")

            tentativas += 1

            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break

        except ValueError as e:
            print(f"Entrada inválida: {e}")

adivinhar_numero()

___

Crie um codigo em python que gere um número aleatório entre 1 e 100, permita que o usuário tente adivinhá-lo, informando se o palpite é maior ou menor, até acertar. Trate erros de entrada: se o valor for inválido (não numérico) ou fora do intervalo 1-100, lance uma exceção ValueError e exiba uma mensagem apropriada.

Exemplo de acerto (supondo número 37):
Tente adivinhar o número (1-100): 37
Saída: Parabéns! Você acertou o número 37.

Exemplo de palpite baixo:
Muito baixo! Tente novamente.

Exemplo de palpite alto:
Muito alto! Tente novamente.

Exemplo de entrada inválida (fora do intervalo):
Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100.

Exemplo de entrada inválida (não numérica):
Entrada inválida: invalid literal for int() with base 10: 'abc'

"""
