"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
import math 

valor_a = float(input("digite o primeiro valor(A): "))
valor_b = float(input("digite o segundo valor(B): "))
valor_c = float(input("digite o terceiro valor(C): "))
delta = (valor_b**2)-(4*valor_a*valor_c)
if delta<0 or valor_a==0:
    print("Impossivel calcular")
else:
    bhaskara_r1 = (-valor_b + math.sqrt(delta))/(2*valor_a)
    bhaskara_r2 = (-valor_b - math.sqrt(delta))/(2*valor_a)
    print(f"A Primeira Raiz é {bhaskara_r1:.5f},e a segunda Raiz é {bhaskara_r2:.5f}")