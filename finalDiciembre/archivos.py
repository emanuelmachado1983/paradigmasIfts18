import os.path
import csv
import variablesGlobales as g

def ingresoNombreArchivo(textoArchivo):
    #Función para ingresar un archivo.
    nombreArchivo = ""
    archivoValido = False
    while not archivoValido:
        nombreArchivo = input(f"Ingrese el nombre de archivo de {textoArchivo} con el que va a trabajar (Ingresa 'N' si querés salir): ".strip())
        archivoValido = validarIngresoArchivo(nombreArchivo)
    if nombreArchivo.upper() == "N":
        return nombreArchivo
    if (len(nombreArchivo.split("."))==1):  #estoy seguro de que si tiene un punto es csv, porque ya lo validé en la función "validarIngresoArchivo"
        return nombreArchivo + ".csv" 
    else:
        return nombreArchivo 

def validarIngresoArchivo(nombreArchivo):
    #Valida el ingreso de un archivo.
    if nombreArchivo == "":
        print ("El nombre de archivo ingresado no puede ser vacío")
        return False
    vectorAux = nombreArchivo.split(".")
    if len(vectorAux) > 2:
        print ("El nombre del archivo no puede contener más de un '.'.")
        return False
    if len(vectorAux) == 2:
        if vectorAux[1] != "csv":
            print ("Solo se pueden ingresar archivos .csv")
            return False
    return True

def validarDocumento (documento, listaErrores, x):
    try:
        int(documento)
    except ValueError:
        listaErrores.append(f"Linea {x}: El documento tiene que ser un valor numérico.")
    if len(documento) != 7 and len(documento) != 8:
        listaErrores.append(f"Linea {x}: El documento solo puede ser de 7 o 8 caracteres.")

def validarCamposVacios(linea, listaErrores, x):
    for item in linea:
        if (linea[item]) == "":
            listaErrores.append(f"Linea {x}: El campo {item} no puede ser vacío.")

def validarArchivoClientes(archivoClientes, camposClientes):
    #Valida si el archivo de clientes tiene alguno de los siguientes problemas:
    #-Tiene algùn documento que no sea numérico.
    #-Los documentos tienen que ser de 7 u 8 caracteres.
    #-Los campos no pueden ser vacíos.
    #-El mail tiene que contener un ".".
    #-El mail no puede contener más de un ".".
    #-El mail tiene que contener un "@".
    #-El mail no puede contener más de un "@"
    try:
        with open(archivoClientes,'r', newline='', encoding="utf8") as file_clientes:
            lectura_clientes_csv = csv.DictReader(file_clientes)
            camposClientes = lectura_clientes_csv.fieldnames
            x=2
            listaErrores = []
            for linea in lectura_clientes_csv:
                #valido que los documentos sean numéricos
                documento = linea[camposClientes[g.COLUMNA_CLIENTES_DOCUMENTO]]
                validarDocumento (documento, listaErrores, x)
            
                #valido que no haya campos vacíos
                validarCamposVacios(linea, listaErrores, x)

                #valido mail
                mail = linea[camposClientes[g.COLUMNA_CLIENTES_CORREO]]
                if len(mail.split(".")) == 1:
                    listaErrores.append(f"Linea {x}: El mail tiene que contener un '.'.")
                if len(mail.split(".")) > 2:
                    listaErrores.append(f"Linea {x}: El mail tiene no puede contener más de un '.'.")
                if len(mail.split("@")) == 1:
                    listaErrores.append(f"Linea {x}: El mail tiene que contener el signo '@'.")
                if len(mail.split("@")) > 2:
                    listaErrores.append(f"Linea {x}: El mail no puede contener más de un signo '@'.")
                x += 1
        if (len(listaErrores) > 0):
            print ("Existen los siguientes errores con el archivo, no se podrá proseguir con el programa hasta que los corrija:")
            for item in listaErrores:
                print (item)
            return False, camposClientes
        return True, camposClientes

    except IOError:
        print("Ocurrió un error al querer operar con el archivo. Corrobore que este exista.")
        return False, camposClientes
    except:
        print("Hubo un error genérico operando el archivo.")
        return False, camposClientes

def validarArchivoViajes(archivoViajes, camposViajes):
    #Valida si el archivo de clientes tiene alguno de los siguientes problemas:
    #-El monto no es numérico.
    #-El monto tiene que tener dos decimales.
    #-Los documentos tienen que ser de 7 u 8 caracteres.
    #-Los campos no pueden ser vacíos.
    try:
        with open(archivoViajes,'r', newline='', encoding="utf8") as file_viajes:
            lectura_viajes_csv = csv.DictReader(file_viajes)
            camposViajes = lectura_viajes_csv.fieldnames
            listaErrores = []
            x = 2
            for linea in lectura_viajes_csv:
                #valido que los documentos sean numéricos
                documento = linea[camposViajes[g.COLUMNA_VIAJES_DOCUMENTO]]
                validarDocumento (documento, listaErrores, x)
            
                #valido que no haya campos vacíos
                validarCamposVacios(linea, listaErrores, x)

                monto = linea[camposViajes[g.COLUMNA_VIAJES_MONTO]]
                montoNumerico = True
                try:
                    float(monto)
                except ValueError:
                    listaErrores.append(f"Linea {x}: El monto no es númerico.")
                    montoNumerico = False
                if (montoNumerico):
                    if len(monto.split(".")) == 1:
                        listaErrores.append(f"Linea {x}: El monto tiene que tener dos decimales.")
                    else:
                        if len(monto.split(".")[1]) != 2:
                            listaErrores.append(f"Linea {x}: El monto tiene que tener dos decimales.")
                    
                x += 1
        if (len(listaErrores) > 0):
            print ("Existen los siguientes errores con el archivo, no se podrá proseguir con el programa hasta que los corrija:")
            for item in listaErrores:
                print (item)
            return False, camposViajes
        return True, camposViajes
    except IOError:
        print("Ocurrió un error al querer operar con el archivo. Corrobore que este exista.")
        return False, camposViajes
    except:
        print("Hubo un error genérico operando el archivo.")
        return False, camposViajes
        
def traerListaArchivoVentasOrdenado(archivo):
    #Trae el archivo de ventas ordenado en una lista
    lista = []
    with open(archivo,'r', newline='', encoding="utf8") as file_viajes:
        lectura_viajes_csv = csv.DictReader(file_viajes)
        for linea_viaje in lectura_viajes_csv:
            lista.append(linea_viaje)
    lista.sort(key = lambda i: i['Documento'])
    return lista