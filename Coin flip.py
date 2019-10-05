T=int(input('Ingrese el número de casos a analizar, T='))
monedas=[]

def invertir(lista):
    if G>1:
        for a in range(0,G):
            for b in range(0,a+1):
                lista=monedas
                if lista[b]==1:
                    lista[b]=0
                    b += 1
                else:
                    lista[b]=1
                    b += 1
                a+=1
            print(lista)

def contar(lista):
    B=0
    C=0
    A=int(len(lista))
    for a in range(0,A):
        if lista[a]==1:
            B+=1
            a+=1
        else:
            C+=1
            a+=1
    if Q==1:
        print('número de caras =',B)
    else:
        print('número de escudos =',C)

for a in range(0,T):
    G = int(input('Ingrese el número de juegos, G='))
    print('1, posición inicial cara... 2, posición inicial escudo')
    I = int(input('I='))
    N = int(input('Ingrese el número de monedas, N='))
    print('1, contar el número de caras al final... 2, contar el número de escudos al final')
    Q = int(input('Q='))
    print()
    for b in range(0,N):
        if I==1:
            monedas.append(1)
        if I==2:
            monedas.append(0)

    invertir(monedas)
    contar(monedas)
    monedas.clear()
    print()