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
* `str` ou `string` (textos)
* `bool` (valores booleanos: `True` ou `False`)

### Strings em Python

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

#### Formatação com f-strings

As f-strings (strings formatadas) são a maneira moderna e legível de incorporar variáveis e expressões diretamente dentro de uma string. A sintaxe utiliza a letra `f` antes das aspas.

```python
estudante = "Pedro"
nota = 10

# A variável é colocada entre chaves {} dentro da string.
mensagem = f"{estudante} tirou a nota {nota}!"
print(mensagem) # Saída: Pedro tirou a nota 10!
```

-----

#### Acessando Partes de uma String

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

#### Métodos de Manipulação e Verificação

##### Limpeza e Formatação de Caixa

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
#  
print(exemplo.lower()) # Saída: "  olá mundo  "

# .upper() converte todos os caracteres para maiúsculas.
print(exemplo.upper()) # Saída: "  OLÁ MUNDO  "

# .replace() substitui uma substring por outra.
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


Laços são estruturas de código que permitem executar um bloco de código repetidamente enquanto uma condição for verdadeira. Em Python, as principais estruturas de laço são `for` e `while`. 

A lógica de um laço pode ser entendida como: repita uma ação até que a condição de parada se torne falsa. 

#### Laço `for`

O laço `for` é utilizado para percorrer os itens de uma coleção de dados (iterável), como listas ou tuplas. Ele é ideal para situações em que o número de repetições é conhecido previamente. 

```python
nomes = ["Carlos", "Ana", "Pedro", "Maria"] 

for nome in nomes: 
  print(nome) 
```

Neste código, o laço `for` itera sobre a lista `nomes`, executando o comando `print(nome)` para cada um dos seus elementos. A palavra `in` e os dois pontos (`:`) na sintaxe são obrigatórios. 

#### Laço `while`

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


