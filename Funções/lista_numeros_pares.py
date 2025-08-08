numero = input("Digite os números separados por espaço: ").split()

pares = filter(lambda x: int(x) % 2 == 0, numero)
print(f"Os numeros pares são:", " ".join(pares))
