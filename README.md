# Python

Repositório contendo diversos exercícios de programação em Python, abordando desde conceitos básicos até tópicos mais avançados, como funções recursivas e manipulação de dados.

Este projeto foi desenvolvido com o objetivo de consolidar o aprendizado em Python por meio de práticas e exercícios.

## Sumário

- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Status](#status)
- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Explicação](#explicação)
- [Como Usar](#como-usar)
- [Autor](#autor)

## Tecnologias Utilizadas

<div style="display: flex; flex-direction: row;">
  <div style="margin-right: 20px; display: flex; justify-content: flex-start;">
    <img src="img/python.png" alt="Logo Python" width="100"/>
  </div>
</div>

## Status

![Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge)

## Descrição

Este repositório contém uma coleção de exercícios de programação em Python.

Os exercícios abrangem diversos tópicos, desde tipos de dados e estruturas condicionais até funções recursivas e manipulação de strings.

Cada exercício tem como objetivo ajudar no desenvolvimento das habilidades de programação, explorando conceitos teóricos na prática.

## Funcionalidades

- Implementação de funções básicas e intermediárias.
- Simulação de cenários do mundo real, como sistemas de inventário e controle de tráfego.
- Utilização de bibliotecas integradas para funcionalidades específicas.
- Aplicação de algoritmos para cálculos matemáticos, manipulação de listas e dicionários.
- Classificação de alunos por média, manipulação de strings e cálculo de distâncias.

## Explicação

Cada exercício está implementado em Python e utiliza uma abordagem didática para solucionar o problema proposto.

A estrutura do código é planejada para ser de fácil compreensão, permitindo que o usuário aprenda conceitos importantes e veja exemplos de implementação.

Alguns dos tópicos abordados nos exercícios incluem:

- **Tipos de Dados:** Uso de listas, tuplas, dicionários e sets para organizar informações.
- **Estruturas Condicionais:** Implementação de decisões lógicas com `if`, `elif` e `else`.
- **Operadores e Funções:** Realização de operações matemáticas e definição de funções.
- **Loops:** Utilização de laços de repetição para percorrer listas e gerar sequências.
- **Funções Anônimas (Lambda):** Uso de expressões lambda para simplificar a lógica.
- **Funções Recursivas:** Resolução de problemas utilizando recursão.
- **Manipulação de Strings:** Processamento e modificação de textos.
- **Bibliotecas Integradoras:** Uso de `datetime` e `random` para funcionalidades específicas.

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
---



## Autor

Desenvolvido por Diego Franco
