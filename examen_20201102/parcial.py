import os.path
import csv

def listar(archivo):
    try:
        with open(archivo,'r', newline='') as f:
            lectura_empleados_csv = csv.DictReader(f)
            campos = lectura_empleados_csv.fieldnames
            for linea in lectura_empleados_csv:
                print (f"Legajo: {linea[campos[0]]}")
                print (f"Apellido: {linea[campos[1]]}")
                print (f"Nombre: {linea[campos[2]]}")
                print (f"Total de vacaciones: {linea[campos[3]]}")
                print ("")
            return
    except IOError:
        print("Ocurrió un error al querer operar con el archivo. Corrobore que este exista.")
    except:
        print("Ocurrio un error genérico a la hora de hacer el listado")

def decidirSiSobreescribirArchivo (archivo):
    if os.path.isfile(archivo):
        intentarDeNuevo = True
        respuesta = "no"
        while intentarDeNuevo:
            respuesta = input(f"El archivo ya existe. Desea sobreescribirlo? si/no: ")
            if respuesta != "si" and respuesta != "no":
                print ("Tenés que responder si o no")
            else:
                intentarDeNuevo = False
        return respuesta == "si"
    else:
        return True

def ingresarEmpleado(archivo, campos):
    guardar = "si"
    lista = []

    tipoAperturaArchivo = "a"
    if decidirSiSobreescribirArchivo(archivo):
        tipoAperturaArchivo = "w"

    while guardar == "si":
        item = {}
        for campo in campos:
            if campo == "Legajo" or campo == "Total Vacaciones":
                intentarDeNuevo = True
                while intentarDeNuevo:
                    try:
                        item[campo] = int(input(f"Ingrese {campo} del empleado: "))
                        intentarDeNuevo = False
                    except:
                        print(f"El campo {campo} debe ser numerico")
            else:
                item[campo] = input(f"Ingrese {campo} del empleado: ")
        lista.append(item)
        guardar = input(f"Desea seguir agregando empleados? si/no: ")

    try:
        with open(archivo, tipoAperturaArchivo, newline='') as file:
            file_guarda = csv.DictWriter(file, fieldnames=campos)

            if tipoAperturaArchivo == "w":
                file_guarda.writeheader()

            file_guarda.writerows(lista)
            print("El archivo se guardó correctamente.")
            return
    except IOError:
        rint("Ocurrió un error al querer operar con el archivo. Corrobore que este exista.")
    except:
        print("Ocurrió un error génerico en la operación.")

def informarDiasDisponibles(archivoEmpleados, archivoVacaciones, camposEmpleados):
    pass

def parcial():
    ARCHIVO_EMPLEADOS = "empleados.csv"
    ARCHIVO_VACACIONES = "dias.csv"
    CAMPOS_EMPLEADOS = ['Legajo', 'Apellido', 'Nombre', 'Total Vacaciones']

    while True:
        print("Elija una opcion: \n 1.Listar usuario \n 2.Ingresar usuario \n 3.Informar días disponibles \n 4.Salir")
        opcion = input("")

        if opcion == "4":
            exit()

        if opcion == "1":
            listar(ARCHIVO_EMPLEADOS)
            continue

        if opcion == "2":
            ingresarEmpleado(ARCHIVO_EMPLEADOS, CAMPOS_EMPLEADOS)
            continue
    
        if opcion == "3":
            informarDiasDisponibles(ARCHIVO_EMPLEADOS, ARCHIVO_VACACIONES, CAMPOS_EMPLEADOS)

        else:
            print("Por favor elija una opción válida")

parcial()