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

# Sintaxe Básica

Python é uma linguagem de programação de alto nível, conhecida por sua sintaxe simples e legível.

Diferente de outras linguagens, não utiliza `{}` para definir blocos de código. A indentação (espaço no início da linha) é obrigatória e indica onde um bloco começa e termina.

Um programa simples em Python:

```python
print("Olá, mundo!")
```

Neste exemplo, `print()` é uma função que exibe mensagens na tela.

---

# Entrada e Saída de Dados

A entrada de dados em Python é feita com a função `input()`. A saída, com a função `print()`.

```python
nome = input("Digite seu nome: ")
print("Olá,", nome)
```

O valor digitado pelo usuário é armazenado na variável `nome` e depois exibido.


---

# Variáveis 

Uma **variável** armazena um valor na memória. Em Python, não é necessário declarar o tipo da variável antes de usá-la.

```python
idade = 25
nome = "João"
altura = 1.75
```

## Processamento e Memória

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

# Tipos de Dados

Os tipos básicos em Python incluem:

* `int` (números inteiros)
* `float` (números decimais)
* `str` ou `string` (textos)
* `bool` (valores booleanos: `True` ou `False`)

## Strings em Python

Strings são sequências de caracteres usadas para representar texto. Em Python, elas são delimitadas por aspas simples (`'`), duplas (`"`) ou triplas (`"""`).

```python
# Aspas simples ou duplas são usadas para strings de uma única linha.
mensagem_simples = 'Olá, mundo!'
mensagem_dupla = "Python é incrível!"

# Aspas triplas permitem criar strings que abrangem múltiplas linhas.
texto_multilinha = """Essa é uma string
que pode ter múltiplas
linhas."""
```

A escolha entre aspas simples e duplas é uma questão de preferência, mas aspas triplas são especificamente úteis para textos longos com quebras de linha.

-----

### Formatação com f-strings

As f-strings (strings formatadas) são a maneira moderna e legível de incorporar variáveis e expressões diretamente dentro de uma string. A sintaxe utiliza a letra `f` antes das aspas.

```python
estudante = "Pedro"
nota = 10

# A variável é colocada entre chaves {} dentro da string.
mensagem = f"{estudante} tirou a nota {nota}!"
print(mensagem) # Saída: Pedro tirou a nota 10!
```

-----

### Acessando Partes de uma String

* **Indexação**

A indexação permite acessar um único caractere de uma string através de sua posição (índice). A contagem começa em `0`. Índices negativos são usados para acessar caracteres a partir do final da string, onde `-1` é o último caractere.

```python
texto = "Python"

# Acessa o caractere na posição 0 (o primeiro).
print(texto[0]) # Saída: P

# Acessa o último caractere.
print(texto[-1]) # Saída: n
```

* **Slicing (Fatiamento)**

O slicing extrai uma substring (uma parte da string) usando a sintaxe `[início:fim:passo]`.

  * `início`: O índice onde a fatia começa (inclusivo).
  * `fim`: O índice onde a fatia termina (exclusivo).
  * `passo`: O intervalo entre os caracteres (opcional).

<!-- end list -->

**Extrai do índice 1 até o 3 (o índice 4 não é incluído):**

```python
texto = "Python"

print(texto[1:4])  # Saída: yth
```

**Se o início for omitido, a fatia começa do índice 0**
```python
print(texto[:3])   # Saída: Pyt

# mesmo que:
print(texto[0:3]) 
```


**Com um passo de 2, extrai caracteres de forma alternada:**
```python
print(texto[::2])  # Saída: Pto

# mesmo que:
print(texto[0:5:2])
```

-----

### Métodos de Manipulação e Verificação

#### Limpeza e Formatação de Caixa

Métodos comuns para transformar ou limpar strings.

* **.strip()**
remove espaços em branco do início e do fim.

```python
exemplo = "  Olá Mundo  "

print(exemplo.strip()) # Saída: "Olá Mundo"
```

* **.lower()**
Converte todos os caracteres para minúsculas.

```python
print(exemplo.lower()) # Saída: "  olá mundo  "
```

* **.upper()**
Converte todos os caracteres para maiúsculas.

```python
print(exemplo.upper()) # Saída: "  OLÁ MUNDO  "
```


* **.replace()**
substitui uma substring por outra.

