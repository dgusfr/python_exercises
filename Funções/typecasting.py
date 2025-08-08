telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]


def converte_para_inteiro(lista_telefones):
    telefones_convertidos = []

    for telefone in telefones:
        telefones_convertidos.append(int(telefone))

    return telefones_convertidos
