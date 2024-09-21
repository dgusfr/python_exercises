inventario = {}
''' inventario = {
    "Nome": {
        "preco": 0.00,
        "quantidade": 0
    }
}'''

def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input(f"Digite o preço unitário de {nome}: R$ "))
    quantidade = int(input(f"Digite a quantidade em estoque de {nome}: "))
    inventario[nome] = {'preco': preco, 'quantidade': quantidade}

def listar_inventario():
    if not inventario:
        print("O inventário está vazio.")
        return
    
    print("\nInventário:")
    for nome, dados in inventario.items():
        print(f"{nome} \n - Preço: R$ {dados['preco']:.2f} - Quantidade: {dados['quantidade']} unidades")
    print()

def remover_produto():
    nome_do_produto = input("Qual o nome do produto a ser removido?")
    if nome_do_produto in inventario:
        del inventario[nome_do_produto]
    else:
        print("Produto a ser excluido não foi encontrado")

def gerar_relatorio():
    if not inventario:
        print("O inventário está vazio.")
        return

    valor_total_estoque = 0
    print("\nRelatório de Estoque:")
    print("--------------------")
    for nome, valores in inventario.items():
        valor_produto = valores["preco"] * valores["quantidade"]
        valor_total_estoque += valor_produto
        print(f"Produto: {nome}:")
        print(f" - Valor total: R$ {valor_produto:.2f}")
    
    print(f"\nValor total do estoque é: R$ {valor_total_estoque:.2f}")

def sistema_de_inventario():
    while True:
        print("\n=== Sistema de Inventário ===")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Listar Produtos")
        print("4. Gerar Relatório de Estoque")
        print("5. Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Digite um número inteiro.")
            continue

        match opcao:
            case 1:
                adicionar_produto()
            case 2:
                remover_produto()
            case 3:
                listar_inventario()
            case 4:
                gerar_relatorio()
            case 5:
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida, tente novamente.")
    
sistema_de_inventario()
