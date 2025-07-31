
# Programação Síncrona

No modelo síncrono, as tarefas são executadas em sequência. Uma operação deve ser concluída antes que a próxima possa começar.

É usado quando o programa é simples e sequencial; quando há pouca entrada e saida de dados e a simplicidade do codigo é mais importante que a velocidade.

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

**Saída:** A execução é bloqueada a cada chamada, uma tarefa após a outra.

```
Iniciando tarefa 1.
Tarefa 1 concluída!
Iniciando tarefa 2.
Tarefa 2 concluída!
```

# Programação Assíncrona, Concorrência e Paralelismo

  * **Programação Assíncrona**: Permite que um programa execute várias tarefas ao mesmo tempo, sem que uma precise esperar a outra terminar.

  É usado quando temos várias entradas e saidas de dados; é necessário lidar com conexões simultanes; as tarefas podem ser executadas em paralelo sem dependerem umas das outras.

  * **Concorrência**: É a alternância rápida entre tarefas, dando a impressão de que rodam ao mesmo tempo. É ideal para operações de I/O (API, banco de dados). 
  
  Analogia: é um único garçom que anota um pedido, envia para a cozinha e atende outro cliente enquanto o primeiro prato é preparado.
  
  * **Paralelismo**: É a execução de múltiplas tarefas verdadeiramente ao mesmo tempo, geralmente em diferentes núcleos de CPU. 
  
  É ideal para cálculos pesados e processamento de dados. A analogia são vários garçons atendendo clientes diferentes simultaneamente.

## A Biblioteca `asyncio` e os Awaitables

`asyncio` é a biblioteca padrão do Python para código assíncrono. Ela gerencia um "loop de eventos" que executa objetos do tipo **Awaitable** (aguardáveis). 


Existem 3 tipos principais:

### 1. Corrotinas (`async def`)

É uma função especial declarada com `async def` que pode ser pausada e retomada. 

A palavra-chave `await` pausa a corrotina e devolve o controle ao loop de eventos para que outra tarefa possa ser executada.

```python
import asyncio

async def corrotina(numero):
    print(f"Iniciando tarefa {numero}.")
    await asyncio.sleep(2)
    print(f"Tarefa {numero} concluída!")

  #Continua a baixo...
```

**Importante**: Usar `await` de forma sequencial não gera concorrência. No código abaixo, `corrotina(2)` só inicia após `corrotina(1)` ter finalizado completamente.

```python
async def main():
    await corrotina(1) # Espera a corrotina 1 terminar
    await corrotina(2) # Só então executa a corrotina 2

asyncio.run(main())
```


**Saída:** O resultado é sequencial, `similar ao síncrono`.

```
Iniciando tarefa 1.
Tarefa 1 concluída!
Iniciando tarefa 2.
```

### 2. Tasks (Tarefas)

Uma `Task` é um objeto que agenda uma corrotina para ser executada de forma **concorrente** . Usa-se `asyncio.create_task()` para agendar a execução da corrotina imediatamente, sem bloqueá-la.

```python
import asyncio

async def corrotina(numero):
    print(f"Iniciando tarefa {numero}.")
    await asyncio.sleep(2)
    print(f"Tarefa {numero} concluída!")

async def main():
    # As tarefas são agendadas e começam a rodar em segundo plano
    tarefa1 = asyncio.create_task(corrotina(1))
    tarefa2 = asyncio.create_task(corrotina(2))
    
    # O await aqui apenas espera as tarefas já iniciadas terminarem
    await tarefa1
    await tarefa2

asyncio.run(main())
```

Ao usar `asyncio.create_task()`, as funções `corrotina` são agendadas para rodarem em paralelo no *event loop*. 

O `await tarefa1` e `await tarefa2` garantem que o programa só prossiga depois que **ambas as tarefas tenham sido concluídas**, permitindo que elas finalizem ao mesmo tempo ou em ordem diferente, dependendo do *scheduler*. 

**Saída:** Ambas as tarefas iniciam juntas, demonstrando a concorrência.

```
Iniciando tarefa 1.
Iniciando tarefa 2.
Tarefa 1 concluída!
Tarefa 2 concluída!
```

Isso demonstra como o `asyncio.create_task` permite iniciar e gerenciar múltiplas operações que podem ser executadas "simultaneamente" dentro do contexto assíncrono.

### 3. Futures (Futuros)

Um `Future` é um objeto que representa um resultado que ainda não está disponível. É um mecanismo de baixo nível usado para comunicação entre tarefas, onde uma tarefa pode esperar pelo resultado que outra tarefa irá definir.

No exemplo abaixo, o código usa `asyncio.Future` para **comunicação entre corrotinas**. `corrotina1` define um **resultado** no `Future` após 2 segundos, e `corrotina2` **aguarda** esse `Future` para obter o resultado antes de prosseguir. Isso sincroniza as tarefas, onde uma depende do valor gerado pela outra.

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
    print("Tarefa 2 finalizada com o resultado:", resultado)

async def main():
    futuro = asyncio.Future()
    tarefa1 = asyncio.create_task(corrotina1(futuro))
    tarefa2 = asyncio.create_task(corrotina2(futuro))
    
    await tarefa1
    await tarefa2

asyncio.run(main())
```

**Saída:** A `Tarefa 2` fica pausada até que a `Tarefa 1` publique o resultado no objeto `futuro`.

```
Tarefa 1 iniciada.
Tarefa 2 iniciada, aguardando o futuro.
Tarefa 1 finalizada.
Tarefa 2 finalizada com o resultado: Resultado da Tarefa 1
```

### 4\. Executando Múltiplas Tarefas com `asyncio.gather`

[cite\_start]`asyncio.gather()` é uma forma de alto nível para executar várias corrotinas concorrentemente e aguardar que todas terminem[cite: 186, 187]. É uma maneira mais limpa de realizar o que `create_task` faz para múltiplas tarefas.

```python
async def main():
    await asyncio.gather(
        corrotina("1", 2),
        corrotina("2", 3),
        corrotina("3", 1)
    )
```

[cite\_start]**Saída:** Todas as tarefas iniciam ao mesmo tempo e terminam em ordens diferentes, dependendo do seu tempo de `sleep`[cite: 191, 192, 193, 194, 195, 196].

```
Tarefa 1 iniciada.
Tarefa 2 iniciada.
Tarefa 3 iniciada.
Tarefa 3 concluída.
Tarefa 1 concluída.
Tarefa 2 concluída.
```