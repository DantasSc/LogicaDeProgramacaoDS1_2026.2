# TODO: Implemente a tabuada aqui
numero_base = int(input("Digite um número para ver a tabuada: "))

# Escreva o laço for
for numero in range(1, 11):
    tabuada = numero_base * numero
    print(f"{numero_base}x{numero}={tabuada}")