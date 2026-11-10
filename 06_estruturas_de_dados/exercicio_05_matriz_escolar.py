"""
EXERCÍCIO 05: Matriz Bidimensional Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma matriz com 3 alunos [nome, nota1, nota2].
Percorra a matriz, calcule a média de cada um e exiba:
"Aluno: [Nome] | Média: [Média] | Situação: [Aprovado / Prova Final]"
(Critério: Média >= 6.0 aprovado).
"""

# TODO: Desenvolva o algoritmo abaixo:
alunos = [
    ["Ryan", 8.0, 6.0],
    ["Dantas", 9.0, 8.0],
    ["Lucas", 5.0, 3.0]
]
for media in alunos:
    aluno=media[0]
    media=(media[1]+media[2])/2
    if media>=6.0:
        situacao="Aprovado"
    else:
        situacao="Recuperação"
    print(f"Aluno:{aluno}| Média:{media}| Situação:{situacao}")