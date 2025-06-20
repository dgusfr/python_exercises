# Python

# Sumário Interativo

- [Python Básico](#python-básico)
  - [1. Sintaxe Básica](#1-sintaxe-básica)
  - [2. Entrada e Saída de Dados](#2-entrada-e-saída-de-dados)
  - [3. Variáveis e Tipos de Dados](#3-variáveis-e-tipos-de-dados)
  - [4. Programação com Python: Processamento e Memória](#4-programação-com-python-processamento-e-memória)
    - [Alocação de Memória](#alocação-de-memória)
  - [5. Condicionais](#5-condicionais)
  - [6. Laços de Repetição](#6-laços-de-repetição)
    - [while](#while)
    - [for](#for)
  - [Exercício Sugerido](#exercício-sugerido)
  - [7. Conversão de Tipos (Typecasting)](#7-conversão-de-tipos-typecasting)
  - [8. Tratamento de Exceções (Exceptions)](#8-tratamento-de-exceções-exceptions)
  - [9. Funções](#9-funções)
  - [Aplicação no Mundo Real](#aplicação-no-mundo-real)
  - [Exercício Sugerido](#exercício-sugerido-1)

- [Estruturas de Dados](#estruturas-de-dados)
  - [1. Listas](#1-listas)
  - [2. Tuplas](#2-tuplas)
  - [3. Sets (Conjuntos)](#3-sets-conjuntos)
  - [4. Dicionários](#4-dicionários)
  - [Aplicação no Mundo Real](#aplicação-no-mundo-real-1)

- [Lista de Exercícios 1](#lista-de-exercícios-1)

- [Módulos](#módulos)
  - [1. O Que São Módulos?](#1-o-que-são-módulos)
  - [2. Módulos Embutidos (Built-in)](#2-módulos-embutidos-built-in)
  - [3. Módulos Personalizados](#3-módulos-personalizados)
  - [4. Importando de Forma Específica](#4-importando-de-forma-específica)
  - [Aplicação no Mundo Real](#aplicação-no-mundo-real-2)
  - [Exercício Sugerido](#exercício-sugerido-2)

- [Funções Lambda](#funções-lambda)
  - [Unpacking Arguments](#unpacking-arguments)
  - [Unpacking Keyword Arguments](#unpacking-keyword-arguments)
- [Decoradores (Decorators)](#decoradores-decorators)
- [Iteradores (Iterators)](#iteradores-iterators)
- [List Comprehensions](#list_comprehensions)
- [Desestruturação](#desestruturação)

- [Lista de Exercícios 2](#lista-de-exercícios-2)

--- 

# Python Básico

## 1. Sintaxe Básica

Python é uma linguagem de programação de alto nível, conhecida por sua sintaxe simples e legível.

Diferente de outras linguagens, não utiliza `{}` para definir blocos de código. A indentação (espaço no início da linha) é obrigatória e indica onde um bloco começa e termina.

Um programa simples em Python:

```python
print("Olá, mundo!")
```

Neste exemplo, `print()` é uma função que exibe mensagens na tela.

---

## 2. Entrada e Saída de Dados

A entrada de dados em Python é feita com a função `input()`. A saída, com a função `print()`.

```python
nome = input("Digite seu nome: ")
print("Olá,", nome)
```

O valor digitado pelo usuário é armazenado na variável `nome` e depois exibido.

---

## 3. Variáveis e Tipos de Dados

Uma **variável** armazena um valor na memória. Em Python, não é necessário declarar o tipo da variável antes de usá-la.

```python
idade = 25
nome = "João"
altura = 1.75
```

Os tipos básicos em Python incluem:

* `int` (números inteiros)
* `float` (números decimais)
* `str` (textos)
* `bool` (valores booleanos: `True` ou `False`)

---

## 4. Programação com Python: Processamento e Memória

Todo programa realiza processamento e utiliza memória para armazenar dados.

### Alocação de Memória

Em Python, a alocação de memória é automática. Quando você cria uma variável, o interpretador reserva espaço na memória para ela.

```python
a = 5
b = 7
c = a + b
```

Cada variável ocupa um espaço na memória com seu valor.

Python também realiza **otimização de memória**. Se duas variáveis possuem o mesmo valor imutável, elas podem compartilhar o mesmo endereço:

```python
a = 5
b = 5
```

Nesse caso, `a` e `b` apontam para o mesmo local na memória, pois o valor é idêntico e imutável (inteiros são imutáveis em Python).

---

## 5. Condicionais

Condicionais permitem executar blocos de código com base em condições.

```python
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

Usamos `if`, `elif` (else if) e `else` para expressar decisões no código.

---

## 6. Laços de Repetição

### `while`

Repete enquanto a condição for verdadeira.

```python
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
```

### `for`

Percorre uma sequência ou intervalo de valores.

```python
for i in range(5):
    print("Número:", i)
```

O `range(5)` gera os números de 0 a 4.

---


## Exercício Sugerido

Crie um programa que:

1. Pergunte o nome e a idade do usuário.
2. Verifique se a pessoa é maior de idade.
3. Mostre uma mensagem personalizada.
4. Conte de 0 até a idade informada usando um `for`.

---


## 7. Conversão de Tipos (Typecasting)

Em Python, às vezes é necessário **converter** um valor de um tipo para outro. Esse processo é chamado de **typecasting** ou **type conversion**.

A conversão pode ser automática (implícita) ou feita manualmente (explícita).

```python
# Conversão implícita
x = 10
y = 2.5
z = x + y  # x (int) é convertido automaticamente para float
print(z)

# Conversão explícita
idade_str = "30"
idade_int = int(idade_str)  # converte string para inteiro
print(idade_int + 5)
```

Python possui funções como `int()`, `float()`, `str()`, `bool()` para conversão explícita.

---

## 8. Tratamento de Exceções (Exceptions)

**Exceções** são erros que ocorrem durante a execução do programa. Se não forem tratadas, o programa pode parar.

O Python fornece uma estrutura para **capturar e tratar esses erros** usando `try`, `except` e, opcionalmente, `finally`.

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except ValueError:
    print("Erro: você digitou um valor inválido.")
except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")
finally:
    print("Execução finalizada.")
```

O bloco `try` tenta executar o código. Se ocorrer algum erro, o Python procura o `except` correspondente para tratar o problema. O `finally`, se presente, é executado sempre.

Tratar exceções é importante para evitar que o usuário tenha uma má experiência com o programa.

---

## 9. Funções

**Funções** são blocos de código reutilizáveis. Elas ajudam a organizar o programa, evitar repetição e facilitar a manutenção.

Em Python, funções são definidas com a palavra-chave `def`.

```python
def saudacao(nome):
    print("Olá,", nome)

saudacao("João")
saudacao("Maria")
```

Funções podem **receber parâmetros** e **retornar valores**.

```python
def somar(a, b):
    return a + b

resultado = somar(5, 3)
print("Resultado:", resultado)
```

Também é possível definir **valores padrão** para parâmetros:

```python
def boas_vindas(nome="visitante"):
    print("Bem-vindo,", nome)

boas_vindas()
boas_vindas("Diego")
```

---

## Aplicação no Mundo Real

Conversão de tipos é útil ao lidar com entradas do usuário ou dados vindos de arquivos.

Tratamento de exceções garante que programas Web, como APIs Flask, lidem com erros sem travar o sistema. Por exemplo, tratando erros de banco de dados ou requisições malformadas.

Funções são a base da modularização. Toda aplicação Flask, por exemplo, é construída com funções que lidam com rotas, lógica de negócio e respostas HTTP.

---

## Exercício Sugerido

Crie uma função chamada `dividir()` que:

1. Recebe dois números como parâmetros.
2. Retorna o resultado da divisão.
3. Trata erro de divisão por zero com `try/except`.

Teste a função com diferentes valores, incluindo zero como divisor.

---
<br>
---
<br>
---


# Estruturas de Dados

Estruturas de dados são formas de organizar e armazenar valores para uso eficiente. Em Python, as mais comuns são listas, tuplas, conjuntos (sets) e dicionários. Cada uma tem características específicas, vantagens e limitações.

---

## 1. Listas

**Listas** são coleções ordenadas e **mutáveis** de elementos. Permitem armazenar qualquer tipo de dado e alterar o conteúdo após a criação.

```python
frutas = ["maçã", "banana", "laranja"]
print(frutas[0])       # Acessa o primeiro item
frutas.append("uva")   # Adiciona um item
frutas.remove("banana")  # Remove um item
print(frutas)
```

É possível acessar os elementos por índices, modificar, ordenar, iterar com `for`, entre outros.

---

## 2. Tuplas

**Tuplas** são semelhantes às listas, mas são **imutáveis**. Após criadas, seus valores não podem ser alterados. Isso as torna mais seguras e eficientes em termos de desempenho.

```python
coordenadas = (10, 20)
print(coordenadas[0])   # Acessa o primeiro item

# coordenadas[0] = 30 → Erro: tuplas não podem ser modificadas
```

Tuplas são úteis quando os dados não devem ser alterados, como posições fixas, constantes ou valores de configuração.

---

## 3. Sets (Conjuntos)

**Sets** são coleções **não ordenadas**, **sem elementos duplicados**. São ideais para eliminar repetições e realizar operações matemáticas como união, interseção e diferença.

```python
numeros = {1, 2, 3, 3, 4}
print(numeros)  # {1, 2, 3, 4}

numeros.add(5)
numeros.remove(2)

outro_set = {3, 4, 6}
print(numeros.intersection(outro_set))  # {3, 4}
```

Por não terem ordem, não é possível acessar os elementos por índice.

---

## 4. Dicionários

**Dicionários** armazenam pares **chave\:valor**. São mutáveis, rápidos e usados para representar dados estruturados.

```python
pessoa = {
    "nome": "Ana",
    "idade": 30,
    "cidade": "São Paulo"
}

print(pessoa["nome"])         # Ana
pessoa["idade"] = 31          # Atualiza valor
pessoa["profissão"] = "Engenheira"  # Adiciona novo par
del pessoa["cidade"]          # Remove uma chave
print(pessoa)
```

Dicionários são fundamentais em APIs, bancos de dados e manipulação de dados JSON.

---

## Aplicação no Mundo Real

* **Listas**: armazenar listas de produtos, nomes ou dados retornados de um banco.
* **Tuplas**: representar dados fixos como coordenadas geográficas ou configurações imutáveis.
* **Sets**: verificar itens únicos, filtrar duplicatas ou comparar grupos.
* **Dicionários**: armazenar objetos estruturados, como dados de usuário em um sistema web.

Em Flask, os dados das requisições (como formulários e JSON) muitas vezes são tratados como dicionários.

---

# Lista de Exercícios 1

1. Leia três números inteiros, calcule a média aritmética simples e informe se cada número está abaixo, acima ou exatamente na média, apresentando os resultados em uma única linha organizada.

2. Solicite o valor de um investimento inicial, a taxa de juros anual e o número de anos, então calcule e mostre o montante anual acumulado usando juros compostos, imprimindo uma linha para cada ano com o saldo atualizado.

3. Crie um programa que solicite dois números inteiros e uma operação matemática (`+`, `-`, `*`, `/`). Execute a operação escolhida e exiba o resultado. Utilize tratamento de exceções para divisões por zero e entradas inválidas.

4. Solicite ao usuário seu nome completo e idade. Imprima uma saudação personalizada e informe em que ano ele completará 100 anos.

5. Faça um programa que receba uma lista de 5 nomes digitados pelo usuário, ordene-os alfabeticamente e exiba o resultado com uma numeração.

6. Crie uma função `classificar_idade()` que recebe a idade como parâmetro e retorna se a pessoa é "criança", "adolescente", "adulto" ou "idoso". Utilize essa função com dados lidos do usuário.

7. Crie um dicionário para armazenar dados de um livro: título, autor, ano e número de páginas. Solicite os dados ao usuário e, ao final, exiba o dicionário formatado.

8. Solicite um número inteiro positivo e use um laço `for` para imprimir todos os números pares de 0 até esse número, inclusive.

9. Crie uma lista de números inteiros e utilize um laço `for` para imprimir a soma acumulada dos elementos, passo a passo, linha por linha.


---


# Módulos

Programas bem organizados são divididos em partes menores e reutilizáveis. Em Python, essas partes são chamadas de **módulos**. Usar módulos ajuda a manter o código limpo, reaproveitável e mais fácil de manter.

---

## 1. O Que São Módulos?

Um **módulo** é um arquivo `.py` que contém definições e implementações de variáveis, funções ou classes. Ao importar um módulo, podemos usar seus recursos em outro arquivo ou programa.

Python já vem com uma biblioteca padrão de módulos prontos para uso, mas você também pode criar os seus.

---

## 2. Módulos Embutidos (Built-in)

Python possui diversos módulos nativos que você pode importar a qualquer momento sem instalar nada.

Exemplo com o módulo `math`, usado para cálculos matemáticos:

```python
import math

raiz = math.sqrt(25)
print("Raiz quadrada de 25:", raiz)

print("Valor de PI:", math.pi)
```

Outros módulos embutidos úteis:

* `random`: geração de números aleatórios
* `datetime`: manipulação de datas e horários
* `os`: interação com o sistema operacional
* `sys`: acesso a informações do sistema Python
* `statistics`: funções estatísticas básicas

---

## 3. Módulos Personalizados

Você pode criar seu próprio módulo. Basta escrever um arquivo `.py` com funções ou variáveis e importá-lo em outro arquivo.

### Exemplo prático:

**Arquivo: `meu_modulo.py`**

```python
def saudacao(nome):
    return f"Olá, {nome}!"
```

**Arquivo: `app.py`**

```python
import meu_modulo

mensagem = meu_modulo.saudacao("Ana")
print(mensagem)
```

Ambos os arquivos devem estar no mesmo diretório (ou seguir a estrutura de pacotes correta).

---

## 4. Importando de Forma Específica

Você pode importar somente o que deseja de um módulo:

```python
from math import sqrt

print(sqrt(16))  # Não precisa escrever math.sqrt
```

Também é possível dar apelidos:

```python
import math as m
print(m.pi)
```

---

## Aplicação no Mundo Real

Módulos são fundamentais em projetos maiores. Por exemplo, em uma aplicação Flask, cada parte do sistema pode estar em um módulo diferente:

* Um módulo para as rotas
* Um módulo para o banco de dados
* Um módulo para funções auxiliares

Isso torna o código mais organizado, facilita testes e reaproveitamento de código.


## Exercício Sugerido

1. Crie um módulo chamado `calculadora.py` com funções: `somar(a, b)`, `subtrair(a, b)`, `multiplicar(a, b)` e `dividir(a, b)`.
2. Em outro arquivo `app.py`, importe esse módulo e use as funções com valores fornecidos pelo usuário.

---

# Funções Lambda

Funções **lambda** são funções anônimas em Python — ou seja, funções que **não têm nome**. São usadas quando se precisa de uma função rápida e simples, geralmente passada como argumento para outra função.

---

## 1. Introdução Teórica

Uma função lambda é definida em **uma única linha**, usando a palavra-chave `lambda`. Ela pode ter **vários parâmetros**, mas **apenas uma expressão**, que é automaticamente retornada.

A sintaxe é:

```python
lambda argumentos: expressão
```

Funções lambda são comumente usadas quando se quer evitar a criação de uma função nomeada para tarefas pequenas.

---

## 2. Exemplo Prático

```python
# Função lambda que soma dois números
soma = lambda x, y: x + y

print(soma(3, 5))  # Resultado: 8
```

Elas também são muito usadas com funções como `map()`, `filter()` e `sorted()`:

```python
# Dobrar todos os números de uma lista
numeros = [1, 2, 3, 4]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)  # [2, 4, 6, 8]
```

---

## 3. Explicação do Código

No primeiro exemplo, `lambda x, y: x + y` define uma função que recebe dois parâmetros e retorna a soma deles. Essa função é atribuída à variável `soma`, que pode ser chamada como qualquer função normal.

No segundo exemplo, `map()` aplica a função lambda (que multiplica por 2) a cada item da lista `numeros`.

---

## 4. Aplicações no Mundo Real

Funções lambda são úteis em situações onde funções são **passadas como argumentos**, especialmente em programação funcional e manipulação de dados.

Exemplos reais incluem:

* Ordenar listas de dicionários com base em um campo.
* Aplicar transformações rápidas a listas de dados.
* Definir regras de ordenação em frameworks como Flask ou Pandas.

```python
# Ordenando lista de dicionários por idade
pessoas = [
    {"nome": "Ana", "idade": 30},
    {"nome": "Bruno", "idade": 25}
]

ordenadas = sorted(pessoas, key=lambda pessoa: pessoa["idade"])
print(ordenadas)
```

Sua explicação está muito boa: clara, bem estruturada e com exemplos didáticos. Ainda assim, posso sugerir pequenas melhorias para deixá-la **mais direta, técnica e precisa**, especialmente se for usada em um contexto de estudo ou documentação. Aqui vão as sugestões:

---


## Unpacking Arguments

O `*args` em Python é uma forma prática de permitir que uma função aceite um **número variável de argumentos posicionais** (ou seja, não nomeados). O asterisco (`*`) diante de `args` (nome convencional, mas não obrigatório) tem dois usos principais:

1. **Empacotamento (*Packing*)**: ao definir uma função com `*args`, todos os argumentos posicionais extras são **empacotados em uma tupla**.
2. **Desempacotamento (*Unpacking*)**: ao chamar uma função com `*` antes de uma lista ou tupla, os elementos são **desempacotados** e passados como argumentos individuais.

---

### Exemplo 1: Empacotando argumentos em uma função

```python
def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

print(multiply(2, 3, 4))  # Saída: 24
```

Neste exemplo, `args` será a tupla `(2, 3, 4)`. A função itera sobre os elementos e multiplica os valores. O número de argumentos passados pode variar.

---

### Exemplo 2: Desempacotando argumentos ao chamar uma função

```python
def add(x, y):
    return x + y

nums = [1, 2]
print(add(*nums))  # Saída: 3
```

Aqui, `*nums` desempacota a lista `[1, 2]` e a função recebe os valores como se fossem passados diretamente: `add(1, 2)`.

---


## Unpacking Keyword Arguments

O `**kwargs` em Python permite que uma função aceite um **número variável de argumentos nomeados** (ou seja, passados com chave e valor). O duplo asterisco (`**`) diante de `kwargs` (nome convencional, mas não obrigatório) tem dois usos principais:

1. **Empacotamento (*Packing*)**: ao definir uma função com `**kwargs`, todos os argumentos nomeados extras são **empacotados em um dicionário**.
2. **Desempacotamento (*Unpacking*)**: ao chamar uma função com `**` antes de um dicionário, os pares chave-valor são **desempacotados** como argumentos nomeados.

---

### Exemplo 1: Empacotando argumentos nomeados em uma função

```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(nome="Diego", idade=30, linguagem="Python")
```

**Saída:**

```
nome: Diego  
idade: 30  
linguagem: Python
```

Neste exemplo, os argumentos nomeados passados são empacotados em um dicionário:
`kwargs = {'nome': 'Diego', 'idade': 30, 'linguagem': 'Python'}`

A função então percorre esse dicionário e imprime cada par chave-valor. A quantidade e os nomes dos argumentos podem variar.

---

### Exemplo 2: Desempacotando argumentos nomeados ao chamar uma função

```python
def conectar(host, porta, protocolo):
    print(f"Conectando ao {host}:{porta} via {protocolo}...")

config = {"host": "localhost", "porta": 8080, "protocolo": "HTTP"}
conectar(**config)
```

**Saída:**

```
Conectando ao localhost:8080 via HTTP...
```

Aqui, o `**config` desempacota o dicionário e passa os valores como argumentos nomeados:
`conectar(host="localhost", porta=8080, protocolo="HTTP")`.

---
---


# Decoradores (Decorators)

Decoradores são um recurso avançado e poderoso do Python. Eles permitem **modificar o comportamento de funções** de forma elegante, sem alterar diretamente o código da função original.


## 1. Introdução Teórica

Um decorador é, na prática, uma **função que recebe outra função como argumento e retorna uma nova função com comportamento modificado**.

Decoradores são muito usados para adicionar funcionalidades extras, como:

- Verificar permissões
- Registrar chamadas
- Medir tempo de execução
- Validar parâmetros

Python já possui decoradores prontos, como `@staticmethod` ou `@property`, mas também é possível criar seus próprios decoradores.

---

## 2. Exemplo Prático

```python
def meu_decorador(funcao_original):
    def nova_funcao():
        print("Antes da função")
        funcao_original()
        print("Depois da função")
    return nova_funcao

@meu_decorador
def diga_ola():
    print("Olá!")

diga_ola()
```

---

## 3. Explicação do Código

A função `meu_decorador` recebe `funcao_original` como argumento. Dentro dela, é definida `nova_funcao()`, que chama `funcao_original()` no meio de dois `print()`.

O uso de `@meu_decorador` antes da definição de `diga_ola()` significa que, ao chamar `diga_ola()`, o Python na verdade executa `nova_funcao()` — ou seja, a função decorada.

---

## 4. Aplicações no Mundo Real

Decoradores são muito utilizados em frameworks como Flask e Django.

Por exemplo, no Flask:

```python
@app.route('/home')
def home():
    return "Página inicial"
```

Aqui, `@app.route` é um decorador que associa a função `home()` à rota `/home`.

Outros exemplos práticos:

* `@login_required`: usado para proteger rotas que só podem ser acessadas por usuários autenticados.
* `@cache`: para armazenar o resultado de funções e acelerar execuções futuras.
* `@log_execution`: para registrar em log quando a função foi chamada.


## 5. Exercício Sugerido

Crie um decorador chamado `@mostrar_log` que imprima uma mensagem antes e depois da execução de uma função. Use-o para decorar uma função que imprime "Processando dados...".

---


# Iteradores (Iterators)

Em Python, um **iterador** é um objeto que permite **percorrer uma sequência de elementos**, um por vez. Ele é a base de estruturas como loops `for` e `while`.


## 1. Introdução Teórica

Um iterador segue dois princípios:

- Ele **mantém um estado interno**, ou seja, sabe onde parou na sequência.
- Ele fornece os elementos **um por um**, por meio da função `next()`.

Para ser considerado um iterador, um objeto precisa implementar os métodos especiais:

- `__iter__()` – retorna o próprio objeto iterador.
- `__next__()` – retorna o próximo item ou gera um erro `StopIteration` quando a sequência termina.

Todo **objeto iterável** (como listas, strings, tuplas) pode gerar um iterador.

---

## 2. Exemplo Prático

```python
nomes = ["Ana", "Bruno", "Carlos"]
it = iter(nomes)

print(next(it))  # Ana
print(next(it))  # Bruno
print(next(it))  # Carlos
# print(next(it)) → Lança StopIteration
```

Outro exemplo com `for`, que usa internamente um iterador:

```python
for nome in nomes:
    print(nome)
```

---

## 3. Criando um Iterador Personalizado

Você também pode criar sua própria classe que se comporta como um iterador:

```python
class Contador:
    def __init__(self, limite):
        self.atual = 0
        self.limite = limite

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual < self.limite:
            num = self.atual
            self.atual += 1
            return num
        else:
            raise StopIteration

contador = Contador(3)
for numero in contador:
    print(numero)
```

---

## 4. Explicação do Código

A classe `Contador` começa no zero e vai até o limite definido. Cada chamada ao `next()` retorna o número atual e incrementa.

Quando atinge o limite, a exceção `StopIteration` é lançada automaticamente para encerrar a iteração.

---

## 5. Aplicações no Mundo Real

Iteradores são amplamente usados para percorrer coleções de dados:

* Em APIs para processar grandes volumes de registros paginados.
* Em leitura de arquivos linha por linha com `open()`.
* Em bibliotecas como `pandas`, `Flask` (para `request.stream`) e `itertools`.

Além disso, ao criar um iterador personalizado, você tem controle total sobre o fluxo e formato dos dados sendo percorridos.

---

# List Comprehensions

**List Comprehensions** permite gerar novas listas aplicando operações a elementos de uma lista pre-existente, tudo em uma única linha de código.

### Por que usar List Comprehensions?

Vamos ver um exemplo prático. Suponha que você tenha uma lista de frutas e queira criar uma nova lista contendo apenas as frutas que possuem a letra "a" no nome.

**Sem List Comprehension:**

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
# Saída: ['apple', 'banana', 'mango']
```

Para alcançar o mesmo resultado com uma **List Comprehension**, o código fica muito mais compacto:

**Com List Comprehension:**

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
# Saída: ['apple', 'banana', 'mango']
```

Como você pode ver, a **List Comprehension** simplifica o código, tornando-o mais fácil de ler e entender.

### A Sintaxe

A sintaxe básica de uma **List Comprehension** é a seguinte:

```python
newlist = [expression for item in iterable if condition == True]
```

  * **`expression`**: É o item que será adicionado à nova lista. Você pode manipular o `item` aqui (por exemplo, `x.upper()`, `x*2`).
  * **`item`**: É a variável que representa cada elemento no `iterable`.
  * **`iterable`**: É qualquer objeto que pode ser iterado (como uma lista, tupla, conjunto, range, etc.).
  * **`condition` (opcional)**: É uma expressão booleana que atua como um filtro. Somente os itens para os quais a condição é `True` serão incluídos na nova lista.

O valor de retorno de uma **List Comprehension** é sempre uma **nova lista**, deixando a lista original inalterada.

### Detalhes dos Componentes

#### Condição

A condição funciona como um filtro, aceitando apenas os itens que avaliam como `True`.

**Exemplo:** Filtrar itens que não sejam "apple".

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
# Saída: ['banana', 'cherry', 'kiwi', 'mango']
```

A condição `if x != "apple"` retornará `True` para todos os elementos, exceto "apple", resultando em uma nova lista sem a maçã.

A condição é **opcional** e pode ser omitida se você quiser incluir todos os elementos do iterável original na nova lista:

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)
# Saída: ['apple', 'banana', 'cherry', 'kiwi', 'mango']
```

#### Iterável

O `iterable` pode ser qualquer objeto que possa ser iterado. Isso inclui listas, tuplas, conjuntos (sets), strings, e até mesmo a função `range()`.

**Exemplo:** Usando `range()` para criar uma lista de números.

```python
newlist = [x for x in range(10)]
print(newlist)
# Saída: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Exemplo:** Combinando `range()` com uma condição.

```python
newlist = [x for x in range(10) if x < 5]
print(newlist)
# Saída: [0, 1, 2, 3, 4]
```

#### Expressão

A `expression` é o item atual na iteração, mas também é o resultado final que será adicionado à nova lista. Você pode manipular o item aqui antes que ele seja incluído.

**Exemplo:** Transformar todos os nomes de frutas para maiúsculas.

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)
# Saída: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']
```

Você pode até definir um valor fixo para todos os itens na nova lista:

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)
# Saída: ['hello', 'hello', 'hello', 'hello', 'hello']
```

A expressão também pode conter uma **condição ternária** (ou seja, um `if-else` em uma linha), que manipula o resultado com base em uma condição, em vez de filtrar itens:

**Exemplo:** Substituir "banana" por "orange".

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
# Saída: ['apple', 'orange', 'cherry', 'kiwi', 'mango']
```

Neste exemplo, a expressão diz: "Retorne o item `x` se ele não for 'banana'; caso contrário, retorne 'orange'".

### Múltiplos `for` e `if`

**List Comprehensions** também podem incluir múltiplos cláusulas `for` e `if`, o que as torna incrivelmente flexíveis para operações mais complexas, como achatar listas ou combinar elementos de diferentes iteráveis.

**Exemplo:** Combinar elementos de duas listas onde eles não são iguais.

```python
list1 = [1, 2, 3]
list2 = [3, 1, 4]

# Equivalente a laços for aninhados:
# combs = []
# for x in list1:
#     for y in list2:
#         if x != y:
#             combs.append((x, y))

combs = [(x, y) for x in list1 for y in list2 if x != y]
print(combs)
# Saída: [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

Observe que a ordem das cláusulas `for` e `if` na **List Comprehension** corresponde à ordem dos laços aninhados.

**Exemplo:** Achatar uma lista de listas.

```python
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for elem in vec for num in elem]
print(flattened_list)
# Saída: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

-----

**Exercício:**

Considere o seguinte código:

```python
fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana']
```

Qual será o valor de `newlist`?

a) `['apple', 'cherry']`
b) `['banana']`
c) `True`

---


# Desestruturação

**Desestruturação**, ou **unpacking**, é uma forma eficiente de extrair valores de coleções (como listas e tuplas) e atribuí-los a variáveis de uma vez só.

### Atribuições Simples

Você pode atribuir vários valores a várias variáveis em uma única linha. O número de variáveis deve ser igual ao número de valores.

**Exemplo:**

```python
x, y = 5, 11
print(f"x: {x}, y: {y}") # Saída: x: 5, y: 11

a, b, c = [10, 20, 30] # Funciona com listas também
print(f"a: {a}, b: {b}, c: {c}") # Saída: a: 10, b: 20, c: 30
```

Se o número de variáveis e valores for diferente, você receberá um erro (`ValueError`).

### Desestruturação em Laços `for`

A desestruturação é especialmente útil em laços `for` quando você está iterando sobre coleções que contêm pares ou grupos de valores (como tuplas).

**Exemplo com `enumerate()`:**

A função `enumerate()` retorna pares de (índice, valor) para cada item em uma lista.

```python
minha_lista = ["maçã", "banana", "cereja"]
for indice, fruta in enumerate(minha_lista):
    print(f"{indice}: {fruta}")
# Saída:
# 0: maçã
# 1: banana
# 2: cereja
```

**Exemplo com lista de tuplas:**

Se você tem uma lista de tuplas, pode desestruturar cada tupla diretamente no laço.

```python
pessoas = [
    ("Alice", 30),
    ("Bob", 25),
    ("Carol", 35)
]

for nome, idade in pessoas:
    print(f"Nome: {nome}, Idade: {idade}")
# Saída:
# Nome: Alice, Idade: 30
# Nome: Bob, Idade: 25
# Nome: Carol, Idade: 35
```

Isso é muito mais legível do que acessar os elementos por índice (`pessoa[0]`, `pessoa[1]`).

### Ignorando Valores com `_` (Underscore)

Às vezes, você não precisa de todos os valores de uma coleção. Use o **underscore (`_`)** para ignorar valores que você não vai usar.

**Exemplo:**

```python
dados = ("produto_a", 150.00, "em_estoque")
nome_produto, _, status = dados # Ignoramos o preço
print(f"Produto: {nome_produto}, Status: {status}") # Saída: Produto: produto_a, Status: em_estoque
```

O `_` também é comum em laços quando você precisa repetir algo um certo número de vezes, mas não precisa do valor da iteração:

```python
for _ in range(5):
    print("Olá!") # Imprime "Olá!" 5 vezes
```

### Coletando Valores Restantes com `*` (Asterisco)

O operador **`*`** permite coletar múltiplos valores restantes em uma nova lista durante a desestruturação.

**Exemplo:**

```python
numeros = [1, 2, 3, 4, 5]
primeiro, *resto = numeros
print(f"Primeiro: {primeiro}") # Saída: Primeiro: 1
print(f"Resto: {resto}")       # Saída: Resto: [2, 3, 4, 5]
```

Você também pode coletar valores do meio:

```python
primeiro, *meio, ultimo = [10, 20, 30, 40, 50]
print(f"Primeiro: {primeiro}") # Saída: Primeiro: 10
print(f"Meio: {meio}")         # Saída: Meio: [20, 30, 40]
print(f"Último: {ultimo}")     # Saída: Último: 50
```

Lembre-se: você só pode usar um `*` por atribuição de desestruturação.

---

# Lista de Exercícios 2


1. Crie um módulo chamado `utilitarios.py` que contenha uma função `dobrar(numero)` e outra `eh_par(numero)`. Em outro arquivo, importe e use essas funções com valores fornecidos pelo usuário.

2. Implemente uma função lambda que receba dois números e retorne o maior deles. Teste a função com diferentes pares de valores.

3. Use `map()` com uma lambda para transformar uma lista de temperaturas em graus Celsius para Fahrenheit. Imprima a nova lista.

4. Dada a lista `palavras = ["python", "lambda", "decorador", "função"]`, use `filter()` com lambda para exibir apenas as palavras com mais de 6 letras.

5. Crie um decorador chamado `@logar` que imprima `"Iniciando execução..."` antes da função e `"Execução finalizada."` depois. Use-o para decorar uma função que imprime "Processando dados...".

6. Implemente um decorador `@verificar_login` que só executa a função se o usuário estiver autenticado (`usuario_autenticado = True`). Caso contrário, exiba "Acesso negado".

7. Escreva uma função `ordenar_produtos()` que recebe uma lista de tuplas `(produto, preço)` e retorna a lista ordenada do mais barato ao mais caro usando `sorted()` com lambda.

8. Escreva uma função `contar_letras()` que recebe uma lista de palavras e retorna outra lista com o número de letras de cada palavra. Use `map()` com lambda.

9. Crie um módulo chamado `calculadora.py` com funções `somar`, `subtrair`, `multiplicar` e `dividir`. Faça um programa que importe esse módulo e use as funções com base na escolha do usuário.

10. Escreva um decorador `@tempo_execucao` que calcula o tempo que uma função leva para ser executada. Use a função `time.time()` e aplique-o sobre uma função que faz um `sleep(2)`.

11. Crie uma classe `ContadorRegressivo` que recebe um número inteiro `n` e implementa um iterador que conta de `n` até 0, imprimindo cada valor com `for`.

12. Faça uma classe `MultiploDeTres` que implemente um iterador que percorre de 1 até um limite informado, retornando apenas múltiplos de 3.

13. Escreva uma função que recebe uma lista de nomes e retorna um dicionário onde as chaves são os nomes e os valores são o número de letras de cada nome. Use `lambda` e `map()` ou `dict comprehension`.

14. Crie um iterador que percorra uma string letra por letra, mas apenas retorne as consoantes, ignorando vogais.

15. Implemente uma função `executar_duas_vezes(func)` como decorador, que faz com que a função decorada seja executada duas vezes seguidas.

---


## Referências

## Documentação Oficial do Python
- https://docs.python.org/3/  
- https://docs.python.org/3/tutorial/modules.html  
- https://docs.python.org/3/py-modindex.html  
- https://docs.python.org/3/tutorial/errors.html#exceptions  
- https://docs.python.org/3/tutorial/classes.html  

## Tutoriais e Artigos Técnicos
- **TutorialsPoint** – Sintaxe Básica  
  - https://www.tutorialspoint.com/python/python_basic_syntax.htm  
- **Programiz** – Conversão de Tipos  
  - https://www.programiz.com/python-programming/type-conversion-and-casting  
- **Real Python**  
  - Variáveis: https://realpython.com/python-variables/  
  - Exceções: https://realpython.com/python-exceptions/  
  - Módulos e Pacotes: https://realpython.com/python-modules-packages/  
  - Lambda: https://realpython.com/python-lambda/  
  - POO: https://realpython.com/python3-object-oriented-programming/  
- **DataCamp** – Decorators  
  - https://www.datacamp.com/tutorial/decorators-python  
- **PythonBasics** – Decorators  
  - https://pythonbasics.org/decorators/  
- **TutorialsTeacher** – Magic (Dunder) Methods  
  - https://www.tutorialsteacher.com/python/magic-methods-in-python  

## W3Schools – Seção Python
- Página principal: https://www.w3schools.com/python/  
- Variáveis: https://www.w3schools.com/python/python_variables.asp  
- Listas: https://www.w3schools.com/python/python_lists.asp  
- Tuplas: https://www.w3schools.com/python/python_tuples.asp  
- Sets: https://www.w3schools.com/python/python_sets.asp  
- Dicionários: https://www.w3schools.com/python/python_dictionaries.asp  
- Inheritance: https://www.w3schools.com/python/python_inheritance.asp  
- Lambda: https://www.w3schools.com/python/python_lambda.asp  
- Iterators: https://www.w3schools.com/python/python_iterators.asp  

## Livros
- *Python Fluente* — Luciano Ramalho  

---


