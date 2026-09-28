# TODO: Implemente o menu utilizando match-case ou elif
opcao = int(input("Digite a opção desejada (1, 2 ou 3): "))
# Desenvolva a estrutura de seleção aqui
match opcao :
    case 1:
        print("Consultar Livros")
    case 2:
        print("Realizar Emprestimo")
    case 3:
        print("Devolver Livro")
    case _:
        print("Opção não encontrada")