def busca_sequencial(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return False


def busca_binaria(lista, elemento):
    fist = 0
    last = len(lista)-1

    while fist <= last:
        middle = (fist + last) // 2

        if lista[middle] == elemento:
            return middle
        else:
            if elemento > middle:
                fist = middle + 1
            else:
                last = middle - 1
    return False


def busca_binaria_recursiva(lista, elemento, min=0, max=None):
    if max == None:
        max = len(lista)-1

    if max < min:
        return False
    else:
        meio = min + (max-min) // 2

    if lista[meio] > elemento:
        return busca_binaria(lista, elemento, min, meio-1)
    
    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, meio+1, max)

    else:
        return meio
