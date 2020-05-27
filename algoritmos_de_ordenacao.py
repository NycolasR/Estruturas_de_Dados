def selection_sort(lista):
    for i in range(len(lista)-1):
        n = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[n]:
                n = j
        lista[i], lista[n] = lista[n], lista[i]
        
    return lista


def insertion_sort(lista):
    # considera-se que o 1º elemento já está ordenado
    for i in range(1, len(lista)):
        # se obtém um elemento dos desordenados
        elemento = lista[i]
        j = i

        # j deve ser maior que 0
        # "enquanto houver elementos maiores que elemento
        # na lista dos ordenados..."
        while j > 0 and lista[j-1] > elemento:
            # desloca-se o último elemento dos ordenados
            # para a direita em uma casa
            lista[j] = lista[j-1]
            j -= 1

        # o espaço [j] ficou vazio graças
        # aos deslocamentos realizados dentro do while
        lista[j] = elemento

    return lista


def bubble_sort(lista):
    has_changed = True
    
    while has_changed: # se noo houve alteracao, a lista está ordenada
        has_changed = False

        for i in range(1, len(lista)):
            # a cada 2 elementos, verifica-se se o elemento
            # mais para a esquerda é maior que o seu antecesso
            if lista[i] < lista[i-1]:
                # realiza a troca dos 2 elementos na lista
                lista[i], lista[i-1] = lista[i-1], lista[i]

                # para que a próxima iteração ocorra
                has_changed = True

    return lista


def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    
    lado_esquerdo = merge_sort(lista[:meio])
    lado_direito = merge_sort(lista[meio:])

    return merge(lado_esquerdo, lado_direito)

def merge(lado_esquerdo, lado_direito):
    if not lado_esquerdo:
        return lado_direito
    if not lado_direito:
        return lado_esquerdo

    if lado_esquerdo[0] < lado_direito[0]:
        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)
    
    elif lado_esquerdo[0] >= lado_direito[0]:
        return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])
