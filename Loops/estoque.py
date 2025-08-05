estoque = 5

while estoque > 0:
    estoque -= 1
    print(f"Venda realizads! Estoque restante: {estoque}")
    if estoque == 0:
        print("Estoque esgotado")