```python
print(exemplo.replace("Mundo", "Python").strip()) # Saída: "Olá Python"
```


#### Verificação de Conteúdo

É comum verificar se uma string contém, começa ou termina com uma determinada substring.

```python
texto = "Python é poderoso"

# O operador 'in' verifica se uma substring está presente.
print("poderoso" in texto) # Saída: True
print("Java" in texto)     # Saída: False

# .startswith() verifica se a string começa com a substring.
# É sensível a maiúsculas e minúsculas.
print(texto.startswith("Py"))   # Saída: True
print(texto.startswith("py"))   # Saída: False

# .endswith() verifica se a string termina com a substring.
print(texto.endswith("poderoso")) # Saída: True
print(texto.endswith("oso"))      # Saída: True
```

---


# Condicionais

Condicionais permitem que um programa execute diferentes ações com base em condições que podem ser verdadeiras ou falsas. 

## `if`, `elif` e `else`

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

### Operadores

Para construir as expressões lógicas das condicionais, utilizamos operadores de comparação e lógicos.

#### Operadores de Comparação

Comparam valores e retornam `True` (verdadeiro) ou `False` (falso). 

| Operador | Descrição | Exemplo |
| :--- | :--- | :--- |
| `==` |  Verifica se um valor é **igual** a outro.  | `x == 10` |
| `!=` |  Verifica se um valor é **diferente** de outro. | `x != 10` |
| `>` |  Verifica se um valor é **maior** que outro.  | `x > 10` |
| `<` |  Verifica se um valor é **menor** que outro.  | `x < 10` |
| `>=` |  Verifica se um valor é **maior ou igual** a outro. | `x >= 10` |
| `<=` |  Verifica se um valor é **menor ou igual** a outro.  | `x <= 10` |

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

## Estrutura Condicional `match/case`

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

# Laços de Repetição


Laços são estruturas de código que permitem executar um bloco de código repetidamente enquanto uma condição for verdadeira. Em Python, as principais estruturas de laço são `for` e `while`. 

A lógica de um laço pode ser entendida como: repita uma ação até que a condição de parada se torne falsa. 

## Laço `for`

O laço `for` é utilizado para percorrer os itens de uma coleção de dados (iterável), como listas ou tuplas. Ele é ideal para situações em que o número de repetições é conhecido previamente. 

```python
nomes = ["Carlos", "Ana", "Pedro", "Maria"] 

for nome in nomes: 
  print(nome) 
```

Neste código, o laço `for` itera sobre a lista `nomes`, executando o comando `print(nome)` para cada um dos seus elementos. A palavra `in` e os dois pontos (`:`) na sintaxe são obrigatórios. 

## Laço `while`

O laço `while` executa um bloco de código continuamente enquanto uma condição especificada for verdadeira. É muito útil quando o número de iterações é desconhecido, pois a repetição depende do resultado da condição. 

```python
contador = 0

while contador < 5:
    print(f"Contador atual: {contador}") 
    contador += 1 
```

O laço verifica a condição `contador < 5` e, se for verdadeira, executa o bloco de código. Dentro do laço, o valor do contador é impresso e depois incrementado. Esse processo se repete até que a condição se torne falsa, o que acontece quando o contador atinge o valor 5. Se a condição de saída nunca for alcançada, o laço se torna um **loop infinito**. 

-----

### Controle de Fluxo em Laços

É possível alterar o comportamento de um laço com as instruções `break` e `continue`.

#### `break`

A instrução `break` permite interromper e sair de um laço imediatamente, mesmo que a condição principal do laço ainda seja verdadeira. 

```python
nomes = ["PM3", "Alura", "Latam", "Outros"] 

for nome in nomes: 
    print(nome) 
    if nome == "Alura": 
        print("Nome encontrado! Saindo do laço.") 
        break 
```

Ao encontrar o nome "Alura", o laço imprime a mensagem de confirmação e a instrução `break` é executada, encerrando o laço.   Os nomes que vêm a seguir na lista não são processados. 

#### `continue`

A instrução `continue` permite pular a iteração atual e passar diretamente para a próxima, ignorando o restante do código dentro do bloco do laço para aquela iteração específica. 

```python
nomes = ["PM3", "Alura", "Latam", "Outros"] 

for nome in nomes:
    if nome == "Alura":
      print("Ignorando Alura.") 
      continue 
    print(f"Nome: {nome}") 
```

