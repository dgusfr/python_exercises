"""
Crie um dicionário para armazenar dados de um livro: título, autor, ano e número de páginas. Solicite os dados ao usuário e, ao final, exiba o dicionário formatado.
"""

livro = {
  "titulo" :"",
  "autor": "",
  "ano": 0,
  "numero_paginas": 0
}

livro["titulo"] = input("Digite o titulo do livro:")
livro["autor"] = input("Digite o autor do livro:")
livro["ano"] = input("Digite o ano de lançamento do livro:")
livro["numero_paginas"] = input("Digite o numero de páginas do livro:")

