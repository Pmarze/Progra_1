import math
import time
def palindromo(c):           #el parámetro es un número
    P = [int(d) for d in str(c)]
    P.reverse()
    P=[str(i) for i in P]
    a=int(''.join(P))
    return abs(a-c)

C=[]
T=int(input())
for a in range(0,T):
    A, B = map(int, input().strip('\n').split(' ')) #A-inicio      B-final
    start = time.time()
    for b in range(0,int(math.sqrt(B))+1):          #desde cero hasta raíz de B, porque no hay cuadrados más grandes
        c=b**2
        if (c)>=A:                                  #descartar los cuadrados menores al rango
            if palindromo(c)==0:
                C.append(c)
    end = time.time()
    print(C)
    print(end-start, 'segundos')

    C=[]