Neste caso, quando o laço encontra "Alura", ele imprime a mensagem de aviso e o `continue` faz com que a execução pule a linha `print(f"Nome: {nome}")` e continue para o próximo item da lista. 

-----

### **`range()`**

Gera uma sequência de números, frequentemente utilizada para controlar o número de iterações em laços `for`. 

#### 1\. Iterando um número específico de vezes: `range(stop)`

Esta é a forma mais comum de uso. Você passa um único argumento que funciona como o ponto de **parada (exclusivo)**. O laço sempre começará do zero.

```python
# Executa o bloco de código 5 vezes, para os índices de 0 a 4.
for i in range(5):
    print(f"Repetição número: {i}")
```

Neste caso, `range(5)` gera uma sequência de números que começa em `0` (padrão) e vai até, mas **não inclui**, o `5`. O resultado são os números `0, 1, 2, 3, 4`. É a maneira ideal de executar uma ação um número fixo de vezes.

-----

#### 2\. Definindo um início e fim: `range(start, stop)`

Aqui, você define explicitamente o número de **início (inclusivo)** e o de **parada (exclusivo)**. O passo (incremento) entre os números é, por padrão, `1`.

```python
# Itera sobre os números de 1 a 5.
for numero in range(1, 6):
    print(numero)
```

O `range(1, 6)` gera a sequência `1, 2, 3, 4, 5`. O laço começa no `1` e para antes de chegar ao `6`. É útil quando você precisa iterar sobre um intervalo numérico específico que não começa em zero.

-----

#### 3\. Controlando o passo da iteração: `range(start, stop, step)`

Esta é a forma mais completa, permitindo definir o **início**, a **parada** e o **passo** (o incremento ou decremento).

#### Exemplo com passo positivo (incremento)

Você pode pular números definindo um passo maior que 1.

```python
# Imprime os números pares de 2 até 10.
for i in range(2, 11, 2):
    print(i)
```

Aqui, a sequência começa em `2`, para antes do `11` e avança de `2` em `2`. O resultado é `2, 4, 6, 8, 10`.

#### Exemplo com passo negativo (decremento)

Para fazer uma contagem regressiva, o passo deve ser negativo. O valor de `start` precisa ser maior que o de `stop`.

```python
# Faz uma contagem regressiva de 10 até 1.
for segundos in range(10, 0, -1):
    print(f"{segundos}...")
print("Lançar!")
```

Neste exemplo, que você mencionou, o laço começa em `10` e vai até, mas não inclui, o `0`, diminuindo `1` a cada passo (`-1`). A sequência gerada é `10, 9, 8, 7, 6, 5, 4, 3, 2, 1`. É a forma correta de criar um laço reverso com `range`.

___

### **`len()`**

É usada para obter o comprimento (número de itens) de uma coleção, como uma lista ou string. Isso permite saber quantas iterações um laço precisa realizar. 

---

<br>
<br>

---

## Tratamento de Exceções (Exceptions)

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

## Funções

Funções são blocos de código reutilizáveis que executam uma tarefa específica. Elas são essenciais para organizar o código, evitar repetição e tornar os programas mais modulares.

A sintaxe de uma função é definida com a palavra-chave `def`, seguida pelo nome da função e parênteses. O bloco de código da função é indentado e pode finalizar com uma instrução `return` para enviar um valor de volta.

```python
def ola_mundo(nome): # 'nome' é um parâmetro
    # O bloco de código da função
    return f"Olá, {nome}!"

# Para chamar a função, usamos seu nome seguido por parênteses
# "Laís" é o argumento passado para o parâmetro 'nome'
mensagem_formatada = ola_mundo("Laís")
print(mensagem_formatada) # Saída: Olá, Laís!
```

  *  **Parâmetros** são as variáveis listadas na definição da função.  
  *  **Argumentos** são os valores reais passados para a função quando ela é chamada. 
  *  Variáveis criadas dentro de uma função têm **escopo local**, ou seja, só existem e podem ser acessadas dentro dela. 

-----

### Funções com Parâmetros Padrão

 Permitem definir um valor padrão para um parâmetro, tornando-o opcional na chamada da função. 

