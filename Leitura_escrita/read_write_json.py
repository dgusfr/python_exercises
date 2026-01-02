import json

dados = {"nome": "Ana", "idade": 32, "enderecos": ["Endereco A", "Endereco B"]}

with open("dados.json", "w") as f:
    json.dump(dados, f)

with open("dados.json", "r") as f:
    dados_lidos = json.load(f)
    print(dados_lidos)
