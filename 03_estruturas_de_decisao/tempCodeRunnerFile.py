EXERCÍCIO 01: Imposto de Renda de Lisarb
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de uma pessoa em Rombus (R$).
- Até R$ 2000.00: Isento
- De R$ 2000.01 até R$ 3000.00: 8% sobre o excedente de R$ 2000.00
- De R$ 3000.01 até R$ 4500.00: 18% sobre o excedente de R$ 3000.00 + 8% da faixa anterior
- Acima de R$ 4500.00: 28% sobre o que ultrapassar R$ 4500.00 + impostos anteriores

Imprima "Isento" ou o valor total do imposto formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
salario = float(input("Qual o seu salário? "))

if salario>=0 and salario<=2000.00:
    print(f"Você está isento do imposto")
elif salario>=2000.01 and salario<=3000.00:
    salario = (salario-2000)*0.08
    print(f"O seu imposto é igual a R$ {salario:.2f}")
elif salario>=3000.01 and salario<=4500.00:
    salario = ((salario-3000)*0.18)+80
    print(f"O seu imposto é igual a R$ {salario:.2f}")
else:
    salario = ((salario-4500)*0.28)+350
    print(f"O seu imposto é igual a R$ {salario:.2f}")