
def imprime(self, _array):
    for i in range(len(_array)):
        print(_array[i])


def troca(self, valorA, valorB):
    aux = valorA
    valorA = valorB
    valorB = aux


def bubllesort(self, _array):
    _size = len(_array)

    for i in range(_size):
        
        for j=1 in range(_size):

            if(_array[i] > _array[j]):
                
                troca(_array[i],_array[j])


