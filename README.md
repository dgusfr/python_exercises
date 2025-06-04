

## Exercícios

1. Leia três números inteiros, calcule a média aritmética simples e informe se cada número está abaixo, acima ou exatamente na média, apresentando os resultados em uma única linha organizada.

2. Solicite o valor de um investimento inicial, a taxa de juros anual e o número de anos, então calcule e mostre o montante anual acumulado usando juros compostos, imprimindo uma linha para cada ano com o saldo atualizado.

3. Receba a data de nascimento de uma pessoa no formato DD/MM/AAAA e a data atual, calcule a idade exata em anos, meses e dias e exiba a mensagem em uma única sentença clara.

4. Leia um inteiro de 0 a 999 999, converta-o em texto por extenso (sem acentos) e informe também quantos algarismos o compõem.

5. Peça ao usuário o raio e a altura de um cilindro, calcule volume e área total e explique, na mesma linha, se a área é maior que, menor que ou igual ao dobro do volume.

6. Implemente um verificador de CPF que leia uma string, normalize-a removendo caracteres não numéricos, calcule os dígitos verificadores e diga se o CPF informado é válido ou qual seria o CPF corrigido.

7. Solicite um valor monetário em reais e apresente a quantidade mínima de cédulas e moedas necessárias, usando notas de 200, 100, 50, 20, 10, 5 e 2 e moedas de 1, 0,50, 0,25, 0,10, 0,05 e 0,01, separadas apenas por vírgulas.

8. Receba dois horários no formato HH\:MM\:SS, calcule a diferença absoluta entre eles em horas, minutos e segundos e mostre o resultado em frase única.

9. Peça ao usuário uma palavra e uma letra, conte quantas vezes a letra aparece, informe as posições onde ocorre e mostre a palavra com essas letras em maiúsculas no mesmo output.

10. Crie um programa que leia vários números até que o usuário digite “fim”; ao final informe a soma total, a média, o maior, o menor e a quantidade de valores, tudo em um único parágrafo.

11. Gere a sequência de Fibonacci até ultrapassar 10 000, armazene-a em lista, e exiba quantos termos foram gerados, qual o maior termo e a soma de todos eles.

12. Leia um número inteiro positivo e informe se ele é perfeito, abundante ou deficiente, explicando o critério na mesma sentença de saída.

13. Escreva um algoritmo que construa o Triângulo de Floyd para N linhas (fornecido pelo usuário) e represente o triângulo completo em uma única string multiline sem usar loops aninhados explícitos.

14. Implemente uma função que ordene uma lista de tuplas (nome, nota) por nota descendente e, em caso de empate, por nome ascendente; depois peça dez entradas ao usuário, aplique a função e mostre o ranking final em uma linha.

15. Faça um simulador de lançamento de dois dados que execute 1 000 jogadas, registre as somas obtidas em um dicionário de frequências e mostre o par valor–frequência mais recorrente.

16. Crie um gerador (yield) que, dado um número N, produza todos os números primos menores que N; então leia N, consuma o gerador e mostre quantos primos foram gerados e qual o maior deles.

17. Solicite uma frase, remova pontuação e acentuação, e verifique se é um palíndromo; caso seja, mostre “palíndromo perfeito”, caso contrário exiba a frase invertida e o índice da primeira divergência.

18. Desenvolva uma calculadora de frações que leia duas frações no formato a/b, peça a operação (+, −, \*, /) e devolva o resultado simplificado juntamente com a fração mista, se houver.

19. Implemente um sistema de login simples que leia usuário e senha, verifique-os em um dicionário pré-definido e registre tentativas incorretas em um arquivo .log, avisando o usuário apenas após três erros consecutivos.

20. Crie uma função recursiva que calcule o fatorial, mas utilize memoização com um dicionário global para evitar recomputações e mostre o conteúdo do cache após a chamada principal.

21. Leia um número inteiro positivo e identifique o par de números amigos imediatamente anterior e posterior a ele (se existirem), exibindo-os em frase única.

22. Peça ao usuário um texto grande, substitua todas as ocorrências de datas DD/MM/AAAA por AAAA-MM-DD usando expressão regular e indique quantas substituições foram feitas.

23. Implemente uma função que receba um número inteiro e devolva uma lista com sua representação em base binária, octal e hexadecimal, todas sem prefixos.

24. Crie um script que aceite, via linha de comando (argparse), um arquivo CSV contendo nomes e idades, calcule a média de idades e imprima “Arquivo X ok: média Y” ou mensagem de erro caso o arquivo não exista.

25. Escreva uma classe ContaBancaria com métodos depositar, sacar e transferir e atributos protegidos saldo e titular; crie dois objetos, realize algumas operações e imprima um extrato resumido final.

