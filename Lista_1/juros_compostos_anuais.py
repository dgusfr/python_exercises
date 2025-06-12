valor_inicial = float(input("Digite o valor inicial: "))
taxa_de_juros = float(input("Digite a taxa de juros anual (em %): "))
tempo_em_anos =  int(input("Digite o tempo em anos que o valor ficará aplicado: "))

ano_atual = 1
while ano_atual <= tempo_em_anos:
  valor_final = valor_inicial * (1 + taxa_de_juros / 100) ** ano_atual
  print(f"Montante acumulado no ano {ano_atual}: R$ {valor_final:.2f}")
  ano_atual += 1