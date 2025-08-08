porcentagem_str = input("Digite a porcentagem de desconto: (Ex: 10%)")
compra_str = input("Digite o valor da compra: ")

try:
    porcentagem = float(porcentagem_str.replace("%", "")) / 100
    compra = float(compra_str)
except ValueError:
    print("Entrada inválida.")
    exit()


def aplicar_desconto(valor_compra):
    def calcular(percentual_desconto):
        return valor_compra * (1 - percentual_desconto)

    return calcular


calculadora_desconto = aplicar_desconto(compra)
valor_final = calculadora_desconto(porcentagem)

print(f"O valor final com desconto é: R$ {valor_final:.2f}")
