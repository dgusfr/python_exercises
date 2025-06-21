"""
Implemente uma função lambda que receba dois números e retorne o maior deles. Teste a função com diferentes pares de valores.
"""

maior_numero = lambda x, y: x if x > y else y
# Testando a função lambda com diferentes pares de valores
print(maior_numero(10, 20))  # Deve retornar 20
print(maior_numero(30, 15))  # Deve retornar 30
print(maior_numero(5, 5))  # Deve retornar 5