```python
def cumprimentar(nome="Visitante"): # "Visitante" é o valor padrão
    print(f"Olá, {nome}!")

cumprimentar() # Saída: Olá, Visitante!
cumprimentar("Jade") # Saída: Olá, Jade!
```

 Se nenhum argumento for fornecido, o valor padrão é usado.   Caso contrário, o argumento passado substitui o padrão. 

### Funções Anônimas (Lambda)

 Uma função `lambda` é uma função pequena e anônima, definida sem um nome.  Ela pode ter múltiplos argumentos, mas apenas uma única expressão. 

```python
# Sintaxe: lambda argumentos: expressão
soma = lambda a, b: a + b
print(soma(3, 5)) # Saída: 8
```

 Lambdas são úteis para operações simples ou como argumentos para outras funções (como `map` e `filter`). 

### Funções Recursivas

 São funções que chamam a si mesmas para resolver um problema, dividindo-o em subproblemas menores.   É essencial que tenham uma **condição de parada** para evitar um loop infinito. 

```python
def fatorial(n):
    # Condição de Parada: se n for 0, a recursão para.
    if n == 0:
        return 1
    # Chamada Recursiva: a função chama a si mesma com um valor menor.
    return n * fatorial(n - 1)

print(fatorial(5)) # Saída: 120
```

### Closures (Funções dentro de Funções)

 Uma closure é uma função interna que "se lembra" do ambiente (variáveis) onde foi criada, mesmo depois que a função externa já terminou sua execução. 

```python
def multiplicador(n): # Função externa
    def multiplica(x): # Closure (função interna)
        return x * n # Usa a variável 'n' da função externa
    return multiplica

triplo = multiplicador(3) # 'triplo' agora é uma closure que lembra que n=3
print(triplo(5)) # Saída: 15
```

 Closures são úteis para criar funções especializadas e encapsular lógicas sem a necessidade de usar variáveis globais. 

-----

### Funções Embutidas (`built-in`)

 São funções já incorporadas ao Python, prontas para uso.

#### Interação e Manipulação

| Método | Conceito | Exemplo |
| :--- | :--- | :--- |
| `print()` |  Exibe valores no console. | `print("Olá, mundo!")` |
| `input()` |  Lê uma entrada do usuário como string.  | `nome = input("Digite: ")` |
| `isinstance()` |  Verifica se um objeto pertence a um tipo específico.  | `isinstance(10.5, int)` |
| `len()` |  Retorna o tamanho de um objeto (string, lista, etc.). | `len("Python")` |

Dica: Para ler uma entrada separando os valores por espaços na mesma linha por exemplo 10 20 30, use o método split().

```python
entrada = input().split() 
```

#### Conversão e Criação de Tipos

A função `type()` é usada para verificar o tipo de dado de uma variável ou objeto em Python. Para usá-la, basta passar a variável como argumento.

```python
numero = 10
texto = "Olá, mundo!"
lista = [1, 2, 3]

print(type(numero))
print(type(texto))
print(type(lista))
```

**Saída:**

```
<class 'int'>
<class 'str'>
<class 'list'>
```

Ela retorna a classe do objeto, informando se é um inteiro (`int`), uma string (`str`), uma lista (`list`), etc. É muito útil para depurar e entender com que tipo de dado você está trabalhando.

### Typecasting (Conversão de Tipos) 

Typecasting é o processo de transformar um valor de um tipo de dado em outro. Isso é fundamental em Python, pois muitas operações exigem que os dados estejam em um formato específico. A conversão pode ser:

  * **Implícita**: O Python faz automaticamente, como ao somar um inteiro e um float (o resultado é um float).
  * **Explícita**: O programador força a conversão usando funções específicas. É sobre esta que vamos focar.

A conversão explícita é feita usando funções nativas que têm o mesmo nome do tipo de dado para o qual você deseja converter.

#### Convertendo para Inteiro (`int()`)

A função `int()` converte um valor para um número inteiro. Ao converter um float, a parte decimal é **truncada** (removida), não arredondada.

```python
valor_float = 19.85
valor_str = "100"

inteiro_de_float = int(valor_float)
inteiro_de_str = int(valor_str)

print(f"Float {valor_float} para int: {inteiro_de_float}") # Saída: 19
print(f"String '{valor_str}' para int: {inteiro_de_str}") # Saída: 100
```

#### Convertendo para Ponto Flutuante (`float()`)

