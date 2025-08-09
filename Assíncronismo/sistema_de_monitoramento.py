"""
Crie um código em Python que implemente um **sistema de monitoramento de tarefas assíncronas** com três tarefas executando **simultaneamente** em tempos diferentes (3, 5 e 7 segundos). O programa deve usar **asyncio.create_task()** para executar as tarefas em **paralelo** e implementar um **loop de monitoramento** que verifica o **status** de todas as tarefas a cada segundo.

Requisitos:
- **Três tarefas** com tempos fixos: 3s, 5s e 7s
- **Monitor assíncrono** que verifica o status a cada segundo usando **asyncio.sleep(1)**
- Exibir **lista de status** das tarefas: `['Em andamento', 'Finalizado']`
- Mostrar **mensagem de finalização** quando cada tarefa terminar
- O programa termina apenas quando **todas as tarefas** estiverem concluídas

Use **asyncio.gather()** ou **asyncio.wait()** para aguardar a conclusão de todas as tarefas enquanto o monitoramento acontece em paralelo.

Saída esperada:
```
Status das tarefas: ['Em andamento', 'Em andamento', 'Em andamento']
Status das tarefas: ['Em andamento', 'Em andamento', 'Em andamento']
Status das tarefas: ['Em andamento', 'Em andamento', 'Em andamento']
Tarefa 1 finalizada!
Status das tarefas: ['Finalizado', 'Em andamento', 'Em andamento']
Status das tarefas: ['Finalizado', 'Em andamento', 'Em andamento']
Tarefa 2 finalizada!
Status das tarefas: ['Finalizado', 'Finalizado', 'Em andamento']
Status das tarefas: ['Finalizado', 'Finalizado', 'Em andamento']
Tarefa 3 finalizada!
```
"""
