x = 2
y = 0
n=600851475143

while(n!=1):
    if(n % x == 0):
        y = x
        n = n/x
        print(x)
    else:
       x=x+1
print("primo drivisor más grande")
print(y)

