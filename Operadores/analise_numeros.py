num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > 0 and num2 > 0 and (num1 > 10 or num2 > 10):
    print("Ambos os números são positivos e pelo menos um é maior que 10.")
else:
    print("Os números não atendem às condições.")