# TODO: Implemente a expressão de validação
media_aluno = float(input("Qual a sua média? "))
frequencia_percentual =float(input("Qual a sua porcentgem de frequencia? "))

# Crie a variável aprovado com a expressão lógica
aprovado = media_aluno>=6 and frequencia_percentual>=75
print(f"Status de aprovação:{aprovado}")