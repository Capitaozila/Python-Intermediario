# Realizar uma batalha entre dois personagens
def batalha(personagem1, personagem2):
    forca1 = calcular_forca(personagem1)
    forca2 = calcular_forca(personagem2)
    if forca1 > forca2:
        return personagem1
    else:
        return personagem2
