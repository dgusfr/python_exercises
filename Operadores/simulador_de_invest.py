sair = True
capitalizacao = input("O periodo de capitalização será em meses ou anos? (Digite: mes ou anos ou sair)")

while sair == True:
  if capitalizacao.lower() == 'mês':
    valor_presente = float(input("Digiote o valor presente a ser aplicado:"))
    taxa = float(input("Digite a taxa a ser aplicada:"))
    tempo = int(input("Digite o tempo que será aplicado o valor (Em meses)"))
    valor_final = (valor_presente * ((1 + (taxa/ 12)) ** ( 12 * tempo )))
  elif capitalizacao.lower() == 'anos':
    valor_presente = float(input("Digiote o valor presente a ser aplicado:"))
    taxa = float(input("Digite a taxa a ser aplicada:"))
    tempo = int(input("Digite o tempo que será aplicado o valor (Em meses)"))
    valor_final = (valor_presente * ((1 + (taxa/ 1)) ** ( 1 * tempo )))
  else:
    sair == False

    
