"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:
def calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel):
    custo=(distancia_km/consumo_kml)*preco_combustivel
    return custo
def calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao):
    custo= qtd_pessoas*dias*diaria_alimentacao
    return custo
distancia= float(input("Digite a distância percorrida(Em km): "))
consumo = float(input("Digite a quantidade de combustível consumido: "))
preco_combustivel= float(input("Digite o preço do combustível: "))
pessoas= int(input('Digite a quantidade de pesssoas presentes na viagem: '))
dias= int(input("Digite a quantidade de dias de viagem: "))
alimentacao= float(input("Digite o valor da alimentação diária: "))
valor1=calcular_custo_transporte(distancia,consumo,preco_combustivel)
valor2=calcular_custo_alimentacao(pessoas,dias,alimentacao)
total= valor1+valor2
print(f"O valor total de transporte foi:{valor1}, e o valor total de alimentação foi:{valor2}, e o total é:{total}")