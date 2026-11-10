# Crie um dicionário representando um veículo com as chaves `"marca"`, `"modelo"` e `"ano"`.
# Imprima cada chave e seu respectivo valor usando o método `.items()` em um laço `for`.
# TODO: Crie o dicionário do veículo e percorra com for
veiculo = {
    "marca":"Ferrari",
    "modelo":"458 italia",
    "ano":"2026"
}

# Escreva o laço for com .items()
for chaves, itens in veiculo.items():
    print(chaves,":",itens)