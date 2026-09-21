"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
2 - X-Salada: R$ 4.50
3 - X-Bacon: R$ 5.00
4 - Torrada Simples: R$ 2.00
5 - Refrigerante: R$ 1.50

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
codigo = int(input("digite o código do produto consumido: "))
quantidade = int(input("digite a quantidade de produtos consumidos: "))
hotdog = 4.00
xsalada = 4.50
xbacon = 5.00
torrada = 2.00
refrigerante = 1.50
if codigo == 1 :
    valor = hotdog * quantidade
    print(f"O valor a ser pago é:R${valor:.2f}")
elif quantidade<0 :
    print("Quantidade Inválida")
elif codigo == 2 :
    valor = xsalada * quantidade
    print(f"O valor a ser pago é:R${valor:.2f}")
elif codigo == 3 :
    valor = xbacon * quantidade
    print(f"O valor a ser pago é:R${valor:.2f}")
elif codigo == 4 :
    valor = torrada * quantidade
    print(f"O valor a ser pago é:R${valor:.2f}")
elif codigo == 5 :
    valor = refrigerante * quantidade
    print(f"O valor a ser pago é:R${valor:.2f}")
else:
    print("Código Inválido")