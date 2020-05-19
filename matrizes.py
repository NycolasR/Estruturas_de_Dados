def cria(num_linhas, num_colunas, valor = 0):
    '''
    (int, int, valor) -> matriz
    Cria e retorna ums matriz com num_linhas linhas e num_colunas
    colunas em que cada elemento é passado por parâmetro de
    entrada.
    '''

    matriz = []

    for i in range(num_linhas):
        # cria a linha i
        linha = []
        
        for j in range(num_colunas):
            linha.append(valor)

        # adiciona linha à matriz
        matriz.append(linha)
        
    return matriz


def multiplica(a, b):
    '''
    (matriz, matriz) -> matriz
    Recebe duas matrizes por parâmetro de entrada
    e retorna a matriz resultante da multiplicação
    da primeira pela segunda.
    '''
    
    assert sao_multiplicaveis(a, b)

    c = []
    
    for linha in range(len(a)):
        # começando uma noval linha
        c.append([])
        for coluna in range(len(b[0])):
            # adicionando uma nova coluna
            c[linha].append(0)
            for k in range(len(a[0])):
                c[linha][coluna] += a[linha][k] * b[k][coluna]

    return c


def le_matriz():
    '''
    () -> matriz
    Lê a quantidade de linhas e colunas para formar
    e retornar a matriz desejada.
    '''
    
    tot_linhas = int(input("Digite o número de linhas da matriz: "))
    tot_colunas = int(input("Digite o número de colunas da matriz: "))
    matriz = cria_matriz(tot_linhas, tot_colunas)
    return formata_matriz(matriz)



def dimensoes(matriz):
    '''
    (matriz) -> str
    Retorna uma string formatada com as dimensões
    da matriz.
    '''
    
    return "{} X {}".format(len(matriz), len(matriz[0]))


def contar_linhas_nulas(matriz):
    '''
    (matriz) -> int
    Retorna a quantidade de linhas nulas da matriz.
    '''
    
    tot_linhas = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            is_nula = True
            if matriz[i][j] != 0:
                is_nula = False
                break
        if is_nula:
            tot_linhas += 1

    return tot_linhas


def contar_colunas_nulas(matriz):
    '''
    (matriz) -> int
    Retorna a quantidade de linhas colunas da matriz.
    '''
    
    tot_colunas = 0
    
    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            is_nula = True
            if matriz[i][j] != 0:
                is_nula = False
                break
        if is_nula:
            tot_colunas += 1

    return tot_colunas


def sao_multiplicaveis(m1, m2):
    '''
    (matriz, matriz) -> bool
    Retorna valor lógico True caso a primeira
    matriz possa multiplicar a segunda e
    retorna False, caso contrário.
    '''
    
    return len(m1[0]) == len(m2)


def is_simetrica(matriz):
    '''
    (matriz) -> bool
    Retorna valor lógico True caso a matriz
    seja simétrica e retorna False,
    caso contrário.
    '''
    
    flag = True
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] != matriz[j][i]:
                flag = False

    return flag


def formata(matriz):
    '''
    (matriz) -> str
    Retorna uma string formatada
    que apresenta a matriz passada por
    parâmetro de entrada.
    '''
    
    tot_linhas = len(matriz)
    tot_colunas = len(matriz[0])
    matriz_formatada = ""
    
    for i in range(tot_linhas):
        for j in range(tot_colunas):
            if j == tot_colunas - 1:
                matriz_formatada += f"[ {matriz[i][j]} ]\n"
            else:
                matriz_formatada += (f"[ {matriz[i][j]} ]")

    return matriz_formatada

                
def tem_mesmas_dimensoes(m1, m2):
    '''
    (matriz, matriz) -> bool
    Retorna valor lógico True caso as matrizes
    possuam as mesmas dimensões e retorna False,
    caso contrário.
    '''
    
    return len(m1) == len(m2) and len(m1[0]) == len(m2[0])



def soma(m1, m2):
    '''
    (matriz, matriz) -> matriz
    Retorna a soma das matrizes passadas por
    parâmetro de entrada.
    '''
    
    assert tem_mesmas_dimensoes(m1, m2)

    matriz_resultante = []

    for i in range(len(m1)):
        linha = []
        for j in range(len(m1[0])):
            linha.append(m1[i][j] + m2[i][j])
        matriz_resultante.append(linha)

    return matriz_resultante


def subtrai(m1, m2):
    '''
    (matriz, matriz) -> matriz
    Retorna a subtração da primeira matriz
    pela segunda.
    '''
    
    assert tem_mesmas_dimensoes(m1, m2)

    matriz_resultante = []

    for i in range(len(m1)):
        linha = []
        for j in range(len(m1[0])):
            linha.append(m1[i][j] - m2[i][j])
        matriz_resultante.append(linha)

    return matriz_resultante

