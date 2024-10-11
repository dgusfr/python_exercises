valor_da_compra = float(input("Digite o valor total da compra:"))
numero_de_parcelas = int(input("Digite o numero de parcelas:"))

if numero_de_parcelas >= 6:
  valor_da_compra = valor_da_compra + (valor_da_compra * 0.02)
  valor_da_parcela = valor_da_compra / numero_de_parcelas
  print(f"{numero_de_parcelas}x: R$ {valor_da_parcela}")
else:
  valor_da_parcela = valor_da_compra / numero_de_parcelas
  print(f"{numero_de_parcelas}x: R$ {valor_da_parcela}")


