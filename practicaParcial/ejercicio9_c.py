import os.path
import csv

class Prestacion:
    pass

#ordenamiento de burbujeo que usa muy poca memoria, pero es lento.
def ordenarDatos(datos, campos):
    x=0
    while x < len(datos):
        y=0
        while y < len(datos):
            linea1=datos[x]
            linea2=datos[y]
            if linea1[campos[1]] < linea2[campos[1]]:                
                lineaAux = datos[y]
                datos[y] = datos[x]
                datos[x] = lineaAux
            y+=1
        x+=1
    return datos

def imprimirDatos(datos):
    for linea in datos:
        print (linea)

def eje9_listar(archivo):
    print("Ingrese dni del beneficiario sin puntos, por ejemplo (30495657):")
    dniIngresado = input("")
    try:
        with open(archivo,'r', newline='') as file:
            lectura_csv = csv.DictReader(file, delimiter=';')
            campos = lectura_csv.fieldnames
            sumaTotalTodosLosBeneficiarios = 0
            sumaTotalBeneficiarioSeleccionado = 0
            datos = []
            for linea in lectura_csv:
                dni = linea[campos[0]]
                prestacion = linea[campos[1]]
                saldo = float(linea[campos[2]].replace(",","."))
                sumaTotalTodosLosBeneficiarios += saldo
                if (dni == dniIngresado ):
                    sumaTotalBeneficiarioSeleccionado += saldo
                    datos.append(linea)
            
            imprimirDatos(datos)
            datos = ordenarDatos(datos, campos)
            print ("-----")
            imprimirDatos(datos)
            print ("-----")
            print("")
            print("Prestaciones:")
            x=0
            print(len(datos))
            while x < len(datos):
                linea=datos[x]
                prestacionAux = linea[campos[1]]
                sumaSaldoPrestacion = 0
                contador = 0
                while x < len(datos) and linea[campos[1]] == prestacionAux:
                    print (linea)
                    sumaSaldoPrestacion += float(linea[campos[2]].replace(",","."))
                    contador += 1
                    x += 1
                    if (x< len(datos)):
                        linea=datos[x]
                print(f"{prestacionAux}, cantidad de consultas: {contador}, saldo{sumaSaldoPrestacion}")
            print(f"Total gastado del beneficiario: {sumaTotalBeneficiarioSeleccionado}")
            print(f"Total gastado de todos los beneficiario: {sumaTotalTodosLosBeneficiarios}")
       
            return
    except IOError:
        print("Ocurrio un error con el archivo")

# 7 a
def ejercicio9():
    ARCHIVO = "pagos_prestaciones.csv"
    #CAMPOS = ['DNI', 'Prestación', 'Saldo']

    while True:
        print("Elija una opcion: \n 1.Buscar beneficiario \n 2.Salir")
        opcion = input("")

        if opcion == "2":
            exit()
        if opcion == "1":
            eje9_listar(ARCHIVO)
        else:
            print("Por favor elija una opcion valida")

ejercicio9()


#linea.rstrip("\n")