'''
Defina um dicionário que armazene informações sobre uma pessoa (nome, idade e cidade). Acesse o valor correspondente à chave idade e atualize o valor para um número diferente.
'''

pessoa = {
  "nome": "Diego",
  "idade": "27",
  "cidade": "São Paulo"
}

print(pessoa["idade"])
pessoa["idade"] = 28
print("A pessoa fez aniversário, a nova idade:", pessoa["idade"])