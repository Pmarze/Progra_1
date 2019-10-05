print('Restricciones:')
print('1 <= B < A <= 10000 ')
print()
A = int(input('Ingrese el número A='))
B = int(input('Ingrese el número B='))
C = 0
if A>10000:
    C+=1

if B > 10000:
    C+=1

if A<B:
    C += 1

if C>0:
    print('operación no permitida')
    C=0

else:
    X=str(A-B)
    Y=int(len(X))
    Z=X[0:Y-1]+'8'
    print(Z)



