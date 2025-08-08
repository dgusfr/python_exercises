adicao = lambda x, y: x + y
subtracao = lambda x, y: x - y
multiplicacao = lambda x, y: x * y
divisao = lambda x, y: x / y


num_um = int(input("Digite o primeiro número: "))
num_dois = int(input("Digite o segundo número: "))
operacao = input("Escolha a operação (| + | - | * | / |):")

if operacao == "+":
    print(adicao(num_um, num_dois))
elif operacao == "-":
    print(subtracao(num_um, num_dois))
elif operacao == "*":
    print(multiplicacao(num_um, num_dois))
elif operacao == "/":
    print(divisao(num_um, num_dois))
