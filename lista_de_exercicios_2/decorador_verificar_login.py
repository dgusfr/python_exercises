"""
Implemente um decorador `@verificar_login` que só executa a função se o usuário estiver autenticado (`usuario_autenticado = True`). Caso contrário, exiba "Acesso negado".
"""

usuario_autenticado = False


def verificar_login(func):
    def wrapper(*args, **kwargs):
        if usuario_autenticado:
            return func(*args, **kwargs)
        else:
            print("Acesso negado")

    return wrapper


@verificar_login
def funcao_protegida():
    print("Função protegida executada com sucesso!")


# Testando o decorador
if __name__ == "__main__":
    funcao_protegida()  # Deve exibir "Acesso negado"

    usuario_autenticado = True  # Simulando autenticação
    funcao_protegida()  # Deve exibir "Função protegida executada com sucesso!"
