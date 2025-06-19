"""
Crie uma função classificar_idade() que recebe a idade como parâmetro e retorna se a pessoa é "criança", "adolescente", "adulto" ou "idoso". Utilize essa função com dados lidos do usuário.
"""

idade = int(input("Digite sua idade:"))

def classificar_idade(idade):
  if idade < 12: