peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

IMC = peso / (altura**2)

if IMC < 18.5:
    print("Você esta a baixo do peso. ")
elif 18.5 <= IMC < 25:
    print("Você esta no peso ideal. ")
else:
    print("Você esta acima do peso. ")
