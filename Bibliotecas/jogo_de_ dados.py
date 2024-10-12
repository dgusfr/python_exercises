import random 

soma_sete = 0
soma_onze = 0

for i in range(0, 10000):
  dado_numero_um = random.randint(1, 6)
  dado_numero_dois = random.randint(1, 6)

  if dado_numero_um + dado_numero_dois == 7:
    soma_sete += 1
  elif dado_numero_um + dado_numero_dois == 11:
    soma_onze += 1

print(f"A soma dos dois dados resultaram em 7 {soma_sete} vezes")
print(f"A soma dos dois dados resultaram em 11 {soma_onze} vezes")

probabilidade_de_sete = soma_sete / 10000
probabilidade_de_onze = soma_onze /10000

print(f"A probabilidade da soma dar 7 é {probabilidade_de_sete:.2f} e de dar 11 é {probabilidade_de_onze:.2f}")
