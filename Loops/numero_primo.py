while True:
    limite = int(input("Digite o limite até onde deseja encontrar números primos: "))

    numero = 2  
    while numero <= limite:
        total_divisoes = 0
        primo = True  

        for i in range(2, int(numero**0.5) + 1):
            total_divisoes += 1
            if numero % i == 0:
                primo = False
                break  

        if primo:
            print(f"{numero} é primo. Divisões realizadas: {total_divisoes}")
        else:
            print(f"{numero} não é primo. Divisões realizadas: {total_divisoes}")

        numero += 1

    continuar = input("Deseja continuar buscando mais números primos? (s/n): ").lower()
    if continuar != 's':
        print("Busca por números primos encerrada.")
        break
