numero_de_veiculos = int(input("Quantidade de veiculos que passaram:"))
limite_de_trafego = int(input("Digite o limite de veiculos que podem trafegar:"))
intervalo_de_tempo = float(input("Digite o intervalo de tempo (em horas):"))
media_de_veiculos = 0

if numero_de_veiculos > limite_de_trafego:
  print("Trafego alto")
else:
  print("Trafego normal")
  
media_de_veiculos = numero_de_veiculos / intervalo_de_tempo
print(f"A media de veiculos por hora é:{media_de_veiculos}")
