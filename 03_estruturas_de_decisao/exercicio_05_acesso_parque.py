"""
EXERCÍCIO 05: Acesso à Bilheteria do Parque
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba a idade do visitante (valor base do ingresso: R$ 100,00):
- Menor que 12 anos: "Infantil" (50% de desconto -> R$ 50,00)
- Maior ou igual a 60 anos: "Melhor Idade" (Gratuidade -> R$ 0,00)
- Demais idades: "Integral" (R$ 100,00)

Imprima o tipo de bilhete e o valor final a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
idade = int(input("Qual a idade do(a) visitante? "))
ingresso_base = 100
if idade<12 :
    infantil = ingresso_base - (ingresso_base*0.5)
    print(f"O seu ingresso é o Infantil e o valor é:R${infantil}")
elif idade >= 60:
    melhor_idade = 0
    print(f"O seu ingresso é o Melhor Idade e o valor é: R${melhor_idade:.2f}")
else:
    integral = ingresso_base
    print(f"O Seu ingresso é o Integral e o valor do seu ingresso é:R${integral}")