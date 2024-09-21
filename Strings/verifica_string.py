endereco = input("Digite um endereço de site: ")

if endereco.startswith("www"):
    print("O endereço começa com 'www'.")
else:
    print("O endereço NÃO começa com 'www'.")

if endereco.endswith(".com"):
    print("O endereço termina com '.com'.")
else:
    print("O endereço NÃO termina com '.com'.")
