import math
import time
def palindromo(c):           #el parámetro es un número
    P = [int(d) for d in str(c)]
    P.reverse()
    P=[str(i) for i in P]
    a=int(''.join(P))
    return abs(a-c)
T=int(input())
for a in range(0,T):
    A, B = map(int, input().strip('\n').split(' ')) #A-inicio      B-final
    #start = time.time()
    z=0
    for b in range(0,int(math.sqrt(B))+1):          #desde cero hasta raíz de B, porque no hay cuadrados más grandes
        if palindromo(b)==0:                        #Analizar si el número es un palíndromo
            c=b**2                                  # Si es palindromo elevar al cuadrado para ver si su cuadrado también es palindromo
            if (c)>=A:                              #descartar los cuadrados menores al rango
                if palindromo(c)==0:                #Analizar si el número es un palíndromo
                    z+=1
    #end = time.time()
    print(z)
    #print(end-start, 'segundos')