class ArchivoConfigNoEncontradoError(Exception):
    pass

class FormatoConfigInvalidoError(Exception):
    pass

class ValorConfigInvalidoError(Exception):
    pass

class ParametroConfigFaltanteError(Exception):
    pass

class DimensionInvalidaError(Exception):
    pass


config = {}

try:
    
    try:
        archivo = open("config.txt", "r")
    except FileNotFoundError:
        raise ArchivoConfigNoEncontradoError("No se encontró el archivo 'config.txt'. Verifica que exista en la misma carpeta que el script.")

    for numero_linea, linea in enumerate(archivo, start=1):
        linea = linea.strip()
        if not linea:
            continue  

        try:
            clave, valor = linea.split("=")
        except ValueError:
            raise FormatoConfigInvalidoError(f"Línea {numero_linea} mal formada: '{linea}'. Se esperaba el formato clave=valor.")

        try:
            config[clave] = float(valor)
        except ValueError:
            raise ValorConfigInvalidoError(f"Línea {numero_linea}: el valor '{valor}' de '{clave}' no es un número válido.")

    archivo.close()
    
    parametros_requeridos = (
        "ancho", "alto", "max_iter",
        "real_min", "real_max", "imag_min", "imag_max")
    
    for parametro in parametros_requeridos:
        if parametro not in config:
            raise ParametroConfigFaltanteError(f"Falta el parámetro '{parametro}' en config.txt" )

    ancho, alto, max_iter = int(config["ancho"]), int(config["alto"]), int(config["max_iter"])

    if ancho <= 0 or alto <= 0:
        raise DimensionInvalidaError("Los valores de 'ancho' y 'alto' deben ser mayores a 0 para poder calcular la imagen.")

    salida = open("clase.csv", "w")
    salida.write("fila,columna,iteraciones\n")
    for fila in range(alto):
        for columna in range(ancho):
            real = config["real_min"] + (columna/ancho) * (config["real_max"] - config["real_min"])
            imag = config["imag_min"] + (fila/alto) * (config["imag_max"] - config["imag_min"])
            c = complex(real, imag)

            z = 0 + 0j
            iteraciones = 0
            while (abs(z) <= 2) and (iteraciones < max_iter):
                z = z * z + c
                iteraciones += 1

            salida.write(f"{fila},{columna},{iteraciones}\n")
    salida.close
    print("DONE")

except (ArchivoConfigNoEncontradoError,
        FormatoConfigInvalidoError,
        ValorConfigInvalidoError,
        ParametroConfigFaltanteError,
        DimensionInvalidaError) as e:
    print(f"Error: {e}")