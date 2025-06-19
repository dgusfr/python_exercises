idade = int(input("Digite sua idade:"))

def classificar_idade(idade):
  if idade < 12:
    print("Você é uma criança.")
  elif 12 <= idade < 17:
    print("Você é um adolecente.")
  elif 17 <= idade < 60:
    print("Você é um adulto.")
  else:
    print("Você é um idoso.")


classificar_idade(idade)