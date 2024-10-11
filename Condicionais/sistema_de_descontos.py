valor_total_compra = float(input("Digite o valor total da compra:"))
valor_com_desconto = 0

if valor_total_compra >= 1000:
  valor_com_desconto = valor_total_compra - (valor_total_compra * 0.1)
elif 500 <= valor_total_compra < 1000:
  valor_com_desconto = valor_total_compra - (valor_total_compra * 0.05)
else:
  print("Sem descontos aplicáveis")
  