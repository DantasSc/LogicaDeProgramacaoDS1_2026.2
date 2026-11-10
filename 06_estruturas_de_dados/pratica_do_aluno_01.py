# TODO: Implemente o carrinho de compras
carrinho_compras = []

# Adicione 3 produtos e ordene a lista
for i in range(3):
    produto=input("Digite o produto que será adicionado ao carrinho: ")
    carrinho_compras.append(produto)
carrinho_compras.sort()
print(f"Seu carrinho contém:{carrinho_compras}")