

# range(n) = [0, n-1]
# range(i,n) = [i, n-1]
# range(i,n,inc) [i, n-1] i = i + inc

def imprime(_array):
        print("\n\n\n",_array,"\n\n\n")


def troca(_array, posicaoA, posicaoB):
    aux = _array[posicaoA]
    _array[posicaoA] = _array[posicaoB]
    _array[posicaoB] = aux


def BublleSort(_array):
    _size = len(_array)
    cont = 0
    for i in range(_size):
        
        for j in range(1,_size):
            cont +=1
            if(_array[j-1] > _array[j]):
                troca(_array,j-1,j)
    print(cont)

def BublleSortMelhorado(_array):
    _size = len(_array)
    cont = 0
    ordenado = True
    for i in range(_size):
        if(ordenado == True):
            ordenado = False
            for j in range(1,_size):
                cont +=1
                if(_array[j-1] > _array[j]):
                    ordenado = True
                    troca(_array,j-1,j)
                    
    print(cont)

def InsertionSort(_array):

    _size = len(_array)
    cont = 0
    for i in range(1,_size):
        escolhido = _array[i]

        j = i-1

        while((j >= 0) and (_array[j] > escolhido)):
            troca(_array,j+1,j)
            cont +=1
            j -= 1
        _array[j+1] = escolhido
    
    print(cont)




def SelectionSort(_array):
    