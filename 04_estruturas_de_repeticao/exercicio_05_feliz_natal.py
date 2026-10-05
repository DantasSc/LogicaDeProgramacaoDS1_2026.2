"""
EXERCÍCIO 05: Feliz Nataaal!
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba um número inteiro I (nível de empolgação).
Utilize repetição para exibir a frase "Feliz natal!" repetindo a letra 'a'
da palavra natal exatamente I vezes (ex: I=5 -> "Feliz nataaaal!").
"""

# TODO: Desenvolva o algoritmo abaixo:
quantidade=0
i = int(input("Digite o seu nivel de empolgação(Em números inteiros): "))

quant_a = ''
for quant in range(1,i):
    quant_a += "a"
print(f"Feliz Nat{quant_a}l!")
