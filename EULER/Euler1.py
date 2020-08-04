#calcular la suma de multiplos de 3 o 5 antes de 1000
numeros_multiplos =[]
for x in range(0,1000):
    if x % 3 == 0:
        numeros_multiplos.append(x)
    elif x % 5 ==0:
        numeros_multiplos.append(x)
print(numeros_multiplos)
suma = 0
for y in numeros_multiplos:
    suma = suma + y
print(suma)