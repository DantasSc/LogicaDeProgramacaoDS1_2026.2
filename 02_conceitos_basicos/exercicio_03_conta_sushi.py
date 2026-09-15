"""
EXERCÍCIO 03: Conta do Nagoya Sushi House
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie um programa que:
1. Leia o valor total consumido no restaurante (em R$).
2. Aplique a taxa de 10% de serviço do garçom.
3. Exiba o valor final da conta a pagar com mensagem formatada.
"""

# TODO: Desenvolva o algoritmo abaixo:
valor_total = float(input("Qual o valor total consumido (em R$)? "))
taxa = valor_total*0.1
valor_final = valor_total + taxa
print(f"O valor total a ser pago é:R${valor_final:.2f}")