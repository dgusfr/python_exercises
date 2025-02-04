# Python

Repositório contendo diversos exercícios de programação em Python, abordando desde conceitos básicos até tópicos mais avançados, além disso ele tambem possui.

Este projeto foi desenvolvido com o objetivo de consolidar o aprendizado em Python por meio de práticas e exercícios.



<div style="display: flex; flex-direction: row;">
  <div style="margin-right: 20px; display: flex; justify-content: flex-start;">
    <img src="img/python.png" alt="Logo Python" width="100"/>
  </div>
</div>

## Status

![Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge)


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

## Autor

Desenvolvido por Diego Franco
