numero = int(input("Digite um numeor entre 1 à 7:"))

dias_semana = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado"
}

if (1<= numero <= 7):
  print(f"O dia da semana correspondente ao {numero} é {dias_semana[numero]}")
else:
  print("Número inválido! Por favor, insira um número entre 1 e 7.")