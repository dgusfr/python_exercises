import json

dados = {"nome": "Ana", "idade": 32, "enderecos": ["Endereço A", "Endereço B"]}

with open("dados.json", "r") as f:
    dados_lidos = json.load(f)
    print(dados_lidos)
