lista_nomes = []

for i in range(5):
  nome = input(f"Digite o {i} nome: ")
  lista_nomes.append(nome)

lista_nomes.sort()

print("Lista de nomes ordenada:")
for nome in lista_nomes:
  print(nome)