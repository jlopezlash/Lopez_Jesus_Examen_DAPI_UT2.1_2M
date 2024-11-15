NombreC = input('Dime tu nómbre en formato Nombre Apellido ')
Nombre = NombreC.split()
print(Nombre[0])
Palabra = input('Dime una palabra ')
Vocal = input('Dime una vocal de la palabra ')
for letra in Palabra:
    if letra == Vocal:
        letra = letra.upper()
print(Palabra)