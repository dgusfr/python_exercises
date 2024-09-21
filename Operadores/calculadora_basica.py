numero_um = float(input("Digite o primeiro numero:"))
numero_dois = float(input("Digite o segundo numero:"))

soma = numero_um + numero_dois
subtracao = numero_um - numero_dois
multiplicacao = numero_um * numero_dois
divisao = numero_um / numero_dois


print(f"A soma dos numeros é: {soma}\n a subtração: {subtracao}\n a multiplicação: {multiplicacao}\n a divisão: {"%.2f" % divisao}")