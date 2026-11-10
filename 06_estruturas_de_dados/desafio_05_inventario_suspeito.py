"""
DESAFIO 05: O INVENTÁRIO SUSPEITO DO LABORATÓRIO
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
Elimine duplicatas usando conjuntos (set) e previna o erro KeyError em dicionários
usando o método .get().

SUA MISSÃO:
1. Obtenha a lista de itens únicos a partir de uma lista com duplicatas.
2. Consulte chaves no dicionário de forma segura sem quebrar o programa.
"""

# TODO: Desenvolva o algoritmo abaixo:
itens = [
    "Microscópio",
    "Proveta",
    "Termômetro",
    "Microscópio",
    "Béquer",
    "Proveta",
    "Luvas",
    "Termômetro",
    "Béquer"
]
lista=set(itens)
laboratorio = {
    "Microscópio": 5,
    "Proveta": 12,
    "Termômetro": 3,
    "Béquer": 8,
    "Luvas": 20
}
print(lista)
print(f"Quantidade de Microscópios:{laboratorio.get("Microscópio")}")
print(f"Quantidade de Provetas:{laboratorio.get("Proveta")}")
print(f"Quantidade de Termômetros:{laboratorio.get("Termômetro")}")
print(f"Quantidade de Béquers:{laboratorio.get("Béquer")}")
print(f"Quantidade de Luvas:{laboratorio.get("Luvas")}")