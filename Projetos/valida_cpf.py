"""
Crie um código em Python que peça ao usuário um número de CPF e verifique se ele tem exatamente 11 dígitos e contém apenas números. Se válido, exiba "CPF válido.". Caso contrário, exiba uma mensagem de erro apropriada: "Erro: O CPF deve conter apenas números." (se houver não-dígitos) ou "Erro: O CPF deve ter exatamente 11 dígitos." (se o comprimento for diferente).

Exemplo de entrada válida:
Digite seu CPF: 12345678901
Saída: CPF válido.

Exemplo inválido (não-dígitos):
Digite seu CPF: 1234abc567
Saída: Erro: O CPF deve conter apenas números.

Exemplo inválido (comprimento errado):
Digite seu CPF: 1234567
Saída: Erro: O CPF deve ter exatamente 11 dígitos.
"""


def validar_cpf():
    cpf = input("Digite seu CPF (Sem pontos e traços): ")
    if not cpf.isdigit():
        return "Erro: O CPF deve conter apenas números."
    if len(cpf) != 11:
        return "Erro: O CPF deve ter exatamente 11 dígitos."
    return "CPF válido."


print(validar_cpf())
