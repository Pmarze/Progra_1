import random
caballos=[]
distancias=[]
lista=[]

def mergesort(lista):
    if len(lista)>1:
        mitad=int(len(lista)/2)
        izquierda=lista[:mitad]
        derecha =lista[mitad:]

        mergesort(izquierda)
        mergesort(derecha)

        i,j,k=0,0,0
        while i<len(izquierda) and j<len(derecha):
            if izquierda[i]<derecha[j]:
                lista[k]=izquierda[i]
                i+=1
            else:
                lista[k]=derecha[j]
                j+=1
            k+=1

        while i<len(izquierda):
            lista[k]=izquierda[i]
            i+=1
            k+=1
        while j<len(derecha):
            lista[k]=derecha[j]
            j+=1
            k+=1

print()
T=int(input('Ingrese el número de casos a analizar, T='))
if T<=0:
    print('Número no válido,0<T<11')
if T>10:
    print('Número no válido,0<T<11')

if 0<T<11:
    N = int(input('Ingrese el número de caballos que quiere analizar, N='))
    print()
    if 0>N>5000:
        print('Número no válido')
        N=0
    else:
        for a in range(0,T):
            for x in range(1,N+1):
                caballos.append(random.randint(1,1000000001))
            print('Caballos analizados',caballos)
            for y in range(0,N+1):
                Z=y+1
                for z in range(Z,N):
                    distancias.append(abs(caballos[y]-caballos[z]))
                    Z+=1
            print(distancias)

            mergesort(distancias)
            print(distancias)
            print('La mínima diferencia posible es:',distancias[0])
            print()
            caballos.clear()
            distancias.clear()