"""Crie uma função que receba uma lista de coordenadas em um plano cartesiano, 
onde cada ponto é representado como uma tupla (x, y). 
A função deve calcular a distância entre dois pontos consecutivos usando a fórmula 
da distância euclidiana. Exiba a maior distância entre dois pontos consecutivos 
e o total da soma das distâncias. 
"""
import math

coordenadas = [(4, 5),(3, 2),(6, 7),(1 ,9)]
maior_distancia  = 0
soma_dist = 0

for i in range(len(coordenadas) - 1):
  p1 = coordenadas[i]
  p2 = coordenadas[i + 1]

  d = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
  soma_dist = soma_dist + d

  if d > maior_distancia:
    maior_distancia = d
  
print("A maior distancia é", maior_distancia)
print("A soma das distancia é", soma_dist)
