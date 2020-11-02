import os.path
import csv

def eje8_guardar(archivo, campos, textoGenericoSingular, textoGenericoPlural):
    guardar = "si"
    lista = []
    while guardar == "si":
        item = {}

        for campo in campos:
            item[campo] = input(f"Ingrese {campo} del {textoGenericoSingular}: ")
        lista.append(item)
        guardar = input(f"Desea seguir agregando {textoGenericoPlural}? si/no")

    try:
        archivo_existe = os.path.isfile(archivo)
        with open(archivo, 'a', newline='') as file:
            file_guarda = csv.DictWriter(file, fieldnames=campos)

            if not archivo_existe:
                file_guarda.writeheader()

            file_guarda.writerows(lista)
            print("se guardó correctamente")
            return
    except IOError:
        print("Ocurrió un error con el archivo.")
    except:
        print("Hubo un error génerico en la operación a la hora de guardar el archivo")

def eje8_listar(archivoAlumnos, archivoMaterias):
    try:
        with open(archivoAlumnos,'r', newline='') as fileAlumnos:
            lectura_alumnos_csv = csv.DictReader(fileAlumnos)
            camposAlumnos = lectura_alumnos_csv.fieldnames
            for lineaAlumnos in lectura_alumnos_csv:
                #texto = "f"{linea[campos[1]]} {linea[campos[2]]}"
                with open(archivoMaterias,'r', newline='') as fileMaterias:
                    lectura_materias_csv = csv.DictReader(fileMaterias)
                    camposMaterias = lectura_materias_csv.fieldnames
                    adeudaMaterias = False
                    for lineaMaterias in lectura_materias_csv:
                        if lineaMaterias[camposMaterias[0]] == lineaAlumnos[camposMaterias[0]]:
                            print(f"{lineaAlumnos[camposAlumnos[1]]} {lineaAlumnos[camposAlumnos[2]]} debe la materia {lineaMaterias[camposMaterias[1]]} del año {lineaMaterias[camposMaterias[2]]}")
                            adeudaMaterias = True
                    if adeudaMaterias == False:
                        print(f"{lineaAlumnos[camposAlumnos[1]]} {lineaAlumnos[camposAlumnos[2]]} no adeuda materias de ningún año")
            return
    except IOError:
        print("Ocurrio un error con el archivo")
    #except:
    #    print("Ocurrio un error genérico a la hora de hacer el listado")

def ejercicio8():
    ARCHIVO_ALUMNOS = "alumnos.csv"
    ARCHIVO_MATERIAS = "deuda_materias.csv"
    CAMPOS = ['DNI', 'Apellido', 'Nombre', 'Año', 'Comision']

    while True:
        print("Elija una opcion: \n 1.Guardar datos \n 2.Listar datos \n 3.Salir")
        opcion = input("")

        if opcion == "3":
            exit()
        if opcion == "1":
            eje8_guardar(ARCHIVO_ALUMNOS, CAMPOS, "alumno", "alumnos")
        if opcion == "2":
            eje8_listar(ARCHIVO_ALUMNOS, ARCHIVO_MATERIAS)
        else:
            print("Por favor elija una opcion valida")

ejercicio8()