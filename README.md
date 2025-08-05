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

Condicionais permitem que um programa execute diferentes ações com base em condições que podem ser verdadeiras ou falsas. 

### `if`, `elif` e `else`

A estrutura básica de uma condicional é o `if`, que executa um bloco de código se sua condição for verdadeira. O uso dos dois pontos (`:`) após a expressão é obrigatório. 

```python
nome = "Alura"
if nome == "Alura": # A condição verifica se a variável nome é igual a "Alura"
    print("Boas vindas") # Este código só é executado se a condição for verdadeira
```

O bloco `else` é opcional e executado somente se a condição do `if` for falsa. 

```python
nome = "Start"
if nome == "Alura":
    print("Boas vindas")
else:
    # Como 'nome' não é "Alura", a condição do if é falsa e este bloco é executado
    print("Nome desconhecido")
```

Para testar múltiplas condições em sequência, utiliza-se o `elif` (uma contração de "else if"). Ele permite adicionar novas verificações antes de chegar ao `else` final. 

```python
nome = "Latam"
if nome == "Alura":
    print("Bem-vindo à Alura!")
elif nome == "Latam":
    # A primeira condição foi falsa, então esta é testada e, por ser verdadeira, o bloco é executado
    print("Bem-vindo ao Latam!")
else:
    print("Nome desconhecido.")
```

-----

#### Operadores

Para construir as expressões lógicas das condicionais, utilizamos operadores de comparação e lógicos.

#### Operadores de Comparação

Comparam valores e retornam `True` (verdadeiro) ou `False` (falso). 

| Operador | Descrição | Exemplo |
| :--- | :--- | :--- |
| `==` |  Verifica se um valor é **igual** a outro. [cite: 57] | `x == 10` |
| `!=` |  Verifica se um valor é **diferente** de outro. [cite: 57] | `x != 10` |
| `>` |  Verifica se um valor é **maior** que outro. [cite: 57] | `x > 10` |
| `<` |  Verifica se um valor é **menor** que outro. [cite: 57] | `x < 10` |
| `>=` |  Verifica se um valor é **maior ou igual** a outro. [cite: 57] | `x >= 10` |
| `<=` |  Verifica se um valor é **menor ou igual** a outro. [cite: 57] | `x <= 10` |

#### Operadores Lógicos

 São usados para combinar múltiplas condições.  Os mais comuns são `and` e `or`. 

  *  **`and`**: Retorna `True` apenas se **todas** as condições forem verdadeiras. 

<!-- end list -->

```python
idade = 25
tem_documento = "sim"

# Ambas as condições devem ser verdadeiras para o resultado ser verdadeiro
if idade >= 18 and tem_documento == "sim":
    print("Entrada permitida!")
else:
    print("Entrada negada.")
```

  *  **`or`**: Retorna `True` se **pelo menos uma** das condições for verdadeira.

<!-- end list -->

```python
feriado = "não"
folga = "sim"

# Basta que uma das condições seja verdadeira para o resultado ser verdadeiro
if feriado == "sim" or folga == "sim":
    print("Você pode descansar hoje!")
else:
    print("Dia normal de trabalho.")
```

---

### Estrutura Condicional `match/case`

Introduzida no Python 3.10, a estrutura `match/case` oferece uma forma mais declarativa e poderosa para o controle de fluxo, sendo uma alternativa moderna para cadeias longas de `if/elif/else`. 

Ela é especializada em **comparação de padrões estruturais** (structural pattern matching).

```python
def processar_comando(comando):
    match comando:
        case "iniciar":
            print("Sistema iniciando...")
        
        case ("enviar", destinatario):
            print(f"Enviando dados para {destinatario}...")

        case {"acao": "deletar", "id": item_id}:
            print(f"Deletando item {item_id}.")

        case _:
            print("Comando não reconhecido.")

# Exemplos de uso
processar_comando("iniciar")
processar_comando(("enviar", "servidor_central"))
processar_comando({"acao": "deletar", "id": 101})
processar_comando("pausar")
```

A instrução `match` avalia uma variável (o *sujeito*, `comando` no exemplo) e a compara, em ordem, com os padrões definidos em cada bloco `case`. 

O código do primeiro `case` que corresponder perfeitamente ao padrão do sujeito é executado, e a estrutura é encerrada. 

Se nenhum padrão corresponder, o bloco do `case _` (chamado de *wildcard* ou coringa) é executado, funcionando como um `else` padrão.

O grande poder do `match/case` está na sua capacidade de não apenas comparar valores literais (como `case "iniciar"`), mas também de desestruturar tipos de dados complexos, como tuplas e dicionários. 

No `case ("enviar", destinatario)`, a estrutura verifica se o comando é uma tupla de dois elementos começando com "enviar" e, em caso positivo, automaticamente atribui o segundo elemento à variável `destinatario`. 

Da mesma forma, no `case {"acao": "deletar", ...}`, ele verifica se o comando é um dicionário com as chaves e valores especificados, extraindo o valor da chave `"id"` para a variável `item_id`. Isso torna o código mais legível e expressivo ao lidar com estruturas de dados variadas.


____

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

---
<br>
---
<br>
---




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


