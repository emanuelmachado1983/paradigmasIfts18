import os.path
import csv

def listar(archivo):
# Funcion para realizar listado simple de empleados
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
# Función para decidir si se sobreescribe el archivo o no
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

def existeUsuarioArchivo (archivo, legajo):
    #Función que sirve para chequear si el legajo ya existe en el archivo
    #No hago el try catch acá. A propósito. La idea es que el error lo handlee la función que lo llama.
    #Si hago el try catch acá lo que va a pasar es que la función que lo llama siga de largo y no quiero 
    encontroEmpleado = False
    if os.path.isfile(archivo):
        with open(archivo,'r', newline='') as f:
            lectura_empleados_csv = csv.DictReader(f)
            campos = lectura_empleados_csv.fieldnames
            encontroEmpleado = False
            for linea in lectura_empleados_csv:
                if int(linea[campos[0]]) == legajo:
                    encontroEmpleado = True
                    break #lo encontró, no necesito seguir recorriendo el for
    
    return encontroEmpleado

def existeUsuarioLista (lista, legajo):
    #Función que sirve para chequear si el legajo está en la lista
    
    encontroEmpleado = False
    for item in lista:
        if item['Legajo'] == legajo:
            return True
    return encontroEmpleado

def textoAmigableCampo (texto):
#Es una funcion para que se muestre más amigable el texto que se muestra para algunos campos
    if texto == 'Legajo':
        return 'el legajo'
    if texto == 'Apellido':
        return 'el apellido'
    if texto == 'Nombre':
        return 'el nombre'
    if texto == 'Total Vacaciones':
        return 'el total de vacaciones'
    return texto

def ingresarEmpleado(archivo, campos):
 # Función para realizar el ingreso de un empleado
    print ("ACLARACION: Los empleados no se verán impactados en el archivo hasta que no termine de cargarlos todos.")
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
                        item[campo] = int(input(f"Ingrese {textoAmigableCampo(campo)} del empleado: "))
                        #tengo que chequear si el legajo existe
                        if tipoAperturaArchivo != "w" and campo == "Legajo" and existeUsuarioArchivo(archivo, item[campo]): 
                            print(f"El legajo ya existe")
                        else:
                            if campo == "Legajo" and existeUsuarioLista(lista, item[campo]):
                                print(f"El legajo ya existe")
                            else:
                                intentarDeNuevo = False
                    except ValueError:
                        print(f"El campo {campo} debe ser numerico")
                    except IOError:
                        print("Ocurrió un error al querer operar con el archivo a la hora de buscar si existe el legajo.")
                        return
                    
            else:
                item[campo] = input(f"Ingrese {textoAmigableCampo(campo)} del empleado: ")
            
            
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
        print("Ocurrió un error al querer operar con el archivo. Corrobore que este exista.")
    except:
        print("Ocurrió un error génerico en la operación.")

def informarDiasDisponibles(archivoEmpleados, archivoVacaciones):
#función para informar días disponibles
    intentarDeNuevo = True
    legajoIngresado = 0
    while intentarDeNuevo:
        try:
            legajoIngresado = int(input(f"Ingrese legajo del empleado: "))
            intentarDeNuevo = False
        except:
            print(f"El dato ingresado tiene que ser numérico")
    
    try:
        cantidadDiasTomados = 0
        #abro el archivo de empleados como siempre
        with open(archivoEmpleados,'r', newline='') as file_empleados:
            lectura_empleados_csv = csv.DictReader(file_empleados)
            campos_empleados = lectura_empleados_csv.fieldnames
            legajoEncontrado = False
            for lineaEmpleados in lectura_empleados_csv:
                legajo = int(lineaEmpleados[campos_empleados[0]])
                if legajo != legajoIngresado:
                    continue
                apellido = lineaEmpleados[campos_empleados[1]]
                nombre = lineaEmpleados[campos_empleados[2]]
                totalVacaciones = int(lineaEmpleados[campos_empleados[3]])
                #recorro todo el archivo de vaciones. Lo recorro todo porque en ningún momento se aclaró que estaba ordenado
                #como supongo que no está ordenado, tengo que recorrerlo todo para asegurarme que sumo todas las vacaciones 
                with open(archivoVacaciones,'r', newline='') as file_vacaciones:
                    lectura_vacaciones_csv = csv.DictReader(file_vacaciones)
                    for lineaVacaciones in lectura_vacaciones_csv:
                        campos_vacaciones = lectura_vacaciones_csv.fieldnames
                        if int(lineaVacaciones[campos_vacaciones[0]]) == legajo:
                            cantidadDiasTomados += 1
                print (f"Legajo {legajo} : {nombre} {apellido}, le restan {totalVacaciones - cantidadDiasTomados} días de vacaciones")
                legajoEncontrado = True
                break #en este punto ya se encontró el legajo así que salgo del for, así no recorro todo sin necesidad.
            if not legajoEncontrado: 
                print ("Legajo no encontrado")
    except IOError:
        print("Ocurrió un error al querer operar con los archivos. Corrobore que existan.")
    #except:
    #    print("Ocurrio un error genérico a la hora de hacer el listado")

def parcial():
    ARCHIVO_EMPLEADOS = "empleados.csv"
    ARCHIVO_VACACIONES = "dias.csv"

    #Hay ciertas validaciones que se hacen con estos campos, así que por favor no cambiar los titulos de los campos
    CAMPOS_EMPLEADOS = ['Legajo', 'Apellido', 'Nombre', 'Total Vacaciones']

    while True:
        print("Elija una opcion: \n 1.Listar usuarios \n 2.Ingresar usuario \n 3.Informar días disponibles de vacaciones \n 4.Salir")
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
            informarDiasDisponibles(ARCHIVO_EMPLEADOS, ARCHIVO_VACACIONES)

        else:
            print("Por favor elija una opción válida")

parcial()