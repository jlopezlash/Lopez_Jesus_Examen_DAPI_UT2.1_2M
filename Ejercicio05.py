def area_cuadrado(lado):
    '''La funcion calculara el área de una cuadrado
    Parametros
        Entrada :Lado
        Salida  :Area
    '''
    Area = lado * lado
    print(Area)
    return Area
area_cuadrado(8)

def mayor_de_tres(a, b, c):
    '''La funcion mostrara el numero mayor
    Parametros
        Entrada :3 numeros dados por el usuario
        Salida  :El mayor de los 3
    '''
    x = a, b, c
    x = list(x)
    y = max(x)
    print(y)
    return
mayor_de_tres(input('Dime un número '),input('Dime un número '),
              input('Dime un número '))
    