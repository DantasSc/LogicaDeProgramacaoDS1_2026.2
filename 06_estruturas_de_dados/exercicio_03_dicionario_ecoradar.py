"""
EXERCÍCIO 03: Dicionário da Equipe EcoRadar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Estruture um dicionário com 3 membros (matrícula -> cargo).
Leia uma matrícula via terminal e exiba a função correspondente cadastrada.
"""

# TODO: Desenvolva o algoritmo abaixo:
membros={
    "001":"Desenvolvedor",
    "002":"Designer",
    "003":"Analista de dados"
}
matricula = input("Digite sua matrícula: ")

print(f"Seu Cargo é:{membros[matricula]}")