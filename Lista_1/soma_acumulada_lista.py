"""
Crie uma lista de números inteiros e utilize um laço `for` para imprimir a soma acumulada dos elementos, passo a passo, linha por linha.
"""

lista = [1, 2, 3, 4, 5]
soma_acumulada = 0

for numero in lista:
    soma_acumulada += numero
    print(f"Soma acumulada até agora: {soma_acumulada}")
print(f"Soma total: {soma_acumulada}")
