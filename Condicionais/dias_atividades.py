atv_a = int(input("Informe os dias para a atividade A: "))
atv_b = int(input("Informe os dias para a atividade B: "))
atv_c = int(input("Informe os dias para a atividade C: "))

if atv_a < 0 or atv_b < 0 or atv_c < 0:
    print("Os dias não podem ser negativos")
else:
    tempo_total = atv_a + atv_b + atv_c
    print(f"A quantidade total de dias é: { tempo_total} dias")
