valorRefeicao = 42.54
taxaServico = 10

def custoTotal():
    custo = valorRefeicao + (valorRefeicao * taxaServico / 100)
    print("Custo total: R$", custo)

custoTotal()