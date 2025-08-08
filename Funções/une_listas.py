produto = input("Digite os produtos separados por vírgula: ").split(
    ","
)  # maçã, banana, pera
preco = input("Digite os preços separados por vírgula: ").split(",")  # 2.5, 1.2, 3.0

for prod, pre in zip(produto, preco):
    print(f"{prod.strip()} : {pre.strip()}")
