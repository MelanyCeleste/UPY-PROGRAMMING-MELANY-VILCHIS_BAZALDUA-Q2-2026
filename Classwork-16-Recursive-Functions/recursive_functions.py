
#recursiva
def recursiva(n):
    # Validamos que n sea un numero entero 
    if not isinstance(n, int):
        raise TypeError(f"n debe ser un entero")

    # Validamos que n no sea negativo
    if n < 0:
        raise ValueError("n no puede ser negativo")
    if n == 0:
        return "Done!"
    else:
        print(n)
        return recursiva(n - 1)

#Fibonacci
def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError(f"n debe ser un entero")

    if n < 0:
        raise ValueError("n no puede ser negativo")

    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#Factorial
def factorial(n):
    if not isinstance(n, int):
        raise TypeError(f"n debe ser un entero")

    if n < 0:
        raise ValueError("n no puede ser negativo")

    if n == 0 or n == 1:
        return 1
    else:
        return factorial(n - 1) * n


#Recursive multiplication
def multiplicacion_recursiva(n, m):
    if not isinstance(m, int):
        raise TypeError(f"m debe ser un entero")

    if m < 0:
        raise ValueError("m no puede ser negativo")

    if m == 0:
        return 0
    else:
        return multiplicacion_recursiva(n, m - 1) + n


#division_entera_recursiva
def division_entera_recursiva(dividendo, divisor):
    if not isinstance(dividendo, int) or not isinstance(divisor, int):
        raise TypeError("dividendo y divisor deben ser enteros")

    if divisor == 0:
        raise ZeroDivisionError("El divisor no puede ser 0")

    if dividendo < 0:
        raise ValueError("no se pueden utilizar dividendos negativos")

    if dividendo - divisor < 0:
        return 0
    else:
        return division_entera_recursiva(dividendo - divisor, divisor) + 1


#potencia_recursiva
def potencia_recursiva(base, exponente):
    if not isinstance(exponente, int):
        raise TypeError(f"exponente debe ser un entero")

    if exponente < 0:
        raise ValueError("Esta funcion no soporta exponentes negativos")

    if exponente == 0:
        return 1
    else:
        return potencia_recursiva(base, exponente - 1) * base


#serie_collatz
def serie_collatz(n):
    if not isinstance(n, int):
        raise TypeError(f"n debe ser un entero")

    if n <= 0:
        raise ValueError("n debe ser un entero positivo (mayor a 0)")

    if n == 1:
        print("END!")
        return 0
    else:
        if n % 2 == 0:
            print(n // 2)
            return serie_collatz(n // 2)
        else:
            print(3 * n + 1)
            return serie_collatz(3 * n + 1)


#aplanar_json
def aplanar_json(diccionario, clave_padre='', separador='.'):
    if not isinstance(diccionario, dict):
        raise TypeError(
            f"Se esperaba un diccionario, se recibio: {type(diccionario).__name__}"
        )

    elementos = []
    for key, value in diccionario.items():
        nueva_llave = f"{clave_padre}{separador}{key}" if clave_padre else key
        if isinstance(value, dict):
            elementos.extend(aplanar_json(value, nueva_llave, separador).items())
        else:
            elementos.append((nueva_llave, value))
    return dict(elementos)