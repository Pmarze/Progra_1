import numpy as np
def Cm(A):
    r = A.min(axis=1)  # mínimo de cada filas
    R = max(r)  # máximo de r
    return R
def RM(A):
    c = A.max(axis=0)  # máximo de cada columna
    C = min(c)  # mínimo de c
    return C
def ceros(A,B,N):
    for b in range(N):
        for c in range(N):
            if A[b][c]==B[b][c]:
                A[b][c]=0
    return A
def cerof(H,D,F,G,N):
    for a in range(N):
        for b in range(N):
            H[a][b]=H[a][b]*F[a][b]
            H[a][b] = H[a][b]*G[a][b]
    for c in range(N):
        for d in range (N):
            if H[c][d]!=0:
                H[c][d]=D[c][d]
    return H
N=input() #NxN
N=int(N)
E=[]
respuesta=0
for a in range(N):                          #para crear la matriz de NXN
    B=input().strip('\n').split(' ')
    B=list(map(int,B))
    E.append(B)                             #Crea una lista de listas
D=np.array(E)                               #Convierte la lista en matriz
R=RM(D)                                     #máximo de los mínimos de cada columna
C=Cm(D)                                     #mínimo de los máximos de cada columna
if R-C==0:
    print(respuesta)
elif R-C!=0:
    X=np.sort(D, axis=0) #matriz con columnas ordenadas
    Y=np.sort(D, axis=1) #matriz con filas ordenadas
    F=ceros(X,D,N) #volver cero los valores que no cambian al reordenarse
    G=ceros(Y,D,N)
    H=np.copy(D)                 #copia de D para manipular
    I=cerof(H,D,F,G,N)
    for b in range(N):
        for c in range(N):
            print('prueba')