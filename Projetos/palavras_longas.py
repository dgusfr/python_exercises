"""
Crie um codigo em python que receba um texto do usuário e exiba todas as palavras com mais de 10 letras. Se nenhuma for encontrada, exiba "Nenhuma palavra longa foi encontrada no texto.".

Exemplo de entrada:
Digite um texto: A programação estruturada facilitou o desenvolvimento de grandes sistemas computacionais
Saída: Palavras longas encontradas: programação, estruturada, desenvolvimento, computacionais
"""

texto = input("Digite um texto: ")
palavras_longas = []


def conta_palavras(texto):

    for palavra in texto.split():
        if len(palavra) >= 10:
            palavras_longas.append(palavra)

    if palavras_longas:
        print("Palavras longas encontradas: ", end="")
        for palavra in palavras_longas:
            print(f"{palavra}, ", end="")
    else:
        print("Nenhuma palavra longa foi encontrada no texto.")


conta_palavras(texto)
