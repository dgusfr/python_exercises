valor_total_compra = float(input("Digite o valor total da compra:"))

if valor_total_compra >= 1000:
  valor_com_desconto = valor_total_compra - (valor_total_compra * 0.1)
  print(f"O valor com desconto é {valor_com_desconto}")
elif 500 <= valor_total_compra < 1000:
  valor_com_desconto = valor_total_compra - (valor_total_compra * 0.05)
  print(f"O valor com desconto é {valor_com_desconto}")
else:
  print("Sem descontos aplicáveis")
  
