"""
EXERCÍCIO 03: Pares entre Cinco Números
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite 5 números inteiros ao usuário.
Utilize uma estrutura de repetição e um contador para verificar quantos números pares
foram digitados. Ao final, imprima a quantidade total.
"""

# TODO: Desenvolva o algoritmo abaixo:
soma = 0
for num in range(1,6):
    numero = int(input("Digite um numero: "))
    if numero%2 ==0:
        soma +=1
print(f"Dos números digitados há {soma} números pares!")