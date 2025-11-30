import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Nome", "Idade", "Cidade"])
    writer.writerow(["Ana", "32", "Sao Paulo"])
    writer.writerow(["Roberto", "45", "Rio de Janeiro"])


with open("data.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
