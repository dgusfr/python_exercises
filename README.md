# Python

## Sumário

1. [Tipagem](#tipagem)
   - [Correção na Interpretação dos Dados](#correção-na-interpretação-dos-dados)
   - [Alocação Eficiente de Memória](#alocação-eficiente-de-memória)
   - [Operações Corretas em Variáveis](#operações-corretas-em-variáveis)
2. [Variáveis](#variáveis)
   - [Criando Variáveis](#criando-variáveis)
   - [Atribuição e Referência](#atribuição-e-referência)
   - [Tipagem Dinâmica](#tipagem-dinâmica)
   - [Conversão de Tipos (Casting)](#conversão-de-tipos-casting)
   - [Obtendo o Tipo de uma Variável](#obtendo-o-tipo-de-uma-variável)
   - [Sensibilidade a Maiúsculas e Minúsculas](#sensibilidade-a-maiúsculas-e-minúsculas)
3. [Tipos de Dados](#tipos-de-dados)
   - [Inteiros (int)](#inteiros-int)
   - [Ponto Flutuante (float)](#ponto-flutuante-float)
   - [Precisão de Ponto Flutuante](#precisão-de-ponto-flutuante)
   - [Strings (str)](#strings-str)
   - [Métodos Comuns de String](#métodos-comuns-de-string)
   - [Índices e Fatiamento](#índices-e-fatiamento)
   - [Booleanos (bool)](#booleanos-bool)
4. [Tipos Mutáveis e Imutáveis](#tipos-mutáveis-e-imutáveis)
5. [Gerenciadores de Pacotes e Ambientes Virtuais](#gerenciadores-de-pacotes-e-ambientes-virtuais)
   - [PIP e PyPI](#pip-e-pypi)
   - [Ambientes Virtuais](#ambientes-virtuais)
   - [Pipenv](#pipenv)
6. [Estruturas Condicionais](#estruturas-condicionais)
   - [If](#if)
   - [Elif e Else](#elif-e-else)
7. [Operadores](#operadores)
   - [Aritméticos](#aritméticos)
   - [Relacionais](#relacionais)
   - [Lógicos](#lógicos)
8. [Estruturas de Repetição (Loops)](#estruturas-de-repetição-loops)
   - [Loop For](#loop-for)
   - [Loop While](#loop-while)
9. [Exceções (Exceptions)](#exceções-exceptions)
   - [Tratamento de Exceções](#tratamento-de-exceções)
   - [Levantando Exceções](#levantando-exceções)
10. [Bibliotecas Integradas](#bibliotecas-integradas)
    - [datetime](#datetime)
    - [random](#random)
    - [os](#os)
    - [sys](#sys)
    - [math](#math)
    - [re (Expressões Regulares)](#re-expressões-regulares)
11. [Funções](#funções)
    - [Definição de Funções](#definição-de-funções)
    - [Funções Lambda](#funções-lambda)
    - [Funções Recursivas](#funções-recursivas)
    - [Função main()](#função-main)
12. [Exercícios](#12-exercícios)
    - [Inventário](#inventário)
    - [Sistema de Notas](#sistema-de-notas)
    - [Controle de Tráfego](#controle-de-tráfego)
    - [Simulador de Investimentos](#simulador-de-investimentos)
    - [Gerador de Números Primos](#gerador-de-números-primos)
    - [Jogo de Adivinhação](#jogo-de-adivinhação)
    - [Sistema de Agendamento](#sistema-de-agendamento)
    - [Ranking de Alunos](#ranking-de-alunos)
    - [Cálculo de Fibonacci](#cálculo-de-fibonacci)
    - [Manipulação de Strings](#manipulação-de-strings)
13. [Autor](#autor)

...

# Fundamentos

## Introdução à Computação

Todo programa computacional exige dois recursos principais: **processamento** e **memória**.

- **Processamento** refere-se à capacidade do sistema de executar instruções, como cálculos, manipulação de dados e controle de fluxo.
- **Memória** é onde os dados são armazenados temporariamente para serem acessados e manipulados durante a execução do programa.

Em Python, assim como em outras linguagens de programação, a memória é um recurso fundamental que precisa ser gerido com eficiência para garantir que os programas funcionem corretamente e sem desperdícios.

<br></br>

## Alocação de Memória

A alocação de memória é o processo pelo qual o sistema operacional reserva espaço na memória RAM para que os programas possam armazenar e acessar dados. Em Python, esse processo é **gerenciado automaticamente** pelo interpretador, mas entender como a memória é alocada e gerida pode ajudar a escrever programas mais eficientes.

### Memória RAM

É a memória de acesso rápido onde os dados são temporariamente armazenados enquanto o programa está sendo executado.

### Heap e Stack

A memória em Python pode ser dividida entre:

- **Heap**: onde os objetos dinâmicos são armazenados.
- **Stack**: onde as variáveis locais e as chamadas de função são geridas.

## Variáveis e Atribuição de Memória

Uma variável em Python é um **identificador** que aponta para um valor armazenado na memória. Diferente de linguagens de programação que exigem a declaração explícita do tipo de variável (como `int`, `float`, `char`), Python é uma linguagem de **tipagem dinâmica**, ou seja, o tipo da variável é determinado automaticamente pelo valor atribuído a ela.

### Componentes de uma Variável

- **Identificador**: Nome da variável (ex: `a` em `a = 5`).
- **Valor**: O dado associado à variável (ex: `5` em `a = 5`).
- **Endereço de Memória**: Local onde o valor é armazenado.

### Como Funciona a Atribuição em Python?

Quando você atribui um valor a uma variável, o interpretador aloca espaço na memória para armazenar esse valor.

```python
# Exemplo:
a = 5
b = 7
c = a + b
```

| Endereço | Conteúdo | Variável |
|----------|---------|----------|
| 12350    | 5       | a        |
| 12360    | 7       | b        |
| 12370    | 12      | c        |

Outro exemplo:

```python
a = 5
b = 5
```

| Endereço | Conteúdo | Variável |
|----------|---------|----------|
| 12350    | 5       | a        |
| 12350    | 5       | b        |

Python otimiza esse processo apontando `a` e `b` para o mesmo endereço de memória, pois ambos contêm o mesmo valor imutável. Esse é um comportamento conhecido como **interning**.

## Alocação de Memória em Listas

Listas em Python são implementadas como **arrays dinâmicos**, onde a memória é alocada de forma que as listas possam crescer ou diminuir dinamicamente.

Cada elemento de uma lista em Python é um **ponteiro** para um objeto armazenado em outra parte da memória.

```python
numeros = [1, 2, 3, 4, 5]
```

Aqui, `numeros` é uma lista contendo cinco inteiros. Cada inteiro é armazenado em uma posição de memória, e a lista `numeros` contém ponteiros para essas posições.

### Alocação Dinâmica

Python gerencia automaticamente o tamanho da lista. Quando você adiciona um novo item, Python pode **realocar** a lista inteira em um novo bloco de memória maior, se necessário.

## Alocação de Memória em Matrizes (Vetores Bidimensionais)

Matrizes são essencialmente **arrays de arrays**. Em Python, elas são representadas por **listas de listas**.

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Aqui, `matriz` é uma lista que contém três listas, cada uma representando uma linha da matriz. Cada sublista é armazenada em uma posição de memória, e a lista `matriz` contém ponteiros para essas sublistas.

A alocação de memória funciona de maneira semelhante à das listas simples, mas agora com **múltiplas camadas de listas**.

---

<br></br>

# Entrada e Saída de Dados

## A Função `print()`

A função `print()` exibe dados na tela. Ela é usada para mostrar resultados e mensagens no console.

### Exemplo básico:

```python
print("Olá, mundo!")  # Exibe "Olá, mundo!"
```

### Parâmetros importantes da função `print()`:

#### 1. `sep` (separador)

Define o separador entre os valores passados para `print()`. Por padrão, é um espaço (`" "`), mas pode ser alterado.

```python
print("Python", "é", "incrível", sep="-")
# Saída: Python-é-incrível
```

#### 2. `end` (final da linha)

Define o que será exibido ao final da linha. O valor padrão é `"\n"` (nova linha), mas pode ser alterado para continuar imprimindo na mesma linha.

```python
print("Olá", end="!")
print("Mundo")
# Saída: Olá!Mundo
```

#### 3. Pular linha

Para pular uma linha dentro de uma string, utilize `\n`.

```python
print("Linha 1\nLinha 2\nLinha 3")
```

**Saída:**

```
Linha 1
Linha 2
Linha 3
```

## A Função `input()`

A função `input()` é utilizada para interagir com o usuário, solicitando informações.

```python
entrada = input("Digite algo: ")
```

O que o usuário digitar será capturado como uma **string** e armazenado na variável `entrada`.

### Tratamento da entrada com `int()`, `float()`, etc.

Se o dado inserido precisar ser usado como número, ele deve ser **convertido**.

```python
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura em metros: "))
nome = input("Digite seu nome: ")
```

### Tratamento de Erro com `try-except`

Se o usuário digitar algo inválido, o programa pode gerar um erro. Para evitar isso, usamos `try-except`.

```python
try:
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura em metros: "))
    nome = input("Digite seu nome: ")
    print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}")
except ValueError:
    print("Por favor, insira um número válido para a idade e altura.")
```

---

<br></br>

## Tipagem
A tipagem em programação classifica os diferentes tipos de informações em um programa. Isso é essencial para:

1. **Correção na Interpretação dos Dados**  
   O computador precisa saber o tipo do dado para interpretá-lo corretamente. Exemplo:
   - `01101000` como inteiro pode representar `104`
   - `01101000` como caractere pode ser `'h'`

2. **Alocação Eficiente de Memória**  
   - Um `int` pode ocupar `4 bytes`
   - Um `float` pode ocupar `8 bytes`
   - Uma `string` ocupa espaço variável

3. **Operações Corretas em Variáveis**  
   - Inteiros podem ser somados, subtraídos, multiplicados.
   - Strings podem ser concatenadas, divididas.
   - Operações incompatíveis geram erros (`'texto' + 5` não é válido).

## Variáveis
Uma variável é um espaço na memória onde um valor pode ser armazenado e acessado.

### Criando Variáveis
Python não exige declaração de tipo:
```python
x = 5
y = "John"
print(x)  # 5
print(y)  # John
```

Variáveis podem mudar de tipo:
```python
x = 4      # int
x = "Sally"  # str
print(x)  # Sally
```

### Atribuição e Referência
A atribuição de uma variável a outra não cria uma nova cópia do valor, mas ambas apontam para o mesmo objeto:
```python
a = 3
b = a  # 'b' aponta para o mesmo objeto que 'a'
```

### Tipagem Dinâmica
As variáveis podem mudar de tipo dinamicamente:
```python
x = 4       # int
x = "Sally" # str
print(x)    # Sally
```

### Conversão de Tipos (Casting)
```python
x = str(3)    # '3'
y = int(3)    # 3
z = float(3)  # 3.0
```

### Obtendo o Tipo de uma Variável
```python
x = 5
y = "John"
print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
```

### Sensibilidade a Maiúsculas e Minúsculas
```python
a = 4
A = "Sally"
print(a)  # 4
print(A)  # Sally
```

<br></br>

## Tipos de Dados
Python possui vários tipos de dados integrados:

| Categoria   | Tipo       | Descrição                         |
|------------|-----------|---------------------------------|
| Texto      | `str`      | Sequência de caracteres         |
| Numéricos  | `int`      | Números inteiros                |
|            | `float`    | Números de ponto flutuante      |
|            | `complex`  | Números complexos               |
| Sequência  | `list`     | Coleção ordenada e mutável      |
|            | `tuple`    | Coleção ordenada e imutável     |
|            | `range`    | Sequência de números            |
| Mapeamento | `dict`     | Coleção de pares chave-valor    |
| Conjuntos  | `set`      | Coleção não ordenada, sem duplicatas |
|            | `frozenset`| Semelhante a `set`, mas imutável |
| Booleano   | `bool`     | Representa `True` ou `False`    |
| Binários   | `bytes`    | Sequência imutável de bytes     |
|            | `bytearray`| Sequência mutável de bytes      |
|            | `memoryview`| Acesso a dados binários         |
| Nenhum     | `NoneType` | Representa ausência de valor    |

### Inteiros (`int`)
```python
numero_inteiro = 10
outro_inteiro = -3
resultado = numero_inteiro + outro_inteiro  # 7
print(resultado)
```

### Ponto Flutuante (`float`)
```python
numero_float = 3.14
outro_float = 2.5
resultado = numero_float * outro_float
print(resultado)  # 7.85
```

#### Precisão de Ponto Flutuante
```python
resultado = 0.1 + 0.2
print(resultado)  # 0.30000000000000004
print(round(resultado, 2))  # 0.3
print(f"{resultado:.2f}")  # 0.30
```

### Strings (`str`)
```python
nome = "Diego"
mensagem = "Olá, " + nome + "!"
print(mensagem)  # Olá, Diego!
```

#### Métodos Comuns de String
```python
texto = "Python é incrível"
print(len(texto))        # 17
print(texto.lower())     # python é incrível
print(texto.upper())     # PYTHON É INCRÍVEL
print(texto.strip())     # "Python é incrível"
print(texto.replace("Python", "Programação"))
print(texto.split())     # ['Python', 'é', 'incrível']
```

#### Índices e Fatiamento
```python
texto = "Python"
print(texto[0])      # P
print(texto[2:5])    # tho
print(texto[::-1])   # nohtyP (inverso)
```

### Booleanos (`bool`)
```python
maior_de_idade = True
if maior_de_idade:
    print("Você tem permissão para votar.")
```

## Tipos Mutáveis e Imutáveis

| Tipo         | Mutável? |
|-------------|---------|
| `int`       | Não     |
| `float`     | Não     |
| `str`       | Não     |
| `tuple`     | Não     |
| `list`      | Sim     |
| `dict`      | Sim     |
| `set`       | Sim     |

Exemplo de tipo mutável:
```python
lista = [1, 2, 3]
lista[1] = 10
print(lista)  # [1, 10, 3]
```

Exemplo de tipo imutável:
```python
a = 5
a = 10  # Cria um novo objeto, não altera o original
```

---

<br></br>

# Estruturas Condicionais
Estruturas condicionais permitem tomar decisões com base em condições.

### If
```python
idade = 20
if idade >= 18:
    print("Você é maior de idade.")
```

### Elif e Else
```python
idade = 16
if idade >= 18:
    print("Maior de idade.")
elif idade >= 16:
    print("Pode aprender a dirigir.")
else:
    print("Muito jovem para dirigir.")
```

## Operadores
### Aritméticos
- `+` Adição  
- `-` Subtração  
- `*` Multiplicação  
- `/` Divisão  
- `//` Divisão inteira  
- `%` Módulo  
- `**` Exponenciação  

### Relacionais
- `==` Igualdade  
- `!=` Diferença  
- `>` Maior  
- `<` Menor  
- `>=` Maior ou igual  
- `<=` Menor ou igual  

```python
print(5 > 3)  # True
print(5 == 5)  # True
```

### Lógicos
- `and` Ambas condições verdadeiras  
- `or` Pelo menos uma condição verdadeira  
- `not` Inverte o valor lógico  

```python
print(True and False)  # False
print(True or False)  # True
print(not True)  # False
```

## Estruturas de Repetição (Loops)

### Loop For
```python
for i in range(1, 21):
    print(i, end=' ')
```

### Loop While
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

## Exceções (Exceptions)

### Tratamento de Exceções
```python
try:
    x = int(input("Digite um número: "))
except ValueError:
    print("Erro! Esse não é um número válido.")
```

### Levantando Exceções
```python
def verificar_idade(idade):
    if idade < 18:
        raise ValueError("Idade menor que 18.")
    print("Idade válida.")
```

<br></br>

## Bibliotecas Integradas

### datetime
```python
import datetime
now = datetime.datetime.now()
print(f"Data e Hora Atual: {now}")
```

### random
```python
import random
numero_aleatorio = random.randint(1, 10)
print(f"Número aleatório: {numero_aleatorio}")
```

### os
```python
import os
diretorio_atual = os.getcwd()
print(f"Diretório atual: {diretorio_atual}")
```

### sys
```python
import sys
print(f"Versão do Python: {sys.version}")
```

### math
```python
import math
print(f"Raiz quadrada de 25: {math.sqrt(25)}")
```

### re (Expressões Regulares)
```python
import re
texto = "O email de contato é exemplo@email.com"
padrao = r"\w+@\w+\.\w+"
email = re.search(padrao, texto)
print(f"Email encontrado: {email.group()}")
```

## Funções

### Definição de Funções
```python
def saudar(nome):
    print("Olá, " + nome + "!")
saudar("Diego")
```

### Funções Lambda
```python
soma = lambda a, b: a + b
print(soma(5, 3))
```

### Funções Recursivas
```python
def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n - 1)
print(fatorial(5))
```

### Função main()
```python
def main():
    print("Este é o ponto de entrada do programa.")
if __name__ == "__main__":
    main()
```
---

<br></br>

## **Gerenciadores de Pacotes e Ambientes Virtuais**

### **PIP e PyPI**
O **PIP** instala pacotes do **PyPI**:
```bash
pip install requests
```
Arquivo `requirements.txt`:
```
requests==2.25.1
Flask==1.1.2
```
Instalação em lote:
```bash
pip install -r requirements.txt
```

### **Ambientes Virtuais**
Criando um ambiente:
```bash
virtualenv meu_ambiente
```
Ativando:
```bash
source meu_ambiente/bin/activate  # Linux/macOS
meu_ambiente\Scripts\activate     # Windows
```
Saindo do ambiente:
```bash
deactivate
```

### **Pipenv**
Gerencia ambientes virtuais e dependências.
```bash
pip install pipenv
pipenv install flask
pipenv shell
```
---

## 12. Exercícios

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

