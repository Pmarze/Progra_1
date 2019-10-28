def entero(C):
    X=0
    for x in range(0,len(C)):
        Y=int(C[a]*(10**(len(C)-a-1)))
        X=X+Y
    return X

T=input() #casos a analizar
T=int(T)
for a in range(0,T):
    N = input()  # número N
    A=list(N)
    B=len(A)
    if A.count('9')==B:
        print('1'+ '0' * (B-1) + '1')
    else:
        par = B%2
        C=A.copy()
        if par==0:
            if C[(B//2)-1]>= C[B//2]:
                for b in range(0,(B//2)):
                    C[(B-b-1)]=C[b]
                print(C)
            else:
                C[(B//2)-1]= int(C[(B//2)-1])+1
                for c in range(0,(B//2)):
                   C[(B-c-1)]=C[c]
                print(C)
        if par==1:
            D=C[0:(B//2)]
            E=C[(B//2)+1:B]
            D.reverse()
            G,I=0,0
            for d in range(0,len(D)):
                F=int(D[d]*(10**(len(D)-d-1)))
                G=G+F
            for e in range(0,len(E)):
                H=int(E[e]*(10**(len(E)-e-1)))
                I=H+I
            if G>I:
                for f in range(0,(B//2)):
                    C[(B-f-1)]=C[f]
                print(C)
            elif G<=I:
                C[B//2]=int(C[B//2])+1
                for g in range(0,(B//2)):
                    C[(B-g-1)]=C[g]
                print(C)