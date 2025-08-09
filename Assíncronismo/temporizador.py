"""
Crie um código em Python que simule um **temporizador assíncrono** de 3 segundos. O programa deve exibir "Iniciando temporizador..." imediatamente, aguardar 3 segundos usando **asyncio.sleep()**, e depois exibir "Tempo finalizado após 3 segundos!". Use **async/await** para implementar a funcionalidade assíncrona.
"""

import asyncio


async def temporizador():
    print("Iniciando temporizador...")
    await asyncio.sleep(3)
    print("Tempo finalizado após 3 segundos!")


asyncio.run(temporizador())
