def somar_numeros(numeros):
  soma = 0
  for numero in numeros:
    soma = soma + numero
  return soma

lista_de_numeros = [1, 2, 4, 6, 8]
resultado = somar_numeros(lista_de_numeros)

print(resultado)
 