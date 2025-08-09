"""
Você foi contratado para desenvolver um sistema de apostas esportivas assíncrono. Os jogadores fazem suas apostas em jogos de futebol, mas os resultados só são revelados depois de um tempo aleatório, simulando a espera real por um resultado.

Nesta tarefa, você deve:

Criar um sistema onde cada aposta é armazenada em um asyncio.Future() e só é definida após um tempo determinado;
Simular três jogos diferentes, nos quais os apostadores fizeram suas apostas;
O resultado de cada jogo será "Vitória do Time A", "Vitória do Time B" ou "Empate", escolhido aleatoriamente;
Cada jogo levará entre 2 e 8 segundos para ter seu resultado definido;
O programa não deve esperar cada aposta individualmente, ele deve registrar todas e continuar rodando;
Assim que um resultado for definido, ele deve ser exibido imediatamente;
Quando todos os jogos forem finalizados, o programa exibe a mensagem "Todos os resultados foram revelados!".
Variáveis pré-definidas:

jogos = [
    {"id": 1, "times": "Flamengo vs Palmeiras"},
    {"id": 2, "times": "São Paulo vs Corinthians"},
    {"id": 3, "times": "Grêmio vs Internacional"},
]

RESULTADOS = ["Vitória do Time A", "Vitória do Time B", "Empate"]
Copiar código
Saída esperada:

Aposta no jogo 1 (Flamengo vs Palmeiras) registrada! Aguardando resultado...
Aposta no jogo 2 (São Paulo vs Corinthians) registrada! Aguardando resultado...
Aposta no jogo 3 (Grêmio vs Internacional) registrada! Aguardando resultado...

Aposta no jogo 2 definida: Vitória do Corinthians (após 3s).
Aposta no jogo 1 definida: Empate (após 5s).
Aposta no jogo 3 definida: Vitória do Grêmio (após 7s).

Todos os resultados foram revelados!
"""
