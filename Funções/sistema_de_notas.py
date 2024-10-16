alunos = []

def adicionar_alunos():
  cond = True
  while cond:
    nome = input("Nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    aluno = {
      "nome": nome,
      "notas": [nota1, nota2, nota3]
    }
    
    alunos.append(aluno)

    continuar = input("Deseja adicionar mais alunos? (s/n): ")
    if continuar.lower() != 's':
        cond = False

def imprime_boletim_turma():
  if not alunos:
    print("O Boletim está vazio.")
    return
    
  print("Boletim da Turma:")
  for aluno in alunos:
    print(f"Nome: {aluno['nome']}")
    print(f"Notas: {aluno['notas']}")

def calcular_media():
  for aluno in alunos:
    print(f"Nome: {aluno['nome']}")
    print(f"Notas: {aluno['notas']}")
    media = sum(aluno['notas']) / 3
    aluno['media'] = media
    print(f"Média do aluno {aluno['nome']} é {media:.2f}")

def classifica_aluno():
  for aluno in alunos:
     if 'media' not in aluno:
        print("É necessário calcular as médias antes de classificar.")
        return  # Sai da função se a média não estiver calculada

  alunos.sort(key=lambda aluno: aluno['media'], reverse=True)

  print("\nRanking dos Alunos:")
  for aluno in alunos:
    print(f"Nome: {aluno['nome']}, Média: {aluno['media']:.2f}")

def sistema_de_notas():
        while True:
            print("\n=== Sistema de Notas ===")
            print("1. Adicionar Aluno")
            print("2. Média das notas")
            print("3. Ranking")
            print("4. Exibir Boletim")
            print("5. Sair")
            
            try:
                opcao = int(input("Escolha uma opção: "))
            except ValueError:
                print("Opção inválida. Digite um número inteiro.")
                continue

            match opcao:
                case 1:
                    adicionar_alunos()
                case 2:
                    calcular_media()
                case 3:
                    classifica_aluno()
                case 4:
                    imprime_boletim_turma()
                case 5:
                    print("Saindo do sistema...")
                    break
                case _:
                    print("Opção inválida, tente novamente.")

sistema_de_notas()
