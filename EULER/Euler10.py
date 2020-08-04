#The sum of the primes below 10 is 2+3+5+7=17
#Find the sum of all the primes below two  millions

import time
import math

lista_primos=[2]
def is_prime1(n):
    booleano = True
    for x in range (2,n):
        if n % x ==0:
            booleano = False
            break
    return booleano

def is_prime2(n):
    booleano = True
    for x in range (2, math.floor( math.sqrt(n))+1):
        if n % x == 0:
            booleano = False
            break
    return booleano

def is_prime3( n, lista_primos):
    booleano = True
    for x in range (3,n):
        for i in range(0, len(lista_primos)):
            if( lista_primos[i] >  math.sqrt(x) ):
                lista_primos.append(x)
                break
            elif x % lista_primos[i] == 0:
                break
    return lista_primos

def problema10(n=200000):
    for x in range(3,n):
        if is_prime2(x):
            lista_primos.append(x)

    print( sum(lista_primos))

start = time.time()             #para ver el tiempo de ejecución de la función
problema10(n=20000000)
end = time.time()
print('tiempo de ejecución', end - start, 'segundos')

start = time.time()             #para ver el tiempo de ejecución de la función
print(sum(is_prime3(20000000, [2])) )
end = time.time()
print('tiempo de ejecución', end - start, 'segundos')