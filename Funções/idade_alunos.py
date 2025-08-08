nascimento = int(input("Digite o ano de nascimento:  "))
ano_atual = int(input("Digite o ano atual: "))


def calcula_idade(nascimento, ano_atual):
    if ano_atual < nascimento:
        print("Digite as datas corretas")
    else:
        idade = ano_atual - nascimento
        print(f"O aluno tem {idade} anos ")


calcula_idade(nascimento, ano_atual)
