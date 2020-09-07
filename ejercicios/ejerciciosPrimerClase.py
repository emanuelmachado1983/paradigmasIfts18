#Ejercicio 1
#
# Crear un programa que imprima por pantalla el mensaje “Hello World!”.
#
# Nota: se puede imprimir el dato puro o el dato almacenado en una variable, siempre es una buena práctica usar variables.
def exercise1():
    print("Hello World!")

#exercise1()

# Ejercicio 2
#
# Crear un programa que imprima por pantalla todos los números pares del 0 al 100.

def exercise2():
    i= 0
    while i <= 100:
        print(i)
        i = i + 1

#exercise2()

# Ejercicio 3
#
# Crear un programa que imprima por pantalla todos los números del 0 al 100 que sean divisibles por 3.

def exercise3():
    i= 0
    while i <= 100:
        if i % 3 == 0:
            print(i)
        i = i + 1

#exercise3()

# Ejercicio 4
# Crear un programa que pida al usuario que ingrese dos números y luego el programa imprima por pantalla: en un renglón la suma de ellos, en otro la resta y en otro el producto.

def exercise4():
    i= 0
    numero1 = int(input("ingrese un número"))
    numero2 = int(input("ingrese otro número"))

    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    print (suma)
    print (resta)
    print (multiplicacion)
    

#exercise4()

# Ejercicio 5
#
# Crear un programa que pida al usuario 10 números enteros, los almacene en una lista, ordene los números dentro de la lista y luego imprima por pantalla la lista completa y ordenada.​


def exercise5():
    userList = []
    for i in range(10):
        userList.append(int(input("ingrese un número")))
    userList.sort()
    print(userList)
#exercise5()

# ​
# Ejercicio 6
#
# Crear un programa que le pida al usuario dos números enteros y luego: si el primero es mayor que el segundo, retorne 1, si el primero es menor que el segundo retorne -1 y si ambos números son iguales retorne 0.

def exercise6():
    numero1 = int(input("ingrese un número"))
    numero2 = int(input("ingrese otro número"))

    if numero1 > numero2:
        return 1
    if numero2 > numero1:
        return -1
    if numero2 == numero1:
        return 0

#print(exercise6())

# Ejercicio 7
#
# Crear un programa que le pida al usuario ingresar dos números enteros y devuelva el punto medio entre ellos.

def exercise7():
    numero1 = int(input("ingrese un número"))
    numero2 = int(input("ingrese otro número"))

    return (numero1 + numero2) / 2

#print(exercise7())

#
# Ejercicio 8
#
# Crear un programa que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.
#

def exercise8():
    seguirIngresando = ""
    listaPares = []
    listaImpares = []
    while seguirIngresando != "N":
        numero = int(input("ingrese un número"))
        if numero % 2 == 0:
            listaPares.append(numero)
        else:
            listaImpares.append(numero)
        seguirIngresando = input("Ingrese el caracter 'N' si quiere dejar de ingresar números")

    listaPares.sort()
    listaImpares.sort()
    print(listaPares)
    print(listaImpares)

# print(exercise8())

# Ejercicio 9
#
# Crear un programa que solicite al usuario que ingrese su dirección mail. Imprimir un mensaje indicando si la dirección es válida o no. Una dirección se considerará válida si contiene el símbolo "@".
# 

def exercise9():
    mail = input("Ingrese dirección de email")
    if mail.find("@")>1:
        print("Dirección válida")
    else:
        print("Dirección inválida")
# exercise9()

# Ejercicio 10
#
# Crear un programa que dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

def exercise10():
    dni = int(input("Ingrese DNI: "))
    dniString = str(dni)
    if (len(dniString) == 7 or len(dniString) == 8):
        return True
    else:
        return False

#print(exercise10())

# Ejercicio 11
#
# Crear un programa que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro.​
def exercise11():
    word = input("Ingrese palabras: ")
    word = word.strip()
    vectorWord = word.split()
    if len(vectorWord) == 0:
        return 0
    return vectorWord[-1]

#print(exercise11())

# Ejercicio 12
#
# En McDonald’s se pueden comprar patitas de pollo en 6, 9 o 20 unidades. Crear un programa que, a partir de un número, decida si es posible comprar esa cantidad de patitas.
#
#

def exercise12():
    units = int(input("Ingrese cantidad de unidades: "))
    if (units==6 or units == 9 or units == 20):
        return True
    return False

#print(exercise12())