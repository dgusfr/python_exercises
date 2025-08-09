"""
Crie um código em Python que simule um **sistema de notificações assíncronas** para três usuários com diferentes configurações. O programa deve ter uma **corrotina** que processa cada usuário baseado em seu **status** (VIP ou comum) e **preferência de notificação** (ativada ou desativada). Use **asyncio.gather()** para processar todos os usuários **simultaneamente**.

Requisitos:
- **Ana**: VIP com notificações ativadas (recebe notificação prioritária)
- **João**: Usuário comum com notificações ativadas (recebe notificação normal)
- **Carla**: Usuário comum com notificações desativadas (não recebe nada)

Saída esperada:
```
Enviando notificações...
Notificação VIP para Ana enviada!
Notificação normal para João enviada!
Carla desativou as notificações. Nada foi enviado.
Todas as notificações foram processadas!
```
"""
