"""
Crie um código em Python que execute duas **tarefas concorrentes** usando **asyncio**. O programa deve ter duas **corrotinas**: uma que simula um download (aguarda 2 segundos) e outra que simula análise de dados (aguarda 3 segundos). Ambas devem ser iniciadas **simultaneamente** usando **asyncio.gather()** e exibir mensagens no início e fim de cada tarefa.

Saída esperada:
```
Iniciando download...
Iniciando análise de dados...
Download concluído!
Análise de dados concluída!
```
"""

import asyncio


async def download():
    print("Iniciando download...")
    await asyncio.sleep(2)
    print("Download concluído!")


async def analise_de_dados():
    print("Iniciando análise de dados...")
    await asyncio.sleep(3)
    print("Análise de dados concluída!")


async def main():
    await asyncio.gather(download(), analise_de_dados())


asyncio.run(main())
