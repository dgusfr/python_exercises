"""
Crie um **programa em Python** que calcule automaticamente a **gorjeta** e o **valor total** a ser pago em um restaurante. O programa deve solicitar ao usuário o **valor da conta** e a **porcentagem de gorjeta** desejada, realizar os cálculos necessários e exibir tanto o **valor da gorjeta** quanto o **total final** formatados corretamente.

Requisitos:
- Use **input()** para capturar o valor da conta e a porcentagem de gorjeta
- Converta os valores para **float** para permitir casas decimais
- Calcule a gorjeta usando a fórmula: `valor_conta * (porcentagem / 100)`
- Calcule o total: `valor_conta + valor_gorjeta`[5][3]
- Formate a saída com **duas casas decimais** usando `:.2f`
- Exiba os resultados com **formatação monetária** (R$)

Entrada esperada:
```
Digite o valor da conta: 120.00
Digite a porcentagem de gorjeta: 10
```

Saída esperada:
```
Valor da gorjeta: R$ 12.00
Total a pagar: R$ 132.00
```
"""


def calcular_gorgeta():
    try:
        valor_da_conta = float(input("Digite o valor da conta: "))
        porc_de_gorjeta = float(
            input("Digite a porcentagem da gorgeta (Ex: 10% -> 10): ")
        )

        valor_gorgeta = valor_da_conta * (porc_de_gorjeta / 100)
        valor_total = valor_da_conta + valor_gorgeta

        print(f"Valor da gorgeta: R$ {valor_gorgeta:.2f}")
        print(f"Total a pagar: R$ {valor_total:.2f}")
    except ValueError:
        print(
            "Por favor, insira valores numéricos válidos para a conta e a porcentagem de gorjeta."
        )


if __name__ == "__main__":
    calcular_gorgeta()
