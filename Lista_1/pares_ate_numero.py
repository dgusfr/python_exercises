"""
Solicite um número inteiro positivo e use um laço `for` para imprimir todos os números pares de 0 até esse número, inclusive.
"""

numero = int(input("Digite um numero inteiro positivo:"))
if numero < 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    print(f"Os numeros pares de 0 até{numero} são:")
    for i in range(0, numero + 1, 2):
        print(i, end='  ')
    print()  

        
