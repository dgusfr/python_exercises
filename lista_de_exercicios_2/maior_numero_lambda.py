"""
Implemente uma função lambda que receba dois números e retorne o maior deles. Teste a função com diferentes pares de valores.
"""

maior_numero = lambda x, y: x if x > y else y

print(maior_numero(10, 20))
print(maior_numero(30, 15))
print(maior_numero(5, 5))
