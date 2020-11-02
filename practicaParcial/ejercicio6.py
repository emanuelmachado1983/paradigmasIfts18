def tablaMultiplicar(numero):
    try:
        nombreArchivo = "tabla-" + str(numero) + ".txt"
        with open(nombreArchivo, 'w') as f:
            for i in range(13):
                #print(f"{numero} * {i} = {numero * i}")
                f.write(f"{numero} * {i} = {numero * i}\n")
    except IOError:
        print("Se produjo un error en el manejo del archivo")
    except:
        print("Se produjo un error")

tablaMultiplicar (10)