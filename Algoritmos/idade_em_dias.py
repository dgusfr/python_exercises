print("Preencha com a data do seu nascimento:")
dia_nascimento = int(input("Dia:"))
mes_nascimento = int(input("Mês:"))
ano_nascimento = int(input("Ano:"))

print("Preencha com a data de hoje:")
dia_atual = int(input("Dia:"))
mes_atual= int(input("Mês:"))
ano_atual = int(input("Ano:"))

ano_em_dias = (ano_atual - ano_nascimento) * 365
mes_em_dias = (mes_atual - mes_nascimento) * 30

if mes_atual < mes_nascimento or (mes_atual == mes_nascimento and dia_atual < dia_nascimento):
  ano_em_dias -= 1


dias = (dia_atual - dia_nascimento)

idade_em_dias = ano_em_dias + mes_em_dias + dias
print(f"A sua idade em dias é:", idade_em_dias)