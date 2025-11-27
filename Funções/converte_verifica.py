telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]


def converte(telefones):
    telefones_inteiros = []

    for telefone in telefones:
        telefones_inteiros.append(int(telefone))

    verifica(telefones_inteiros)


def verifica(telefones_inteiros):
    for telefone in telefones_inteiros:
        if isinstance(telefone, int):
            print(f"O telefone {telefone} foi convertido com sucesso.")
        else:
            print(f"A conversão não foi totalmente bem sucedida.")


converte(telefones)
