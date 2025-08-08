porcentagem = input("Digite a porcentagem de desconto: (Ex: 10%)")
compra = input("Digite o valor da compra: ")


def aplicar_desconto(valor_compra):
    def calcular(percentual_desconto):
        return valor_compra * (1 - percentual_desconto)

    return calcular


calculadora_desconto = aplicar_desconto(compra)
valor_final = calculadora_desconto(porcentagem)

print(f"O valor final com desconto é: R$ {valor_final:.2f}")