26. Crie uma subclasse ContaPoupanca que herde de ContaBancaria, aplique juros mensais em método próprio e demonstre o efeito após doze meses, exibindo saldo inicial e final.

27. Desenvolva um gerenciador de contexto (with) chamado temporizador que meça o tempo de execução de um bloco de código e imprima “Executado em X,YYY s” ao sair do contexto.

28. Implemente uma classe Data que suporte operadores de comparação (<, >, ==) baseados em dia, mês e ano e permita incremento de um dia usando o operador +=; demonstre comparações e incrementos.

29. Crie uma função decoradora que registre, em JSON, o nome da função decorada, os argumentos recebidos e o timestamp de execução; aplique a deco­radora a duas funções de sua escolha e mostre o arquivo gerado.

30. Utilize o módulo threading para disparar simultaneamente três tarefas que imprimam “tarefa N iniciada” e “tarefa N concluída” com sleep aleatório; sincronize a conclusão usando join e avise quando todas finalizarem.

31. Reescreva o exercício anterior usando asyncio e corrotinas, garantindo que o relatório final indique qual abordagem (threads ou async) concluiu primeiro.

32. Escreva um analisador de logs Apache que leia um arquivo access.log, conte requisições por código de status HTTP e exiba o top 3 em frase contínua.

33. Implemente uma API REST mínima com Flask que possua endpoints GET /itens, POST /itens e DELETE /itens/<id>, armazene dados em memória e exiba um resumo das rotas disponíveis quando executada.

34. Adapte a API anterior para usar SQLite via SQLAlchemy, criando automaticamente a tabela Item se não existir e retornando JSON detalhado das operações.

35. Crie testes unitários usando pytest para os endpoints da API SQLAlchemy, verificando códigos de resposta e conteúdo JSON, e informe a cobertura de testes ao final.

36. Desenvolva um script que faça requisição GET a uma API pública de cotação de moedas, converta um valor de BRL para USD e EUR e exiba as três quantias em um único parágrafo.

37. Escreva um programa que gere um arquivo Excel (.xlsx) contendo três colunas: número, quadrado e cubo para valores de 1 a 50, salvando o arquivo como tabela-potencias.xlsx e confirmando a criação.

38. Implemente uma classe Pessoa com nome e idade e uma propriedade calculada chamada categoria que retorna “menor”, “adulto” ou “idoso”; leia cinco pessoas, armazene-as em lista e mostre quantas caem em cada categoria.

39. Crie um script que leia um arquivo de configuração INI, aplique-lhe uma atualização de chave solicitada pelo usuário e grave o arquivo atualizado, indicando sucesso ou falha.

40. Leia um diretório informado na linha de comando e gere um relatório CSV com caminho completo, tamanho em bytes e data de modificação de cada arquivo, ignorando subdiretórios ocultos.

41. Faça um validador de senha que exija no mínimo 8 caracteres, uma letra maiúscula, uma minúscula, um número e um símbolo; informe ao usuário quais requisitos ainda faltam até a senha ser aceita.

42. Implemente um algoritmo que encontre o menor caminho entre duas cidades usando o algoritmo de Dijkstra em um grafo não dirigido lido de um JSON de distâncias e mostre o trajeto calculado.

43. Crie um compress-decompress simples: leia um texto, comprima-o usando zlib, mostre o tamanho original e comprimido e depois descomprima confirmando integridade.

44. Desenvolva um sistema de votação que registre candidatos em um dicionário, permita votos por número e, ao fim, exiba vencedor, total de votos e percentual de participação.

45. Implemente um crawler que visite uma URL inicial, siga até 30 links internos distintos, colete títulos das páginas e salve em arquivo HTML com uma lista de links e títulos.

46. Crie uma classe Vetor2D com operações de soma, subtração, produto escalar e módulo, suportando operadores +, − e \*. Demonstre as operações com dois vetores lidos do usuário.

47. Construa um script que converta arquivos Markdown de um diretório em HTML usando a biblioteca markdown, salvando cada arquivo com o mesmo nome e extensão .html, e indique quantos foram convertidos.

48. Desenvolva um analisador sintático simples que leia expressões matemáticas contendo +, −, \*, / e parênteses, converta-as para árvore de expressão e avalie o resultado, exibindo a forma pós-fixa e o valor numérico.

49. Implemente um simulador de fila de atendimento usando a classe Queue do módulo queue, com threads produtoras que geram senhas e consumidoras que atendem, mostrando tempo médio de espera.

50. Crie um jogo texto-baseado “Aventuras no Castelo” com classes Sala, Item e Jogador, permitindo mover-se entre salas, pegar itens, salvar e carregar o estado em arquivo JSON e exibindo a conclusão quando o jogador encontrar o tesouro final.


## Autor

Desenvolvido por Diego Franco

