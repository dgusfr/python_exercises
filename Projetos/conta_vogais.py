"""
Crie um codigo em python que peça ao usuário um texto e exiba a quantidade de vogais (a, e, i, o, u) nele contidas, considerando maiúsculas e minúsculas.

Exemplo:
Entrada: A linguagem Python é muito versátil.
Saída: O texto contém 13 vogais.
"""

texto = input("Digite o texto aqui: ")


def calcula_vagais(texto):
    texto = texto.lower()
    vogais = "aeiouáéíóúâêîôûãõ"
    contador = 0

    for letra in texto:
        if letra in vogais:
            contador += 1

    return f"O texto contém {contador} vogais"


print(calcula_vagais(texto))
