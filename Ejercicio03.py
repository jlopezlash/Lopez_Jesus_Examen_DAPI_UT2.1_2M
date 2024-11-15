N = int(input('Introduce un número entero positivo '))
if N %2 == 0:
    print(N,'es par')
else:
    print(N,'es impar')
X = int(input('Introduce un número entero '))
for i in range(X+1):
    if i %3 == 0:
        print(i)