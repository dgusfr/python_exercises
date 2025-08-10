"""
import random
def pedra_papel_tesoura():
opcoes = ["pedra", "papel", "tesoura"]
escolha_computador = random.choice(opcoes)
escolha_usuario = input("Escolha: pedra, papel ou tesoura? ").lower()

if escolha_usuario not in opcoes:
    print("Escolha inválida!")
    return

print(f"Computador escolheu: {escolha_computador}")

if escolha_usuario == escolha_computador:
    print("Empate!")
elif (
    (escolha_usuario == "pedra" and escolha_computador == "tesoura") or
    (escolha_usuario == "papel" and escolha_computador == "pedra") or
    (escolha_usuario == "tesoura" and escolha_computador == "papel")
):
    print("Você venceu!")
else:
    print("Você perdeu!")

pedra_papel_tesoura()

---

Crie um código em Python que permita ao usuário escolher entre pedra, papel ou tesoura, com o computador escolhendo aleatoriamente uma opção. Exiba a escolha do computador e o resultado da partida (quem venceu ou se foi empate), seguindo as regras: pedra ganha de tesoura, tesoura ganha de papel, papel ganha de pedra.

Exemplo de entrada:
Escolha: pedra, papel ou tesoura? papel
Saída (se computador escolher pedra): Computador escolheu: pedra
Você venceu!

Exemplo de derrota:
Computador escolheu: tesoura
Você perdeu!

Exemplo de empate:
Computador escolheu: papel
Empate!

"""
