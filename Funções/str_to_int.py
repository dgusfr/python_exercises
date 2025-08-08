entrada = input("Digite os valores das vendas: ").split()

print(sum((map(lambda x: int(x), entrada))))
