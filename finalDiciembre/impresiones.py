from variablesGlobales import *

def imprimirSalto():
    print(f"--------------------------------------------------------------------------------------------------------------------------------")

def imprimirEncabezadoClientes():
    print ("[Nombre, dirección, documento, fecha de alta, correo electrónico, empresa]")

def imprimirEncabezadoViajes():
    print ("[Documento, fecha, monto]")

def imprimirTotalUsuariosEmpresa(empresa, contadorUsuarios):
    imprimirSalto()
    print(f"Empresa: {empresa}")
    print(f"Total de usuarios: {contadorUsuarios}")

def imprimirMensajeConSalto(mensaje):
    #Imprime mensaje separado con saltos
    imprimirSalto()
    print(mensaje)
    imprimirSalto()

def imprimirMensajeConSaltoSuperior(mensaje):
    #Imprime mensaje con solo el salto superior
    imprimirSalto()
    print(mensaje)

def imprimirRegistroCliente(camposClientes, registro):
    print (f"[{registro[camposClientes[COLUMNA_CLIENTES_NOMBRE]]}, {registro[camposClientes[COLUMNA_CLIENTES_DIRECCION]]}, {registro[camposClientes[COLUMNA_CLIENTES_DOCUMENTO]]}, {registro[camposClientes[COLUMNA_CLIENTES_FECHA_ALTA]]}, {registro[camposClientes[COLUMNA_CLIENTES_CORREO]]}, {registro[camposClientes[COLUMNA_CLIENTES_EMPRESA]]}]")

def imprimirRegistroViaje(camposViajes, registro):
    print (f"[{registro[camposViajes[COLUMNA_VIAJES_DOCUMENTO]]}, {registro[camposViajes[COLUMNA_VIAJES_FECHA]]}, {registro[camposViajes[COLUMNA_VIAJES_MONTO]]}]")

def imprimirClientes(camposClientes, lista):
    #Imprime una lista de clientes ordenada por nombre
    imprimirEncabezadoClientes()
    lista.sort(key = lambda i: i['Nombre'])
    for registro in lista:
        imprimirRegistroCliente(camposClientes, registro)

def imprimirViajes(camposViajes, lista):
    #Imprime una lista de viajes
    imprimirEncabezadoViajes()
    for registro in lista:
         imprimirRegistroViaje(camposViajes, registro)