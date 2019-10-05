import math
B=[]
T=int(input('Número de casos a analizar, T='))
def factorial(x,n):
    if n>0:
        x=factorial(1,n-1)
        x=x*n
    else:
        x=1
    return x

def descomponer(n,a,b):
    multiplos=[]
    for i in range(a,b+1):
        while n%i==0:
            multiplos.append(i)
            n=n/i
    return multiplos

def ceros(c,d):
    regreso=''
    if c>d:
        print('número de ceros=',d)
    else:
        print('número de ceros=',c)
    return regreso
for a in range(0,T):
    N=int(input('Ingrese un número N, N='))
    A=factorial(1,N)
    print(A)
    B=descomponer(A,2,5)

    c, d, e = 0, 0, 0
    for i in range (0,len(B)):

        if B[i]==2:
            c+=1
        if B[i]==5:
            d+=1
        else:
            e=0
    x=ceros(c,d)
    print(x)
    print()




