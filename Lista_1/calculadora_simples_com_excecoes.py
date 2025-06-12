"""
Crie um programa que solicite dois números inteiros e uma operação matemática (`+`, `-`, `*`, `/`). Execute a operação escolhida e exiba o resultado. Utilize tratamento de exceções para divisões por zero e entradas inválidas.
"""

num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero inteiro: "))

operacao = input("Digite a operação desejada (+, -, *, /): ")

try:
    if operacao == '+':
      resultado = num1 = num2
    elif operacao == '-':
      resultado = num1 - num2
    elif operacao == '*':
      resultado = num1 * num2
    elif operacao == '/':
       if num2 == 0:
          raise ValueError("Divisão por zero não é permitida.")
       else:
            resultado = num1 / num2
    else:
        raise ValueError("Operação inválida. Use +, -, * ou /.")
except ValueError as e:
    print(f"Erro: {e}")
    resultado = None

print(f"O resultado da operação {num1} {operacao} {num2} é: {resultado}" if resultado is not None else "Não foi possível calcular o resultado devido a um erro.")

       
    


