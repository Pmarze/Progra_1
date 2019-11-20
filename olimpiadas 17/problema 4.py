def suma(C,N):
    A=0
    for a in range(N):
        A=C[a]+A
        if A>K:
            A=A-C[a]
            break
    return A,a
def corrimiento(C,n):
    D=C.copy()
    for a in range(len(C)):
        D[a-n]=C[a]  # n es el corrimiento de espacios
    return D
A=0
C=[]
F=0
T=int(input())
for a in range(T):
    R,K,N=map(int, input().strip('\n').split(' '))  #K= capacidad del vagón, R veces repite
    C=input().strip('\n').split(' ')
    C=[int(i) for i in C]
    #print(C)
    D=C.copy()
    for b in range(R):
        E=suma(D,N)
        F=F+E[0]
        D=corrimiento(D,E[1])
    print(F)
    F=0
    E,D=[],[]