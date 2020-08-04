#calcular la suma de los números pares de fibbonacci menores a 4000000
numero_f = []
f0 = 1
f1 = 1
suma=0
par=0
for x in range (1,100):
    f0 = f0+f1
    f1 = f0-f1
    par = f1 % 2
    if f1 > 4000000:
        break
    if par == 0:
       suma = suma + f1
       numero_f.append(f1)
print(numero_f)
print(suma)