# TODO: Defina a função calcular_media e teste-a abaixo
def calcular_media(nota1, nota2, nota3):
    media=(nota1+nota2+nota3)/3
    return media
# Escreva o corpo da função pass
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
# Teste com notas de exemplo
media=calcular_media(nota1,nota2,nota3)
print(f"Sua média é:{media:.2f}")