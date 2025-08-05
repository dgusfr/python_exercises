maca = int(input("Qual a quantidade de maças vendidas:"))
banana = int(input("Qual a quantidade de bananas vendidas:"))

if banana > maca:
    print("As Bananas tiveram mais vendas")
elif maca > banana:
    print("As maças tiveram mais vendas")
else:
    print("A quantidade de vendas de maças e bananas foram as mesmas")
