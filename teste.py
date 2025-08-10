produtos = [
    ["Arroz", 5.99, 30],
    ["Feijão", 8.49, 20],
    ["Macarrão", 4.79, 50],
    ["Óleo", 7.89, 15],
    ["Açúcar", 3.99, 40],
    ["Sal", 2.49, 100],
    ["Café", 14.99, 10],
    ["Leite", 6.49, 25],
]

precos = []

for produto in produtos:
    precos.append(produto[1])


print(precos)
