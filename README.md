# Python

Repositório contendo diversos exercícios de programação em Python, abordando desde conceitos básicos até tópicos mais avançados, além disso, ele também possui uma apostila detalhada com os principais conceitos de programação com Python.

<div style="display: flex; flex-direction: row;">
  <div style="margin-right: 20px; display: flex; justify-content: flex-start;">
    <img src="img/python.png" alt="Logo Python" width="100"/>
  </div>
</div>

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
12. [Exercícios](#exercícios)
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
# Guia de Aprendizado em Python

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

## Estruturas Condicionais
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

## Exercícios

### Inventário
Crie um sistema de inventário que:
- Armazene produtos, quantidades e preços.
- Permita adicionar, remover e listar produtos.
- Gere um relatório com a quantidade total e valor do estoque.

### Sistema de Notas
Crie um sistema de notas escolares:
- Receba notas e calcule a média.
- Classifique alunos como "Aprovado" (>=7), "Recuperação" (5-6.9) ou "Reprovado" (<5).

### Controle de Tráfego
- Pergunte quantos veículos passaram por um ponto.
- Exiba "Tráfego alto" se passar do limite definido.

### Simulador de Investimentos
- Permita calcular juros compostos e comparar diferentes cenários.

### Gerador de Números Primos
- Encontre números primos até um limite informado.

### Jogo de Adivinhação
- Usuário tenta adivinhar um número aleatório de 1 a 100.
- Informe se o número é maior ou menor após cada tentativa.

### Sistema de Agendamento
- Agende compromissos e calcule o tempo restante até a data.

### Ranking de Alunos
- Insira alunos e notas.
- Ordene os alunos por desempenho.

### Cálculo de Fibonacci
- Compare versão iterativa e recursiva.

### Manipulação de Strings
- Conte vogais em uma frase.
- Inverta uma string sem usar slicing.

---

## Autor

Desenvolvido por Diego Franco

