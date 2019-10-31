def vecindad(A,par,n):
    if A[n+par-1]==10:
        A[n+par-1]=0
        A[n+par-2]=int(A[n+par-2])+1
        vecindad(A,par,n-1)
    return A

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
        D=C[0:(B//2)]
        D.reverse()
        F=''.join(D)

        if par==1:
            E=C[(B//2)+1:B]
            G=''.join(E)
            if F>G:
                for b in range(0,(B//2)):
                    C[(B-b-1)]=C[b]
                print(''.join(C))
            elif F<=G:
                C[B//2]=int(C[B//2])+1
                vecindad(C,par,(B//2))
                C=[str(i) for i in C]
                for c in range(0,(B//2)):
                    C[(B-c-1)]=C[c]
                print(''.join(C))
        if par==0:
            E=C[(B//2):B]
            G=''.join(E)
            if F>G:
                for d in range(0,(B//2)):
                    C[(B-d-1)]=C[d]
                print(''.join(C))
            elif F<=G:
                C[(B//2)-1]=int(C[(B//2)-1])+1
                vecindad(C, par, (B // 2))
                C = [str(i) for i in C]
                for e in range(0, (B // 2)):
                    C[(B-e-1)]=C[e]
                print(''.join(C))