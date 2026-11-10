# TODO: Crie a matriz 2x2 e calcule a soma
matriz = [
    [],
    []
]
for i in range(2):
    numero=int(input("Digite um número: "))
    matriz[0].append(numero)
for i in range(2):
    numero=int(input("Digite um número: "))
    matriz[1].append(numero)
# Escreva a lógica de soma aqui
n1=matriz[0][0]
n2=matriz[0][1]
n3=matriz[1][0]
n4=matriz[1][1]
soma=n1+n2+n3+n4
print(f"A soma dos números é:{soma} ")