n = int(input("Digite um número: "))
soma = 0

for i in range(1, n + 1):
    soma += i
    if i < n:
        print(f"{i} + ", end="")
    else:
        print(f"{i} = {soma}")
