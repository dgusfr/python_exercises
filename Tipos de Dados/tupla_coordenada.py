'''Crie uma tupla com 4 coordenadas (números de ponto flutuante) e mostre o valor do segundo item da tupla.'''.encode
import math

coordenada = [(10.5, 22.3), (61.3, 1.456), (12.1, 42.4)]
print(coordenada)

ponto_um = pow((coordenada[2] - coordenada[0]), 2)
ponto_dois = pow((coordenada[3] - coordenada[1]), 2)

distancia = math.sqrt(ponto_um + ponto_dois)
print(distancia)
