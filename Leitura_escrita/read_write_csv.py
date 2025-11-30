import csv

with open("dados.csv", "w") as file:
    author = csv.writer(file)
    author.writerow(["Nome", "Idade", "Cidade"])
    author.writerow(["Nome", "Idade", "Cidade"])
