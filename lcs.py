def LCS(X, Y, pX, pY):
    L = [[0 for x in range(pY+1)] for x in range(pX+1)]
    LarF = [[0 for x in range(pY+1)] for x in range(pX+1)]
    Lar = [[0 for x in range(pY+1)] for x in range(pX+1)]

    for i in range(1, pX+1):
        for j in range(1, pY+1):
            if X[i-1] == Y[j-1]:
                L[i][j]= L[i-1][j-1]+1
                LarF[i][j] = '┐'
            else :
                L[i][j] = max(L[i-1][j], L[i][j-1])
                if L[i-1][j] >= L[i][j-1]:
                    LarF[i][j] = '|'
                else :
                    LarF[i][j] = '-'
    
    lcs = ""
    while i > 0 and j > 0:
        if L[i][j] == max(L[i-1][j], L[i][j-1]):
            if L[i-1][j] >= L[i][j-1]:
                Lar[i][j] = '|'
                i -= 1
            else :
                Lar[i][j] = '-'
                j -= 1
        else :
            Lar[i][j] = '┐'
            lcs = X[i-1] + lcs
            i -= 1
            j -= 1

    return [lcs, L, Lar, LarF]

if __name__ == "__main__" :
    X = str("ABCBDAB")
    Y = str("BDCABA")
    pX = len(X)
    pY = len(Y)
    lcs, l, lar, larf = LCS(X, Y, pX, pY)

    print(f'LCS : {lcs}')
    print('Matriks C : ')
    for i in range(0, len(l)):
        print(l[i])
    print('Matriks B : ')
    for i in range(0, len(larf)):
        print(larf[i])
    print('Matriks LCS : ')
    for i in range(0, len(lar)):
        print(lar[i])
