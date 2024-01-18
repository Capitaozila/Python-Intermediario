def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar =  criar_multiplicador(2)
triplicar =  criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)
quintuplicar = criar_multiplicador(5)

print(duplicar(7))
print(triplicar(7))
print(quadruplicar(7))
print(quintuplicar(7))