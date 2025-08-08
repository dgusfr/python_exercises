telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]


def converte_para_inteiro(lista_telefones):
    telefones_convertidos = []

    for telefone in lista_telefones:
        telefones_convertidos.append(int(telefone))

    verifica_tipo(telefones_convertidos)


def verifica_tipo(lista_telefones):
    for telefone in lista_telefones:
        if isinstance(telefone, int):
            print(f"✓ Telefone {telefone} é um inteiro válido")
        else:
            print(f"✗ Erro: {telefone} não é um inteiro")


converte_para_inteiro(telefones)
