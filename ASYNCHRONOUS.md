
# Programação Síncrona

No modelo síncrono, as tarefas são executadas em sequência. Uma operação deve ser concluída antes que a próxima possa começar.

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

### 2\. Programação Assíncrona, Concorrência e Paralelismo

  * [cite\_start]**Programação Assíncrona**: Permite que um programa execute várias tarefas ao mesmo tempo, sem que uma precise esperar a outra terminar[cite: 18].
  * [cite\_start]**Concorrência**: É a alternância rápida entre tarefas, dando a impressão de que rodam ao mesmo tempo[cite: 20]. [cite\_start]É ideal para operações de I/O (rede, disco)[cite: 21]. [cite\_start]A analogia é um único garçom que anota um pedido, envia para a cozinha e atende outro cliente enquanto o primeiro prato é preparado[cite: 30, 34].
  * [cite\_start]**Paralelismo**: É a execução de múltiplas tarefas verdadeiramente ao mesmo tempo, geralmente em diferentes núcleos de CPU[cite: 24, 25]. [cite\_start]É ideal para cálculos pesados e processamento de dados[cite: 26]. [cite\_start]A analogia são vários garçons atendendo clientes diferentes simultaneamente[cite: 32].

### 3\. A Biblioteca `asyncio` e os Awaitables

[cite\_start]`asyncio` é a biblioteca padrão do Python para código assíncrono[cite: 62]. [cite\_start]Ela gerencia um "loop de eventos" que executa objetos do tipo **Awaitable** (aguardáveis)[cite: 75]. Existem 3 tipos principais:

#### a. Corrotinas (`async def`)

[cite\_start]É uma função especial declarada com `async def` que pode ser pausada e retomada[cite: 89, 90]. [cite\_start]A palavra-chave `await` pausa a corrotina e devolve o controle ao loop de eventos para que outra tarefa possa ser executada[cite: 91].

**Importante**: Usar `await` de forma sequencial não gera concorrência. No código abaixo, `corrotina(2)` só inicia após `corrotina(1)` ter finalizado completamente.

```python
async def main():
    await corrotina(1) # Espera a corrotina 1 terminar
    await corrotina(2) # Só então executa a corrotina 2
```

[cite\_start]**Saída:** O resultado é sequencial, similar ao síncrono[cite: 106, 107, 108, 109].

```
Iniciando tarefa 1.
Tarefa 1 concluída!
Iniciando tarefa 2.
```

#### b. Tasks (Tarefas)

[cite\_start]Uma `Task` é um objeto que agenda uma corrotina para ser executada de forma concorrente[cite: 126]. Usa-se `asyncio.create_task()` para agendar a execução da corrotina imediatamente, sem bloqueá-la.

```python
async def main():
    # As tarefas são agendadas e começam a rodar em segundo plano
    tarefa1 = asyncio.create_task(corrotina(1))
    tarefa2 = asyncio.create_task(corrotina(2))
    
    # O await aqui apenas espera as tarefas já iniciadas terminarem
    await tarefa1
    await tarefa2
```

[cite\_start]**Saída:** Ambas as tarefas iniciam juntas, demonstrando a concorrência[cite: 129, 130].

```
Iniciando tarefa 1.
Iniciando tarefa 2.
Tarefa 1 concluída!
Tarefa 2 concluída!
```

#### c. Futures (Futuros)

[cite\_start]Um `Future` é um objeto que representa um resultado que ainda não está disponível[cite: 138]. É um mecanismo de baixo nível usado para comunicação entre tarefas, onde uma tarefa pode esperar pelo resultado que outra tarefa irá definir.

No exemplo abaixo, `corrotina2` aguarda (`await futuro`) até que `corrotina1` defina um resultado (`futuro.set_result(...)`).

```python
# corrotina1 define o resultado
async def corrotina1(futuro):
    await asyncio.sleep(2)
    [cite_start]futuro.set_result("Resultado da Tarefa 1") [cite: 153]

# corrotina2 espera pelo resultado
async def corrotina2(futuro):
    print("Tarefa 2 iniciada, aguardando o futuro.")
    [cite_start]resultado = await futuro [cite: 156]
    print(f"Tarefa 2 finalizada com o resultado: {resultado}")
```

[cite\_start]**Saída:** A `Tarefa 2` fica pausada até que a `Tarefa 1` publique o resultado no objeto `futuro`[cite: 170, 171, 172].

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