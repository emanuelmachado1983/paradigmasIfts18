import csv

def ingresarDatoString(texto):
    ingresoDatoCorrecto = False
    dato = ""
    while (not ingresoDatoCorrecto):
        dato = input(texto)
        if (dato == ""):
            print ("Ingrese el dato correctamente")
            print ("")
        ingresoDatoCorrecto = True
    return(dato)

def ingresarDatoNumerico(texto):
    ingresoDatoCorrecto = False
    dato = 0
    while (not ingresoDatoCorrecto):
        try:
            dato = int(input(texto))
            ingresoDatoCorrecto = True
        except:
            print ("Ingrese el dato correctamente")
            print ("")
    return(dato)

def ingresarUsario():
    print ("Ingrese los siguientes datos:")
    """
    apellido = ingresarDatoString("Ingrese apellido: ")
    nombre = ingresarDatoString("Ingrese nombre: ")
    fecha = ingresarDatoString("Ingresar fecha de ingreso: ")
    antiguedad = ingresarDatoString("Ingresar antiguedad: ")
    comisiones = ingresarDatoNumerico("comisiones: ")
    """
    apellido = "machado"
    nombre = "emanuel"
    fecha = "13/09"
    antiguedad = 5
    comisiones = 10
    rows = [{
        "Apellido": apellido,
        "Nombre": nombre,
        "Fecha de ingreso": fecha,
        "Antiguedad": antiguedad,
        "Comisiones": comisiones
    }]
    print(rows)
    try:
        with open("vendedores.csv", 'a', newline="") as f:
            csv_writer = csv.DictWriter(f, delimiter=',', fieldnames=['Apellido', 'Nombre', 'Fecha de ingreso','Antiguedad', 'Comisiones'])
            csv_writer.writeheader()
            csv_writer.writerows(rows)
    except:
        print ("")

def listarUsuario():
    with open('vendedores.csv', mode='r', newline="") as f:
        csv_reader = csv.DictReader(f)
        linea = 0
        for row in csv_reader:
            if linea == 0:
                print(f'Column names are {", ".join(row)}')
                linea = linea + 1
            print(f'\t{row["Nombre"]} {row["Apellido"]} trabaja en la empresa desde {row["Fecha de ingreso"]} y lleva comisionado {row["Comisiones"]}.')
            linea += 1

def eleccionOpciones():
    opcion = ""
    while (opcion != "3"):
        print ("1) Ingresar usuario nuevo")
        print ("2) Listar usuarios")
        print ("3) Salir del programa")
        opcion = input("Ingrese la opción que quiera realizar: ")
        if opcion != "1" and opcion != "2" and opcion != "3":
            print ("Opción incorrecta, las opciones posibles son 1, 2, o 3.")
        if opcion == "1":
            ingresarUsario()
        if opcion == "2":
            listarUsuario()
        print ("")

eleccionOpciones()