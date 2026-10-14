"""
DESAFIO 04: REFATORAÇÃO INVESTIGATIVA
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
O código monolítico repete cálculos de desconto e impostos várias vezes.

SUA MISSÃO:
1. Crie uma função calcular_preco_final(preco_base, taxa_desc, taxa_imp) com return.
2. Crie um procedimento exibir_relatorio_item(numero_item, preco_final) com print.
3. Teste suas funções refatoradas.
"""

# TODO: Desenvolva as funções modulares abaixo:

def calcular_preco_final(preco_base, taxa_desc, taxa_imp):
    valor_final=preco_base-(preco_base*taxa_desc)+(preco_base*taxa_imp)
    return valor_final
def exibir_relatorio_item(numero_item,preco_final):
    print(f"O número do item é:{numero_item}, e o preço final é:{preco_final}")

preco_base= float(input("Digite o preço base: "))
taxa_desc= float(input('Digite a porcentagem de desconto em decimos(10% = 0.10): '))
taxa_imp= float(input("Digite a porcentagem de imposto em decimos(10% = 0.10): "))
numero_item= int(input("Digite o número do item: "))
preço_final=calcular_preco_final(preco_base,taxa_desc,taxa_imp)
print(exibir_relatorio_item(numero_item,preço_final))