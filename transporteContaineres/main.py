while True:
    try:
        entradas = input().split(" ")
        A = int(entradas[0])
        B = int(entradas[1])
        C = int(entradas[2])

        entradas1 = input().split(" ")
        X = int(entradas1[0])
        Y = int(entradas1[1])
        Z = int(entradas1[2])

        largura = X // A
        comprimento = Y // B
        altura = Z // C

        print(largura * altura * comprimento)

    except EOFError:
        break