"""
Crie um código em Python que implemente um **sistema de inscrições assíncronas** para uma plataforma de ensino online. O programa deve processar múltiplas inscrições **simultaneamente** usando **asyncio.gather()**, seguindo as regras: verificar **vagas disponíveis**, verificar se o aluno **já está inscrito**, e só então **confirmar a inscrição** ou **rejeitar** conforme apropriado.

Use os seguintes dados:
```python
cursos = {
    "Python Avançado": {"vagas": 2, "inscritos": []},
    "Java para Iniciantes": {"vagas": 1, "inscritos": []},
    "Machine Learning": {"vagas": 0, "inscritos": []},
}

alunos = [
    {"nome": "Alice", "curso": "Python Avançado"},
    {"nome": "Bruno", "curso": "Python Avançado"},
    {"nome": "Carlos", "curso": "Java para Iniciantes"},
    {"nome": "Daniela", "curso": "Machine Learning"},
    {"nome": "Alice", "curso": "Python Avançado"},  # Tentativa de inscrição duplicada
]
```

Crie uma **corrotina** que processe cada inscrição individualmente, verificando **duplicatas**, **vagas disponíveis** e atualizando a lista de **inscritos** quando necessário.

Saída esperada:
```
Inscrevendo Alice no curso Python Avançado...
Inscrição confirmada para Alice no curso Python Avançado!

Inscrevendo Bruno no curso Python Avançado...
Inscrição confirmada para Bruno no curso Python Avançado!

Inscrevendo Carlos no curso Java para Iniciantes...
Inscrição confirmada para Carlos no curso Java para Iniciantes!

Inscrevendo Daniela no curso Machine Learning...
Turma lotada! Daniela não pôde se inscrever no curso Machine Learning.

Inscrevendo Alice no curso Python Avançado...
Alice já está inscrita no curso Python Avançado! Inscrição rejeitada.

Todas as inscrições foram processadas!
```
"""
