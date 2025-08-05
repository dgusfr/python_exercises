renda = float(input("Digite sua renda:"))
parcela = float(input("Digite a parcela desejada: "))

if renda > 2000 and parcela < (0.3 * renda):
    print("Emprestimo aprovado")
else:
    print("Emprestimo negado: parcela acima de 30% da renda")