A função `float()` converte um valor para um número de ponto flutuante (com casas decimais).

```python
valor_int = 42
valor_str = "3.14"

float_de_int = float(valor_int)
float_de_str = float(valor_str)

print(f"Inteiro {valor_int} para float: {float_de_int}") # Saída: 42.0
print(f"String '{valor_str}' para float: {float_de_str}") # Saída: 3.14
```

#### Convertendo para String (`str()`)

A função `str()` converte praticamente qualquer valor para sua representação em formato de texto (string).

```python
valor_int = 500
valor_float = 99.9
valor_lista = [1, 2, 3]

str_de_int = str(valor_int)
str_de_float = str(valor_float)
str_de_lista = str(valor_lista)

print(f"String de inteiro: '{str_de_int}'")     # Saída: '500'
print(f"String de float: '{str_de_float}'")     # Saída: '99.9'
print(f"String de lista: '{str_de_lista}'")     # Saída: '[1, 2, 3]'
```

#### Convertendo para Booleano (`bool()`)

A função `bool()` converte um valor para `True` ou `False`. A regra geral é que valores "vazios" ou nulos são `False`, e a maioria dos outros valores é `True`.

  * **Tornam-se `False`**: `0`, `0.0`, `None`, strings vazias (`""`), listas/tuplas/dicionários/conjuntos vazios (`[]`, `()`, `{}`, `set()`).
  * **Tornam-se `True`**: Qualquer número diferente de zero, strings não vazias e coleções com elementos.

<!-- end list -->

```python
print(f"bool(0): {bool(0)}")               # Saída: False
print(f"bool(''): {bool('')}")             # Saída: False
print(f"bool([]): {bool([])}")             # Saída: False
print(f"bool(1): {bool(1)}")               # Saída: True
print(f"bool('texto'): {bool('texto')}")   # Saída: True
```

#### Convertendo para Tipos de Coleção

Você também pode converter entre diferentes tipos de coleções.

```python
texto = "abc"
tupla = (1, 2, 3, 2) # Tupla com elemento duplicado

# list() cria uma lista a partir de um iterável
lista_de_texto = list(texto)
print(f"String para lista: {lista_de_texto}") # Saída: ['a', 'b', 'c']

# set() cria um conjunto, removendo elementos duplicados
conjunto_de_tupla = set(tupla)
print(f"Tupla para conjunto: {conjunto_de_tupla}") # Saída: {1, 2, 3}

# tuple() cria uma tupla
tupla_de_lista = tuple(lista_de_texto)
print(f"Lista para tupla: {tupla_de_lista}") # Saída: ('a', 'b', 'c')
```


#### Lidando com Erros de Conversão

Tentar uma conversão impossível, como `int("olá")`, gera um erro do tipo `ValueError`. A forma correta de lidar com isso é usando um bloco `try...except`.

```python
entrada_usuario = "25b"

try:
    numero = int(entrada_usuario)
    print(f"Número convertido: {numero}")
except ValueError:
    print(f"Erro: '{entrada_usuario}' não é um número inteiro válido.")
```

---
---

#### Funções Matemáticas

| Método | Conceito | Exemplo |
| :--- | :--- | :--- |
| `abs()` |  Retorna o valor absoluto de um número.  | `abs(-10)` |
| `round()` |  Arredonda um número para um número de casas decimais.  | `round(3.1415, 2)` |
| `max()` |  Retorna o maior valor entre os argumentos.  | `max(3, 5, 1)` |
| `min()` |  Retorna o menor valor entre os argumentos.| `min(3, 5, 1)` |
| `sum()` |  Retorna a soma dos itens de um iterável. | `sum([1, 2, 3])` |

#### Funções para Iteráveis

| Método | Conceito | Exemplo |
| :--- | :--- | :--- |
| `filter()` |  Filtra elementos de um iterável com base em uma função. | `list(filter(lambda x: x > 2, [1, 2, 3, 4]))` |
| `map()` |  Aplica uma função a cada elemento de um iterável. | `list(map(lambda x: x * 2, [1, 2, 3]))` |
| `zip()` |  Une dois ou mais iteráveis em pares de elementos.  | `list(zip([1, 2], ["a", "b"]))` |
| `sorted()` |  Retorna uma nova lista ordenada a partir de um iterável.  | `sorted([3, 1, 4])` |
| `reversed()` |  Retorna um iterador com os elementos na ordem inversa.   | `list(reversed([1, 2, 3]))` |
---

