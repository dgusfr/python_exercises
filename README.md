# Python

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

# Lista de Exercícios – Python Básico e Estrutura de Dados


1. Leia três números inteiros, calcule a média aritmética simples e informe se cada número está abaixo, acima ou exatamente na média, apresentando os resultados em uma única linha organizada.

2. Solicite o valor de um investimento inicial, a taxa de juros anual e o número de anos, então calcule e mostre o montante anual acumulado usando juros compostos, imprimindo uma linha para cada ano com o saldo atualizado.

3. Crie um programa que solicite dois números inteiros e uma operação matemática (`+`, `-`, `*`, `/`). Execute a operação escolhida e exiba o resultado. Utilize tratamento de exceções para divisões por zero e entradas inválidas.

4. Solicite ao usuário seu nome completo e idade. Imprima uma saudação personalizada e informe em que ano ele completará 100 anos.

5. Faça um programa que receba uma lista de 5 nomes digitados pelo usuário, ordene-os alfabeticamente e exiba o resultado com uma numeração.

6. Crie uma função `classificar_idade()` que recebe a idade como parâmetro e retorna se a pessoa é "criança", "adolescente", "adulto" ou "idoso". Utilize essa função com dados lidos do usuário.

7. Crie um dicionário para armazenar dados de um livro: título, autor, ano e número de páginas. Solicite os dados ao usuário e, ao final, exiba o dicionário formatado.

8. Solicite um número inteiro positivo e use um laço `for` para imprimir todos os números pares de 0 até esse número, inclusive.

9. Crie uma lista de números inteiros e utilize um laço `for` para imprimir a soma acumulada dos elementos, passo a passo, linha por linha.

10. Escreva uma função chamada `dividir()` que receba dois números como parâmetros, realize a divisão e trate o caso de divisão por zero com um `try/except`.

11. Solicite uma sequência de números separados por vírgula. Converta a entrada para uma lista de inteiros, remova duplicatas usando um `set` e exiba os valores únicos ordenados.

12. Dada uma tupla com cinco notas de um aluno, calcule a média e informe se ele foi aprovado (média ≥ 6), exibindo também a maior e menor nota.

13. Crie um dicionário com o nome de três cidades como chaves e suas temperaturas atuais como valores. Depois, exiba qual cidade está mais quente e qual está mais fria.

14. Faça um programa que simula um menu de opções com `while`: o usuário pode digitar `1` para adicionar um nome a uma lista, `2` para listar os nomes, `0` para sair. O menu deve se repetir até que o usuário digite `0`.

15. Escreva uma função `conversor_temperatura()` que receba um valor em Celsius e retorne o valor correspondente em Fahrenheit. Peça ao usuário a temperatura e exiba o resultado usando a função.

---

media_tres_numeros.py

juros_compostos_anuais.py

calculadora_simples_com_excecoes.py

ano_cem_anos.py

ordenar_nomes_lista.py

classificacao_idade_funcao.py

dicionario_dados_livro.py

pares_ate_numero.py

soma_acumulada_lista.py

divisao_com_tratamento.py

lista_unica_ordenada.py

avaliacao_aluno_tupla.py

temperatura_cidades.py

menu_interativo_nomes.py

conversor_celsius_fahrenheit.py

---


## Autor

Desenvolvido por Diego Franco

