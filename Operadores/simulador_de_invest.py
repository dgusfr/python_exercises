
taxa = float(input("Digite a taxa a ser aplicada:"))
numero_de_capitalizacao = 0
tempo = 0

capitalizacao = input("O periodo de capitalização será em meses ou anos? (Digite: mes ou anos ou sair)")

if capitalizacao.lower() == 'mês':
  valor_presente = float(input("Digiote o valor presente a ser aplicado:"))
  taxa = float(input("Digite a taxa a ser aplicada:"))
  tempo = int(input("Digite o tempo que será aplicado o valor (Em meses)"))
  valor_final = (valor_presente * ((1 + (taxa/ 12)) ** ( 12 * tempo )))