import os.path
import csv
import variablesGlobales as g
from impresiones import (imprimirSalto, imprimirEncabezadoClientes, imprimirEncabezadoViajes)
from impresiones import (imprimirMensajeConSalto, imprimirRegistroCliente, imprimirTotalUsuariosEmpresa)
from impresiones import (imprimirRegistroViaje, imprimirClientes, imprimirViajes, imprimirMensajeConSaltoSuperior)
from logs import (loguear)
from archivos import (validarIngresoArchivo, ingresoNombreArchivo, validarArchivoClientes)
from archivos import (validarArchivoViajes, traerListaArchivoVentasOrdenado)

def buscarCliente(archivoClientes, camposClientes, nombreIngresado):
    #Hace una búsqueda de clientes por nombre ingresado.
    #Devuelve los clientes que tienen adentro de su nombre el valor ingresado por parámetro.
    #Por ejemplo si ingreso "pedro", va a traer todos los que tengan ese valor dentro del nombre (pedro gutierrez, pedro ramirez)    
    try:
        resultadoLog = "OK"
        lista = []
        with open(archivoClientes,'r', newline='', encoding="utf8") as file_clientes:
            lectura_clientes_csv = csv.DictReader(file_clientes)
            for linea in lectura_clientes_csv:
                if linea[camposClientes[g.COLUMNA_CLIENTES_NOMBRE]].lower().find(nombreIngresado)> -1:
                    lista.append(linea)
            if (len(lista) == 0):
                imprimirMensajeConSalto("No se encontró ningún registro que contenga el nombre ingresado.")
            else:
                imprimirSalto()
                imprimirClientes(camposClientes, lista)
                imprimirSalto()
    except IOError:
        resultadoLog = "Ocurrió un error al querer operar con el archivo."
        imprimirMensajeConSalto(resultadoLog)
    except:
        resultadoLog = "Ocurrió un error genérico."
        imprimirMensajeConSalto(resultadoLog)
    finally: 
        loguear(archivoClientes, "_", "Buscar cliente", resultadoLog, nombreIngresado)

def totalUsuariosPorEmpresa(archivoClientes, camposClientes, empresaIngresada):
    #Trae el total de usuarios por empresa
    #De la misma forma que el la funcion "buscarCliente", con poner parte del nombre alcanza.
    #Si dos empresas en su nombre contienen la variable "empresaIngresada" trae las dos.
    #Si el usuario no ingresa ninguna empresa, muestra todas.
    try:
        resultadoLog = "OK"
        lista = []
        with open(archivoClientes,'r', newline='', encoding="utf8") as file_clientes:
            lectura_clientes_csv = csv.DictReader(file_clientes)
            empresa = ""
            contadorUsuarios = 0
            for linea in lectura_clientes_csv:
                if (empresaIngresada != "" and linea[camposClientes[g.COLUMNA_CLIENTES_EMPRESA]].lower().strip().find(empresaIngresada) == -1):
                    continue
                if empresa != "" and empresa != linea[camposClientes[g.COLUMNA_CLIENTES_EMPRESA]]:
                    imprimirTotalUsuariosEmpresa(empresa, contadorUsuarios)
                    imprimirSalto()
                    imprimirClientes(camposClientes, lista)
                    imprimirSalto()
                    lista = []
                    contadorUsuarios = 0
                empresa = linea[camposClientes[g.COLUMNA_CLIENTES_EMPRESA]]
                lista.append(linea)
                contadorUsuarios += 1
            if len(lista) > 0:
                imprimirTotalUsuariosEmpresa(empresa, contadorUsuarios)
                imprimirSalto()
                imprimirClientes(camposClientes, lista)
                imprimirSalto()
            else:
                imprimirMensajeConSalto("No se encontró ninguna empresa.")
    except IOError:
        resultadoLog = "Ocurrió un error al querer operar con el archivo."
        imprimirMensajeConSalto(resultadoLog)
    except:
        resultadoLog = "Ocurrió un error genérico."
        imprimirMensajeConSalto(resultadoLog)
    finally: 
        loguear(archivoClientes, "", "Total de usuarios por empresa", resultadoLog, empresaIngresada)

