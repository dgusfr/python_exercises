hora_atual = int(input("Digite a hora atual (0-23):"))

if hora_atual < 12:
    print("Bom dia")
if 12 < hora_atual < 18:
    print("Bom tarde")
if 18 < hora_atual:
    print("Bom noite")
