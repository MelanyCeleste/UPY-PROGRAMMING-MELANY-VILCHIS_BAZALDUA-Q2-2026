from PIL import Image

class ArchivoConfigNoEncontradoError(Exception):
    pass

class FormatoConfigInvalidoError(Exception):
    pass

class ValorConfigInvalidoError(Exception):
    pass

class ParametroIncompletoError(Exception):
    pass

class ArchivoDatosNoEncontradoError(Exception):
    pass

class ArchivoVacioError(Exception):
    pass

class FilaDatosInvalidaError(Exception):
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
        linea_limpia = linea.strip()
        if not linea_limpia:
            continue

        try:
            clave, valor = linea_limpia.split("=")
        except ValueError:
            raise FormatoConfigInvalidoError(f"Línea {numero_linea} mal formada: '{linea_limpia}'. Se esperaba el formato clave=valor.")

        try:
            config[clave] = float(valor) if "." in valor else int(valor)
        except ValueError:
            raise ValorConfigInvalidoError(f"Línea {numero_linea}: el valor '{valor}' de '{clave}' no es un número válido.")

    archivo.close()

    print(config)

    try:
        with open("clase.csv", "r") as data:
            datos = data.readlines()
    except FileNotFoundError:
        raise ArchivoDatosNoEncontradoError("No se encontró el archivo 'clase.csv'. Genera primero los datos del fractal.")

    parametros_requeridos = ("alto", "ancho", "max_iter")
    for parametro in parametros_requeridos:
        if parametro not in config:
            raise ParametroIncompletoError(f"Falta el parámetro '{parametro}' en config.txt")

    alto, ancho, max_iter = config["alto"], config["ancho"], config["max_iter"]

    if not (isinstance(alto, int) and isinstance(ancho, int)):
        raise DimensionInvalidaError("'alto' y 'ancho' deben ser números enteros en config.txt (sin punto decimal)")

    if alto <= 0 or ancho <= 0:
        raise DimensionInvalidaError("'alto' y 'ancho' deben ser mayores a 0")

    if max_iter <= 0:
        raise DimensionInvalidaError( "'max_iter' debe ser mayor a 0")

    img = Image.new("HSV",(ancho,alto))

    if not datos:
        raise ArchivoVacioError( "'clase.csv' está vacío, no hay datos para generar la imagen")

    #quitar encabezados
    encabezados = datos.pop(0)
    #print(encabezados)
    for numero_fila, dato in enumerate(datos, start=2):
        try:
            fila, columna, iteraciones= map(int, dato.strip().split(","))
        except ValueError:
            raise FilaDatosInvalidaError(f"Línea {numero_fila} de 'clase.csv' mal formada: '{dato.strip()}'.")

        brillo= 40 if (iteraciones==max_iter) else int((iteraciones/max_iter) * 255)
        try:
            img.putpixel((columna,fila), (brillo,255,255))
        except IndexError:
            raise FilaDatosInvalidaError(f"Línea {numero_fila} de 'clase.csv': la posición (columna={columna}, fila={fila}) "f"está fuera del tamaño de la imagen ({ancho}x{alto})")

    img_rgb= img.convert("RGB")
    img_rgb.save("mandelbrot-clase.png")

    print("DONE")

except (ArchivoConfigNoEncontradoError,
        FormatoConfigInvalidoError,
        ValorConfigInvalidoError,
        ParametroIncompletoError,
        ArchivoDatosNoEncontradoError,
        ArchivoVacioError,
        FilaDatosInvalidaError,
        DimensionInvalidaError) as e:
    print(f"Error: {e}")