def totalDineroPorEmpresa(archivoClientes, archivoViajes, camposClientes, empresaIngresada):
    #Trae el total de dinero por viajes de la empresa ingresada.
    #De la misma forma que la función "buscarCliente", con poner parte del nombre alcanza,
    #pero si hay dos nombres de empresas que contienen la variable "empresaIngresada"
    #devuelve un error indicando que el usuario escriba mejor el nombre.
    #Se tiene que ingresar sí o sí una empresa.
    resultadoLog = "OK"
    continuar = True
    if (empresaIngresada == ""):
        resultadoLog = "Debe ingresar al menos el nombre de una empresa"
        continuar = False
        imprimirMensajeConSalto(resultadoLog)
        loguear(archivoClientes, archivoViajes, "Total de dinero por empresa", resultadoLog, empresaIngresada)
        return
    
    try:
        listaEmpresas = []
        listaClientes = []
        with open(archivoClientes,'r', newline='', encoding="utf8") as file_clientes:
            lectura_clientes_csv = csv.DictReader(file_clientes)
            for linea_cliente in lectura_clientes_csv:
                if (linea_cliente[camposClientes[g.COLUMNA_CLIENTES_EMPRESA]].lower().strip().find(empresaIngresada) == -1):
                    continue
                listaClientes.append(linea_cliente)
                if (not (linea_cliente[camposClientes[g.COLUMNA_CLIENTES_EMPRESA]] in listaEmpresas)):
                    listaEmpresas.append(linea_cliente[camposClientes[g.COLUMNA_CLIENTES_EMPRESA]])
        
        continuar = True
        if len(listaClientes) == 0:
            resultadoLog = "No se encontró ninguna empresa."
            imprimirMensajeConSalto(resultadoLog)
            continuar = False
        
        if len(listaEmpresas) > 1:
            resultadoLog = "Con el nombre que ingresaste se encontró más de una empresa. Ingrese otra vez la empresa, esta vez ingresando mejor el nombre."
            imprimirMensajeConSalto(resultadoLog)
            continuar = False
        
        if (continuar):
            listaClientes.sort(key = lambda i: i['Documento'])
            listaViajes = traerListaArchivoVentasOrdenado(archivoViajes)
            c = 0 #contador para recorrer clientes
            v = 0 #contador para recorrer viaje
            suma = 0
            while c < len(listaClientes):
                while c<len(listaClientes) and v<len(listaViajes) and listaViajes[v]["Documento"] <= listaClientes[c]["Documento"]:
                    if listaClientes[c]["Documento"] == listaViajes[v]["Documento"]:
                        suma = suma + float(listaViajes[v]["monto"])
                    v += 1
                c += 1
            sumaFormateada = "{:.2f}".format(suma)
            imprimirMensajeConSalto(f"{listaEmpresas[0]} {sumaFormateada}")
    except IOError:
        resultadoLog = "Ocurrió un error al querer operar con el archivo."
        imprimirMensajeConSalto(resultadoLog)
    except:
        resultadoLog = "Ocurrió un error genérico."
        imprimirMensajeConSalto(resultadoLog)
    finally: 
        loguear(archivoClientes, archivoViajes, "Total de dinero por empresa", resultadoLog, empresaIngresada)

