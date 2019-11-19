import numpy as np
def diagonal(A):            #el parámetro es una lista
    DIAGX=[0,0]
    DIAGY=[0,0]
    for a in range(4):
        if A[a,a]=='X':
            DIAGX[0]+=1
        if A[a,a]=='O':
            DIAGY[0]+=1
        if A[a,a]=='T':
            DIAGX[0]+=1
            DIAGY[0]+=1
    for b in range(4):
        if A[3-b,b]=='X':
            DIAGX[1]+=1
        if A[3-b,b]=='O':
            DIAGY[1]+=1
        if A[3-b,b]=='T':
            DIAGX[1]+=1
            DIAGY[1]+=1
    return DIAGX, DIAGY
def filas(B):
    filX=[0,0,0,0]
    filO=[0,0,0,0]
    for a in range(4):
        filX[a]=np.count_nonzero(B[:,a]=='X')+np.count_nonzero(B[:,a]=='T')
        filO[a]=np.count_nonzero(B[:,a]=='O')+np.count_nonzero(B[:,a]=='T')
    return filX, filO
def columnas(B):
    colX=[0,0,0,0]
    colO=[0,0,0,0]
    for a in range(4):
        colX[a]=np.count_nonzero(B[a,:]=='X')+np.count_nonzero(B[a,:]=='T')
        colO[a]=np.count_nonzero(B[a,:]=='O')+np.count_nonzero(B[a,:]=='T')
    return colX, colO
def puntos(B):
    a = np.count_nonzero( B =='.')
    return a
A=[]
T=int(input())
for a in range(0,T):
    for b in range(4):
        A.append(list(input()))
    B=np.array(A)
    C=columnas(B)
    D=filas(B)
    E=puntos(B)
    print(C,D,E)