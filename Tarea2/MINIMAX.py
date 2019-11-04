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

N=input() #NxN
N=int(N)
E=[]
respuesta=0
for a in range(N):                          #para crear la matriz de NXN
    B=input().strip('\n').split(' ')
    B=list(map(int,B))
    E.append(B)                             #Crea una lista de listas
D=np.array(E)                               #Convierte la lista en matriz
R=RM(D)
C=Cm(D)
if R-C==0:
    print(R-C)

elif R-C!=0:
    X=np.sort(D, axis=0) #matriz con columnas ordenadas
    #Y=np.sort(D, axis=1) #matriz con filas ordenadas
    print(ceros(X,D,N)) #volver cero los valores que no cambian al reordenarse

    if