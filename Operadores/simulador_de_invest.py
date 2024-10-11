sair = True
capitalizacao = input("O periodo de capitalização será em meses ou anos? (Digite: mes ou anos ou sair):\n")

while sair == True:
  if capitalizacao.lower() == 'mes':
    valor_presente = float(input("Digite o valor presente a ser aplicado:"))
    taxa = float(input("Digite a taxa a ser aplicada:"))
    tempo = int(input("Digite o tempo que será aplicado o valor (Em meses):"))
    valor_final = (valor_presente * ((1 + (taxa/ 12)) ** ( 12 * tempo )))
    print(f"O valor final será de: {valor_final} ")
  elif capitalizacao.lower() == 'anos':
    valor_presente = float(input("Digite o valor presente a ser aplicado:"))
    taxa = float(input("Digite a taxa a ser aplicada:"))
    tempo = int(input("Digite o tempo que será aplicado o valor (Em meses):"))
    valor_final = (valor_presente * ((1 + (taxa/ 1)) ** ( 1 * tempo )))
    print(f"O valor final será de: {valor_final} ")
  else:
    sair == False


