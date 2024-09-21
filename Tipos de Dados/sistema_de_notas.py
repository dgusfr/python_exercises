"""
Crie uma função que simule um sistema de notas escolares. A função deve receber uma lista de notas, calcular a média e
classificar o aluno de acordo com o resultado:
■ "Aprovado" (média >= 7).
■ "Recuperação" (média entre 5 e 6.9).
■ "Reprovado" (média < 5).
O adicione uma funcionalidade que armazene o nome do aluno e retorne a média e a classificação de cada um.
"""


def adicionar_notas():
    notas = []
    while True:
        entrada = input("Adicione um número (ou digite 'done' para terminar): ")

        if entrada.lower() == "done":
            break

        try:
            nota = float(entrada)
            notas.append(nota)
        except ValueError:
            print("Por favor, insira um número válido.")

    return notas


def calcula_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    print(f"A media das notas informadas é: {media:.2f}")
    classifica_aluno(float(media))


def classifica_aluno(media):
    if media >= 7:
        print("Aluno Aprovado")
    elif 5 <= media < 7:
        print("O aluno esta de recuperação")
    else:
        print("O aluno reprovou")


def sistema_de_notas():
    print("Olá, seja bem-vindo ao sistema de notas\n")
    notas = adicionar_notas()
    if notas:
        calcula_media(notas)
    else:
        print("Nenhuma nota foi adicionada.")


sistema_de_notas()
