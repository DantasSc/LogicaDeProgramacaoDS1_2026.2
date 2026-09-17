# TODO: Implemente o menu utilizando match-case ou elif
opcao = int(input("Digite a opção desejada (1, 2 ou 3): "))

# Desenvolva a estrutura de seleção aqui
if opcao==1 :
    print("Consultar Livros")
elif opcao==2:
    print("Realizar Emprestimo")
elif opcao==3:
    print("Devolver Livro")
else:print("Opção não encontrada")