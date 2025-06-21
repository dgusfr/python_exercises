"""
Crie um módulo chamado `utilitarios.py` que contenha uma função `dobrar(numero)` e outra `eh_par(numero)`. Em outro arquivo, importe e use essas funções com valores fornecidos pelo usuário.
"""


def dobrar(numero):
    return numero * 2


def eh_par(numero):
    if numero % 2 == 0:
        return "O numeor é par."
    else:
        return "O numeor é impar."