def totalDineroPorDocumento(archivoClientes, archivoViajes, camposClientes, camposViajes, documentoIngresado):
    #Permite obtener la cantidad total de viajes realizados y monto total por documento, 
    #Muestra los datos del empleado y los viajes.
    #Es obligatorio ingresar un documento.
    if (documentoIngresado == ""):
        imprimirMensajeConSalto("Debe ingresar un documento.")
        loguear(archivoClientes, archivoViajes, "Total de dinero por documento", "Debe ingresar un documento.", documentoIngresado)
        return
    if (not documentoIngresado.isnumeric()):
        imprimirMensajeConSalto("El documento tiene que se numérico.")
        loguear(archivoClientes, archivoViajes, "Total de dinero por documento", "El documento tiene que se numérico.", documentoIngresado)
        return

    try:
        resultadoLog = "OK"
        listaClientes = []
        with open(archivoClientes,'r', newline='', encoding="utf8") as file_clientes:
            lectura_clientes_csv = csv.DictReader(file_clientes)
            #asumo que solo puede haber un cliente por empresa
            for linea_cliente in lectura_clientes_csv:
                if (linea_cliente[camposClientes[g.COLUMNA_CLIENTES_DOCUMENTO]].strip() == documentoIngresado):
                    listaClientes.append(linea_cliente)
                    break
        
        if len(listaClientes) == 0:
            resultadoLog = "No se encontró ningun cliente con ese número de dni."
            imprimirMensajeConSalto(resultadoLog)
        else:
            listaViajes = traerListaArchivoVentasOrdenado(archivoViajes)
            c = 0 #contador para recorrer clientes
            v = 0 #contador para recorrer viajes
            cantidadViajes = 0
            sumaMonto = 0
            listaViajesImprimir = []
            while c < len(listaClientes):
                while c<len(listaClientes) and v<len(listaViajes) and listaViajes[v]["Documento"] <= listaClientes[c]["Documento"]:
                    if listaClientes[c]["Documento"] == listaViajes[v]["Documento"]:
                        sumaMonto = sumaMonto + float(listaViajes[v]["monto"])
                        cantidadViajes += 1
                        listaViajesImprimir.append(listaViajes[v])
                    v += 1
                c += 1
            sumaMontoFormateada = "{:.2f}".format(sumaMonto)
            imprimirMensajeConSaltoSuperior(f"Documento: {documentoIngresado}")
            imprimirSalto()
            imprimirClientes(camposClientes, listaClientes)
            imprimirMensajeConSalto(f"Total de viajes: {cantidadViajes}, Monto: {sumaMontoFormateada}")
            imprimirViajes(camposViajes, listaViajesImprimir)
            imprimirSalto()
    except IOError:
        resultadoLog = "Ocurrió un error al querer operar con el archivo."
        imprimirMensajeConSalto(resultadoLog)
    except:
        resultadoLog = "Ocurrió un error genérico."
        imprimirMensajeConSalto(resultadoLog)
    finally: 
        loguear(archivoClientes, archivoViajes, "Total de dinero por documento", resultadoLog, documentoIngresado)
    
def main():
    archivoValido = False
    while not archivoValido:
        archivoClientes = ingresoNombreArchivo("Clientes")
        if (archivoClientes.upper()) == "N":
            exit()
        camposClientes = []
        archivoValido, camposClientes = validarArchivoClientes(archivoClientes, camposClientes)
    
    archivoValido = False
    while not archivoValido:
        archivoViajes = ingresoNombreArchivo("Viajes")
        if (archivoViajes.upper()) == "N":
            exit()
        camposViajes = []
        archivoValido, camposViajes = validarArchivoViajes(archivoViajes, camposViajes)

    opcion = ""
    opcionesPosibles = "1.Buscar cliente \n"
    opcionesPosibles += "2.Obtener los datos de los usuarios por empresas \n"
    opcionesPosibles += "3.Obtener total de dinero por empresa \n"
    opcionesPosibles += "4.Obtener cantidad total de viajes realizados y monto total por documento \n"
    opcionesPosibles += "5.Salir"

    while opcion != "5":
        print("\n")
        print(f"Elija una opcion: \n{opcionesPosibles}")
        opcion = input("")
        if opcion == "1":
            buscarCliente(archivoClientes, camposClientes, input("Ingrese el nombre del cliente que desea buscar: ").lower().strip())
            continue

        if opcion == "2":
            totalUsuariosPorEmpresa(archivoClientes, camposClientes, input("Ingrese el nombre de la empresa que desea buscar (si no ingresa nada le va a traer todas): ").lower().strip())
            continue
    
        if opcion == "3":
            totalDineroPorEmpresa(archivoClientes, archivoViajes, camposClientes, input("Ingrese el nombre de la empresa que desea buscar (asegurese de que el nombre que ingrese no se repita entre empresas): ").lower().strip())
            continue

        if opcion == "4":
            totalDineroPorDocumento(archivoClientes, archivoViajes, camposClientes, camposViajes, input("Ingrese el documento que desea buscar: ").lower().strip())
            continue

        if opcion == "5":
            loguear(archivoClientes, archivoViajes, "Salir", "Salir", "_")
            exit()
        
        imprimirMensajeConSalto("Elija una opción posible!!")

main()