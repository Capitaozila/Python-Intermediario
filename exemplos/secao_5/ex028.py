class Caneta:

    def __init__(self, cor):
        self.cor_tinta = cor

    # def get_cor(self):
    #     print(f'GET COR {self.cor_tinta}')
    #     return self.cor_tinta

    @property
    def cor(self):
        print('property'.upper())
        return self.cor_tinta


caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
print(caneta.cor)
