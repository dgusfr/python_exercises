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


## 5. Exercício Sugerido

Crie uma lista com tuplas representando produtos: `(nome, preço)`. Use `sorted()` com uma função lambda para ordenar os produtos pelo preço, do menor para o maior, e imprima o resultado formatado.

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
````

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

## 6. Exercício Sugerido

Crie uma classe `IntervaloPares` que recebe dois números inteiros (início e fim). Ela deve ser um iterador que retorna **apenas os números pares** entre esses valores, inclusive.

Use-a com um `for` para imprimir os pares de 2 a 10.

---









## Autor

Desenvolvido por Diego Franco

