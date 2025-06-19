"""
Crie um dicionário para armazenar dados de um livro: título, autor, ano e número de páginas. Solicite os dados ao usuário e, ao final, exiba o dicionário formatado.
"""

livro = {"titulo": "", "autor": "", "ano": 0, "numero_paginas": 0}

livro["titulo"] = input("Digite o titulo do livro: ")
livro["autor"] = input("Digite o autor do livro: ")
livro["ano"] = input("Digite o ano de lançamento do livro: ")
livro["numero_paginas"] = input("Digite o numero de páginas do livro: ")

print("____________________")
print("Informações do livro:")
print("____________________")
print(f"Título: {livro['titulo']}")
print(f"Autor: {livro['autor']}")
print(f"Ano: {livro['ano']}")
print(f"Número de Páginas: {livro['numero_paginas']}")
