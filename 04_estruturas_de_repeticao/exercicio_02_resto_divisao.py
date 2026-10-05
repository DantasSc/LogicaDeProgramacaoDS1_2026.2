"""
EXERCÍCIO 02: Resto da Divisão por 5
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia dois valores inteiros X e Y.
Utilize o laço for para imprimir todos os inteiros entre X e Y (em ordem crescente)
cujo resto da divisão por 5 seja igual a 2 ou igual a 3.
"""

# TODO: Desenvolva o algoritmo abaixo:
valor_x = int(input("Digite um valor: "))
valor_y = int(input("Digite outro valor: "))

if valor_x > valor_y:
    valor_x, valor_y = valor_y,valor_x
for i in range(valor_x,valor_y+1):
    if i%5 ==2 or i%5 ==3:
        print(i)
