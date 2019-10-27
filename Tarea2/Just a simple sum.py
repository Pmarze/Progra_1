#solo falta optimizar, tiempo límite 17s el proceso se tarda 22s
def mcd(a, b):
    if (a == 0):
        return b
    return mcd(b%a,a)

def Fi(N):
    prim_rel=1
    for a in range(2,N):
        R=mcd(a,N)
        if R==1:
            prim_rel+=1
    return prim_rel

T=int(input()) #casos a analizar
for a in range(0,T):
    N,M = map(int,input().strip('\n').split(' '))   # "N" es el número, "M" es el módulo
    while
    A,B=0,0
    F=Fi(M)
    for b in range(1,N+1):
        X = b % M
        Y = b % F
        Z = X ** Y
        A=A+Z
        B=A-Z
    print(A%M)