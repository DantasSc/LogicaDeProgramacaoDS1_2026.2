"""
EXERCÍCIO 02: Aumento de Salário Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de um colaborador da escola e aplique o percentual de reajuste:
- 0.00 a 400.00: 15%
- 400.01 a 800.00: 12%
- 800.01 a 1200.00: 10%
- 1200.01 a 2000.00: 7%
- Acima de 2000.00: 4%

Imprima: novo salário, valor do reajuste ganho e percentual aplicado.
"""

# TODO: Desenvolva o algoritmo abaixo:
salario=float(input("Qual o seu salário? "))
#percentuais
percentual01 = "15%"
percentual02 = "12%"
percentual03= "10%"
percentual04 = "7%"
percentual05 = "4%"
#Valores reajustes
reajuste01 = salario * 0.15
reajuste02 = salario * 0.12
reajuste03 = salario * 0.10
reajuste04 = salario * 0.07
reajuste05 = salario * 0.04
#Salarios Novos
salario01 = salario + reajuste01
salario02 = salario + reajuste02
salario03 = salario + reajuste03
salario04 = salario + reajuste04
salario05 = salario + reajuste05
if salario>=0.00 and salario<=400.00 :
    print(f"O seu novo salário é: R${salario01:2.f} ,o reajuste foi de R${reajuste01:.2f},e o percentual aplicado foi {percentual01}")
elif salario>=400.01 and salario<=800.00 :
    print(f"O seu novo salário é: R${salario02:.2f} ,o reajuste foi de R${reajuste02:.2f},e o percentual aplicado foi {percentual02}")
elif salario>=800.01 and salario<=1200.00 :
    print(f"O seu novo salário é: R${salario03:.2f} ,o reajuste foi de R${reajuste03:.2f},e o percentual aplicado foi {percentual03}")
elif salario>=1200.01 and salario<=2000.00 :
    print(f"O seu novo salário é: R${salario04:.2f} ,o reajuste foi de R${reajuste04:.2f},e o percentual aplicado foi {percentual04}")
else:print(f"O seu novo salário é: R${salario05:.2f} ,o reajuste foi de R${reajuste05:.2f},e o percentual aplicado foi {percentual05}")