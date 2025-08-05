contagem = 10

while contagem > 0:
    if contagem % 2 == 0:
        print(f"Faltam apenas {contagem} segundos - Não perca essa oportunidade!")
    else:
        print(f"A contagem continua: {contagem} segundos restantes.")
    contagem -= 1

print("Aproveite a promoção agora!")