<br>
<br>
<br>

___


# Expressões Regulares (Regex) 

Expressões regulares são padrões usados para encontrar ou substituir sequências de caracteres em um texto. Em Python, as operações de regex são realizadas através do módulo `re`. Para começar, ele deve ser importado.

```python
import re
```

-----

## Componentes de um Padrão Regex

Um padrão de regex é construído com caracteres literais e especiais.

  * **Caracteres Literais**: Correspondem exatamente a si mesmos. Por exemplo, a regex `Python` encontrará a string "Python".
  * **Caracteres Especiais**: Símbolos com um significado específico que definem padrões complexos. Para usar um caractere especial como literal, ele deve ser "escapado" com uma barra invertida (`\`).

Abaixo estão os principais grupos de caracteres especiais.

### Metacaracteres (Caracteres Especiais)

| Símbolo | Descrição |
| :--- | :--- |
| `.` | Corresponde a qualquer caractere, exceto nova linha. |
| `\d` | Corresponde a qualquer dígito (0-9). |
| `\D` | Corresponde a qualquer caractere que não seja um dígito. |
| `\w` | Corresponde a qualquer caractere alfanumérico (letras, números e `_`). |
| `\W` | Corresponde a qualquer caractere que não seja alfanumérico. |
| `\s` | Corresponde a qualquer espaço em branco (espaço, tabulação, etc.). |
| `\S` | Corresponde a qualquer caractere que não seja espaço em branco. |

#### Classes de Caracteres

São grupos de caracteres definidos entre colchetes (`[]`).

| Símbolo | Descrição |
| :--- | :--- |
| `[abc]` | Corresponde a um único caractere: 'a', 'b' ou 'c'. |
| `[^abc]` | Corresponde a qualquer caractere que **não** seja 'a', 'b' ou 'c'. |
| `[a-z]` | Corresponde a qualquer letra minúscula de 'a' a 'z'. |
| `[A-Z]` | Corresponde a qualquer letra maiúscula de 'A' a 'Z'. |
| `[0-9]` | Corresponde a qualquer dígito de '0' a '9'. |

#### Quantificadores

Especificam o número de vezes que um padrão deve ocorrer.

| Símbolo | Descrição |
| :--- | :--- |
| `*` | Corresponde a **0 ou mais** ocorrências do padrão anterior. |
| `+` | Corresponde a **1 ou mais** ocorrências do padrão anterior. |
| `?` | Corresponde a **0 ou 1** ocorrência do padrão anterior. |
| `{n}` | Corresponde a exatamente **n** ocorrências do padrão anterior. |
| `{n,}` | Corresponde a **n ou mais** ocorrências do padrão anterior. |
| `{n,m}` | Corresponde a **entre n e m** ocorrências do padrão anterior. |

-----

### Usando Regex em Python: Exemplo Prático

O exemplo a seguir usa o módulo `re` para encontrar um endereço de e-mail em um texto.

```python
import re

texto = "Entre em contato pelo email support@example.com"

# O 'r' antes da string indica que é uma "raw string", evitando problemas com a barra invertida.
padrao_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# re.search() procura o padrão em qualquer parte do texto.
resultado = re.search(padrao_email, texto)

# É crucial verificar se uma correspondência foi encontrada antes de usar .group().
if resultado:
    # .group() retorna o texto que correspondeu ao padrão.
    print("Email encontrado:", resultado.group()) # Saída: Email encontrado: support@example.com
else:
    print("Nenhum email encontrado.")
```

Neste código, `re.search()` procura pelo padrão de e-mail no texto. Se encontrar, ele retorna um objeto de correspondência; caso contrário, retorna `None`. O método `resultado.group()` é então usado para extrair a string exata que foi encontrada.

### Outros Métodos Úteis do Módulo `re`

| Método | Descrição | Exemplo de Uso |
| :--- | :--- | :--- |
| `search` | Procura pelo padrão em qualquer parte da string e retorna a primeira ocorrência. | `re.search(r"\d+", "Há 1234 alunos")` |
| `match` | Verifica se o padrão corresponde apenas no **início** da string. | `re.match(r"abc", "abcdef")` |
| `findall` | Retorna **todas** as ocorrências do padrão em uma lista. | `re.findall(r"\d+", "3 gatos e 2 cachorros")` |
| `sub` | **Substitui** as ocorrências do padrão por outra string. | `re.sub(r"\d", "#", "Meu número é 1234")` |

### Exemplos de Padrões

  * **Telefone**: A regex `\(\d{2}\)\s\d{4,5}-\d{4}` pode encontrar números de telefone como "(11) 98765-4321".
      * `\(` e `\)`: Parênteses literais.
      * `\d{2}`: Exatamente dois dígitos.
      * `\s`: Um espaço em branco.
      * `\d{4,5}`: De quatro a cinco dígitos.
  * **Data**: A regex `\b\d{2}/\d{2}/\d{4}\b` pode encontrar datas como "25/12/2025".
      * `\b`: Garante que a correspondência é uma "palavra" completa, evitando encontrar datas dentro de outros números.

É altamente recomendável usar ferramentas online como o **regex101** para testar e depurar seus padrões antes de aplicá-los no código.

---

<br>
<br>

---

# Programação Síncrona e Assíncrona Python

## PROGRAMAÇÃO SÍNCRONA

Modelo de execução em que as tarefas são realizadas uma após a outra, de forma sequencial. Cada operação precisa ser concluída antes que a próxima inicie.

```python
import time

def tarefa(numero):
    print(f"Iniciando tarefa {numero}.")
    time.sleep(2)
    print(f"Tarefa {numero} concluída!")

tarefa(1)
tarefa(2)
tarefa(3)
```

**Saída:**

```
Iniciando tarefa 1. Tarefa 1 concluída!
Iniciando tarefa 2. Tarefa 2 concluída!
Iniciando tarefa 3. Tarefa 3 concluída!
```

-----

## PROGRAMAÇÃO ASSÍNCRONA

Permite que um programa execute várias tarefas ao mesmo tempo, sem que uma precise esperar a outra terminar.

**CONCORRÊNCIA**
Alternância rápida entre tarefas, dando a impressão de que rodam ao mesmo tempo. Ideal para tarefas de I/O (API, banco de dados).

**PARALELISMO**
Múltiplas tarefas são executadas ao mesmo tempo. Ideal para cálculos pesados e processamento de dados.

-----

### Analogias

  * **SÍNCRONO:** O garçom atende um cliente por vez, só pegando o próximo pedido quando terminar o primeiro.
  * **ASSÍNCRONO:** O garçom anota o pedido, passa para a cozinha e atende outro cliente enquanto espera a comida ficar pronta.
  * **CONCORRÊNCIA:** O garçom pega pedidos de vários clientes e alterna entre eles, mas continua sozinho no trabalho.
  * **PARALELISMO:** Vários garçons atendem clientes simultaneamente em mesas diferentes.

-----

### QUANDO USAR?

**SÍNCRONA**

  * O fluxo do programa é simples e sequencial.
  * A lógica do código depende da execução ordenada das operações.
  * Há pouca ou nenhuma espera por I/O.
  * O código é puramente computacional e pesado.
  * A simplicidade do código é mais importante que a velocidade.

**ASSÍNCRONA**

  * Há múltiplas tarefas que dependem de I/O.
  * Lidar com várias conexões simultâneas.
  * O sistema precisa melhorar o tempo de resposta.
  * Tarefas podem ser executadas paralelamente sem dependerem uma das outras.

-----

### EXEMPLO DE USO: ENVIO DE E-MAIL DE CONFIRMAÇÃO

  * **SÍNCRONA:** Se o e-mail for enviado e o usuário precisa esperar a resposta de confirmação antes de continuar acessando o sistema.
  * **ASSÍNCRONA:** Se o e-mail for enviado em segundo plano enquanto o usuário segue usando o sistema.

-----

## A BIBLIOTECA ASYNCIO

Biblioteca padrão do Python para escrita de código assíncrono, usada para operações como:

  * Chamadas de API sem bloquear o programa.
  * Leitura e escrita de arquivos ou banco de dados.
  * Criar servidores e bots que precisam lidar com várias conexões simultaneamente.

-----

### CONCEITOS DO ASYNCIO

#### AWAITABLES (AGUARDÁVEIS)

É qualquer objeto que pode ser esperado com o `await`. Existem 3 tipos:

  * Corrotinas
  * Tarefas
  * Futuros

#### COROUTINES (CORROTINAS)

É uma função especial que pode ser pausada e retomada durante sua execução.

  * `async def` define a função como corrotina.
  * `await` pausa a execução para aguardar outra corrotina.


```python
import asyncio

async def corrotina(numero):
    print(f"Iniciando tarefa {numero}.")
    await asyncio.sleep(2)
    print(f"Tarefa {numero} concluída!")

async def main():
    await corrotina(1)
    await corrotina(2)

asyncio.run(main())
```

**Saída:**

``` 
Iniciando tarefa 1. 
 ...2 seg depois:
Tarefa 1 concluída! 
Iniciando tarefa 2. 
 ...2 seg depois:
Tarefa 2 concluída!
```

No código, apesar de usarmos a biblioteca **Asyncio**, a funcionalidade do nosso código está **síncrona**, porque a tarefa 1 é iniciada e após 2 segundos concluída, e só então ela passa para a próxima tarefa.

Isso se deve ao fato de que estamos usando **await** de forma **sequencial** na função main, ou seja, aguardamos a **corrotina** 1 finalizar completamente e depois iniciamos a corrotina 2. 

Quando utilizamos `await corrotina(1)` seguido de `await corrotina(2)`, o interpretador **suspende** a execução de main durante o primeiro await, retomando apenas quando a primeira corrotina termina. 

Somente após isso é que a segunda corrotina é chamada e executada. Essa abordagem elimina qualquer **concorrência** entre as tarefas, fazendo com que elas sejam executadas uma após a outra, resultando em um comportamento **síncrono** mesmo dentro de um contexto assíncrono.

Para as corrotinas trabalherem em **concorrencia** é necessartio usarmos tasks:

#### TASKS (TAREFAS)

É um objeto que executa uma corrotina de forma concorrente, permitindo que múltiplas corrotinas rodem juntas. `asyncio.create_task()` é usado para criar uma tarefa.

```python
import asyncio

async def corrotina(numero):
    print(f"Iniciando tarefa {numero}.")
    await asyncio.sleep(2)
    print(f"Tarefa {numero} concluída!")

async def main():
    tarefa1 = asyncio.create_task(corrotina(1))
    tarefa2 = asyncio.create_task(corrotina(2))

    await tarefa1
    await tarefa2

asyncio.run(main())
```

**Saída:**

```
Iniciando tarefa 1.
Iniciando tarefa 2.
Tarefa 1 concluída!
Tarefa 2 concluída!
```

#### FUTURE (FUTUROS)

É um objeto que representa um valor que ainda não está pronto e que será definido no futuro, usado em integração com APIs de baixo nível.

```python
import asyncio

async def corrotina1(futuro):
    print("Tarefa 1 iniciada.")
    await asyncio.sleep(2)
    futuro.set_result("Resultado da Tarefa 1")
    print("Tarefa 1 finalizada.")

async def corrotina2(futuro):
    print("Tarefa 2 iniciada, aguardando o futuro.")
    resultado = await futuro
    print(f"Tarefa 2 finalizada com o resultado: {resultado}")

async def main():
    futuro = asyncio.Future()
    tarefa1 = asyncio.create_task(corrotina1(futuro))
    tarefa2 = asyncio.create_task(corrotina2(futuro))
    
    await tarefa1
    await tarefa2

asyncio.run(main())
```

**Saída:**

```
Tarefa 1 iniciada.
Tarefa 2 iniciada, aguardando o futuro.
Tarefa 1 finalizada.
Tarefa 2 finalizada com o resultado: Resultado da Tarefa 1
```

-----

### EXECUTANDO MÚLTIPLAS TAREFAS

Você pode executar várias tarefas assíncronas utilizando `asyncio.gather()`.

```python
import asyncio

async def corrotina(nome, tempo):
    print(f"Tarefa {nome} iniciada.")
    await asyncio.sleep(tempo)
    print(f"Tarefa {nome} concluída.")

async def main():
    await asyncio.gather(
        corrotina("1", 2),
        corrotina("2", 3),
        corrotina("3", 1)
    )

asyncio.run(main())
```

**Saída:**

```
Tarefa 1 iniciada.
Tarefa 2 iniciada.
Tarefa 3 iniciada.
Tarefa 3 concluída.
Tarefa 1 concluída.
```

-----


