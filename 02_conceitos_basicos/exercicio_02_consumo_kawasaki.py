"""
EXERCÍCIO 02: Consumo da Kawasaki Versys 300
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Para planejar uma viagem técnica de Tianguá até o Beach Park (Aquiraz),
solicite:
1. A distância total percorrida (em Km).
2. O total de combustível gasto (em Litros).

Calcule e imprima o consumo médio da motocicleta (Km/L) formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
distancia_total = float(input("Qual a distancia percorrida (em Km)? "))
combustivel_total = float(input("Qual o total de combustível gasto (em litros)? "))
consumo_medio = float(distancia_total/combustivel_total)
(print(f"O consumo médio é:{consumo_medio:.2f}Km/L"))