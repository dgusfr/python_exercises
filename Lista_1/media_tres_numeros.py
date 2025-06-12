num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))


media = (num1 + num2 + num3) / 3

def comparar_media(num):
    if num > media:
        return "Acima da média"
    elif num < media:
        return "Abaixo da média"
    else:
        return "Igual a média"
    
print(f"A média é {media}")
print(f"O primeiro número é {num1} e está {comparar_media(num1)}")
print(f"O segundo número é {num2} e está {comparar_media(num2)}")
print(f"O terceiro número é {num3} e está {comparar_media(num3)}")


