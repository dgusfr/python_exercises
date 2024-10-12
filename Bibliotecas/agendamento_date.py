from datetime import datetime

data_do_compromisso = datetime.strptime(input("Digite a data e hora (formato: DD/MM/AAAA HH:MM): "), "%d/%m/%Y %H:%M")

data_de_hoje = datetime.now()

if data_do_compromisso < data_de_hoje:
    print("Erro: O compromisso está marcado para uma data anterior à atual.")
else:
    tempo_restante = data_do_compromisso - data_de_hoje
    print(f"Faltam {tempo_restante} para o compromisso.")
