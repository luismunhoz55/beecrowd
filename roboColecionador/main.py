estrelas = 0

def moverRobo(posicao, direcao, array):
        global estrelas

    # ver a posicao do robô
        DI = posicao[0]
        DJ = posicao[1]

    # ver para onde ele quer ir 
        if direcao == "N":
            DI -= 1
        elif direcao == "L":
            DJ += 1
        elif direcao == "S":
            DI += 1
        elif direcao == "O":
            DJ -= 1

    # verificar se é possivel
        if DI <= len(array) - 1 and DJ <= len(array[0]) - 1 and DI >= 0 and DJ >= 0 and array[DI][DJ] != '#':
            
        # mover 
            if array[DI][DJ] == '*':
                estrelas += 1
            array[DI][DJ] = direcao
            array[posicao[0]][posicao[1]] = '.'
            return [DI, DJ]
        
        # se não for possivel mover, retornar a mesma posição
        return [posicao[0], posicao[1]]
            
    
def mudarDirecao(posicao, direcaoDesejada, array):
    direcao = array[posicao[0]][posicao[1]]

    # esquerda
    if direcao == 'N' and direcaoDesejada == 'E':
        array[posicao[0]][posicao[1]] = 'O'
    elif direcao == 'O' and direcaoDesejada == 'E':
        array[posicao[0]][posicao[1]] = 'S'
    elif direcao == 'S' and direcaoDesejada == 'E':
        array[posicao[0]][posicao[1]] = 'L'
    elif direcao == 'L' and direcaoDesejada == 'E':
        array[posicao[0]][posicao[1]] = 'N'

    # direita
    if direcao == 'N' and direcaoDesejada == 'D':
        array[posicao[0]][posicao[1]] = 'L'
    elif direcao == 'L' and direcaoDesejada == 'D':
        array[posicao[0]][posicao[1]] = 'S'
    elif direcao == 'S' and direcaoDesejada == 'D':
        array[posicao[0]][posicao[1]] = 'O'
    elif direcao == 'O' and direcaoDesejada == 'D':
        array[posicao[0]][posicao[1]] = 'N'

    return array[posicao[0]][posicao[1]]
while True:
    try:
        estrelas = 0
        entradas = input().split(" ")
        
        n = int(entradas[0])
        m = int(entradas[1])
        s = int(entradas[2])
        
        if n == 0 and m == 0 and s == 0:
            break
        
        mapa = []
        
        # criar a matriz do mapa
        for i in range(n):
            linha = list(input())
            mapa.append(linha)
            
        instrucoes = list(input())

        posicao = []

        found = False
        direcao = None

        # encontrar onde o robô está e qual a direção que ele está apontando
        for y in range(n):
            for x in range(m):
                if mapa[y][x] != '.' and mapa[y][x] != '#' and mapa[y][x] != '*':
                    posicao.append(y)
                    posicao.append(x)
                    direcao = mapa[y][x]
                    found = True  
                    break  
            if found:
                break  # Sai do loop externo

        # mover o robo de acordo com as instruções
        for instrucao in instrucoes:
            if instrucao == 'F':
                posicao = moverRobo(posicao, direcao, mapa)
            else:
                direcao = mudarDirecao(posicao, instrucao, mapa)

        print(estrelas)

    except EOFError:
        break
