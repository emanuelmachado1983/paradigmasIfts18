import os.path
import datetime
import csv
from impresiones import (imprimirMensajeConSalto)

def loguear(archivoClientes, archivoViajes, opcionMenu, resultado, parametros):
    #Realiza logs en un archivo.
    try:
        fechaHoy = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        campos = ['fecha', 'opcionMenu', 'archivoClientes', 'archivoViajes', 'resultado', 'parametros']

        archivo = "log.csv"
        tipoAperturaArchivo = "a"
        if not os.path.isfile(archivo):
            tipoAperturaArchivo = "w"

        with open("log.csv", tipoAperturaArchivo, newline='') as file:
            archivoGuardar = csv.DictWriter(file, fieldnames=campos)

            if tipoAperturaArchivo == "w":
                archivoGuardar.writeheader()

            archivoGuardar.writerow({'fecha': fechaHoy, 'opcionMenu': opcionMenu, 'archivoClientes': archivoClientes, 'archivoViajes': archivoViajes, 'resultado': resultado, 'parametros': parametros })
            return
    except IOError:
        imprimirMensajeConSalto("Error al manipular el archivo de logs.")
    except:
        imprimirMensajeConSalto("Error genérico al manipular el archivo de logs.")