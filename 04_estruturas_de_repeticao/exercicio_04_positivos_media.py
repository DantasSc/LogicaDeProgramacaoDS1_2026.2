"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
positivos = 0 
numerador = 0
for i in range(1,7) :
    numero = int(input("Digite um número: "))
    if numero >0:
        positivos +=1
        numerador +=numero
if positivos > 0 :
    media =numerador/positivos
    print(f"Sua média é:{media:.1f}")
else:
    print("Não há Média")
print(f"teve {positivos} números positivos")