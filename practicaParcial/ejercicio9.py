import os.path
import csv

def eje9_listar(archivo):
    print("Ingrese dni del beneficiario sin puntos, por ejemplo (30495657):")
    dniIngresado = input("")
    try:
        with open(archivo,'r', newline='') as file:
            lectura_csv = csv.DictReader(file, delimiter=';')
            campos = lectura_csv.fieldnames
            sumaTotalTodosLosBeneficiarios = 0
            sumaTotalBeneficiarioSeleccionado = 0
            prestaciones = []
            saldosPrestaciones = []
            cantidadConsultasPrestaciones = []
            for linea in lectura_csv:
                dni = linea[campos[0]]
                prestacion = linea[campos[1]]
                saldo = float(linea[campos[2]].replace(",","."))
                sumaTotalTodosLosBeneficiarios += saldo
                if (dni == dniIngresado ):
                    sumaTotalBeneficiarioSeleccionado += saldo
                    #busco la prestacion en la lista para ver si ya está, si ya está sumo el saldo, sino la agrego
                    contador = 0
                    encontroPrestacion = False
                    for prestacionItemLista in prestaciones:
                        if prestacionItemLista == prestacion:
                            saldosPrestaciones[contador] += saldo
                            cantidadConsultasPrestaciones[contador] += 1
                            encontroPrestacion = True
                            break
                        contador = contador + 1
                    
                    if encontroPrestacion == False:
                        prestaciones.append(prestacion)
                        saldosPrestaciones.append(saldo)
                        cantidadConsultasPrestaciones.append(1)
                    print(prestaciones)
                    print(saldosPrestaciones)
                    print(cantidadConsultasPrestaciones)

            print("")
            print("Prestaciones:")
            contador = 0
            for prestacionItemLista in prestaciones:
                print(f"{prestacionItemLista}, cantidad de consultas: {cantidadConsultasPrestaciones[contador]}, saldo{saldosPrestaciones[contador]}")
                contador = contador + 1
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