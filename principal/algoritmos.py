

# range(n) = [0, n-1]
# range(i,n) = [i, n-1]
# range(i,n,inc) [i, n-1] i = i + inc

def imprime(_array):
    for i in range(len(_array)):
        print(_array[i])


def troca(_array, posicaoA, posicaoB):
    aux = _array[posicaoA]
    _array[posicaoA] = _array[posicaoB]
    _array[posicaoB] = aux


def BublleSort(_array):
    _size = len(_array)

    for i in range(_size):
        
        for j in range(i+1,_size):

            if(_array[i] > _array[j]):    
              troca(_array,i,j)
    imprime(_array)