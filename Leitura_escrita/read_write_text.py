with open("dados.txt", "w") as file:
    file.write("Ola, mundo\n")

with open("dados.txt", "r") as file:
    conteudo = file.read()
    print(conteudo)

with open("dados.txt", "a") as file:
    file.write("Ultima linha.\n")
