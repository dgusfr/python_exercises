def determinante_laplace_3x3(matriz):
    if len(matriz) != 3 or any(len(row) != 3 for row in matriz):
        raise ValueError("A matriz deve ser 3x3.")

    # Escolhemos a primeira linha para a expansão de Laplace
    a = matriz[0][0]
    b = matriz[0][1]
    c = matriz[0][2]

    # Calcula os cofatores dos elementos da primeira linha
    cofator_a = (matriz[1][1] * matriz[2][2]) - (matriz[1][2] * matriz[2][1])
    cofator_b = -((matriz[1][0] * matriz[2][2]) - (matriz[1][2] * matriz[2][0]))
    cofator_c = (matriz[1][0] * matriz[2][1]) - (matriz[1][1] * matriz[2][0])

    # O determinante é a soma dos produtos de cada elemento pelo seu cofator
    determinante = (a * cofator_a) + (b * cofator_b) + (c * cofator_c)

    return determinante

# Matriz de exemplo fornecida:
matriz_exemplo = [
    [2, 1, 3],
    [1, 4, 2],
    [-5, -1, -2]
]

try:
    det = determinante_laplace_3x3(matriz_exemplo)
    print(f"O determinante da matriz:")
    for linha in matriz_exemplo:
        print(linha)
    print(f"é: {det}")
except ValueError as e:
    print(f"Erro: {e}")