valor_conta = float(input("Qual o valor da conta?"))
pessoas = int(input("quantas pessoas vão dividir a conta?"))
valor_por_pessoa = valor_conta/pessoas
print(f"O valor por pessoa será de:R${valor_por_pessoa:.2f}")