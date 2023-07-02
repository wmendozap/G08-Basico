class A:
    def __int__(self):
        self.inicial = 30
        self._contador = 0

    def incrementa(self):
        self._contador = self._contador + 1

    def cuenta(self):
        return self._contador

class B:
    def __int__(self):
        self.inicial = True
        self.__contador = 0

    def incrementa(self):
        self.__contador = self.__contador + 1

    def cuenta(self):
        return self.__contador

var_1 = A()
var_1.inicial = 30
var_1._contador = 0
var_1.incrementa()
var_1.incrementa()
var_1.incrementa()
print(var_1.cuenta())
