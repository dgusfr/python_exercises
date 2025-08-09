"""
Crie um código em Python que implemente um **sistema de processamento de pedidos assíncrono** para uma loja online. O programa deve processar uma lista de pedidos **simultaneamente** usando **asyncio.gather()**, seguindo a lógica: verificar **pagamento aprovado**, depois **estoque disponível**, e só então **confirmar o pedido**. Caso alguma condição falhe, o pedido deve ser **cancelado**.

Use a seguinte lista de pedidos:
```python
pedidos = [
    {"id": 101, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 102, "pagamento_aprovado": True, "estoque_disponivel": False},
    {"id": 103, "pagamento_aprovado": False, "estoque_disponivel": True},
    {"id": 104, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 105, "pagamento_aprovado": False, "estoque_disponivel": False},
]
```

Crie uma **corrotina** que processe cada pedido individualmente, exibindo mensagens para cada etapa do processamento.

Saída esperada:
```
Processando pedido #101...
Pagamento aprovado para pedido #101.
Estoque disponível para pedido #101.
Pedido #101 confirmado! Enviado para entrega.

Processando pedido #102...
Pagamento aprovado para pedido #102.
Estoque indisponível para pedido #102. Pedido cancelado.

Processando pedido #103...
Pagamento recusado para pedido #103. Pedido cancelado.

Todos os pedidos foram processados!
```
"""
