# Encapsulamento (modificadores de acesso: public, _protected, __private)
# Python não tem modificadores de acesso, mas tem convenções
# as seguintes convenções são:
#   (sem underline) = public. 
#       pode ser acessado de qualquer lugar

#   _ (um underline) = protected. 
#       não DEVE ser usado fora da classe ou suas subclasses

#   __ (dois underlines) = private. pode ser acessado apenas dentro da classe
#       "nome mangling" (desfiguração de nomes) em Python
#       só DEVE ser usado dentro da classe que foi declarado


class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__exemplo = 'isso é private'
        
    def metodo_publico(self):
        # self.metodo_protected()
        # print(self._protected)
        print(self.__exemplo)
        self.__metodo_private()
        return 'metodo público'
    
    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'
    
    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'
    
    
f = Foo()
print(f.metodo_publico())
print(f._Foo__metodo_private())