import math

class LimiteInferiorError(Exception):
    pass


class LimiteSuperiorError(Exception):
    pass


class FuncionVaciaError(Exception):
    pass


class FuncionSinXError(Exception):
    pass


class FuncionInvalidaError(Exception):
    pass


class IntervaloInvertidoError(Exception):
    pass


class MetodoInvalidoError(Exception):
    pass


class FuncionNoDefinidaError(Exception):
    pass

a=(input("write the left endpoint of the interval: "))
b=(input("write the right endpoint of the interval: "))
f_x=input("write the function f(x) to integrate: ")
method=input("write the integration method to use (LRM/RRM/MRM/TRAP): ")
 
valido = True
 
try:
    try:
        if "pi" in a:
            a = eval(a.replace("pi", str(math.pi)))
        else:
            a = float(a)
    except (ValueError, SyntaxError, NameError):
        raise LimiteInferiorError("El límite inferior debe ser numérico")
except LimiteInferiorError as e:
    print(e)
    valido = False
 
try:
    try:
        if "pi" in b:
            b = eval(b.replace("pi", str(math.pi)))
        else:
            b = float(b)
    except (ValueError, SyntaxError, NameError):
        raise LimiteSuperiorError("El límite superior debe ser numérico")
except LimiteSuperiorError as e:
    print(e)
    valido = False
 
try:
    if f_x.strip() == "":
        raise FuncionVaciaError("La función ingresada no es válida")
    elif "x" not in f_x:
        raise FuncionSinXError("La función debe estar escrita en términos de x")
    else:
        try:
            eval(f_x.replace("x", "1.0"))
        except Exception:
            raise FuncionInvalidaError("La función ingresada no es válida")
except (FuncionVaciaError, FuncionSinXError, FuncionInvalidaError) as e:
    print(e)
    valido = False
 
if valido:
    try:
        if a >= b:
            raise IntervaloInvertidoError("El límite inferior debe ser menor que el límite superior")
    except IntervaloInvertidoError as e:
        print(e)
        valido = False
 
if valido:
    try:
        if method not in ("LRM", "RRM", "MPM", "TM"):
            raise MetodoInvalidoError("El método de integración no es válido. Usa LRM, RRM, MPM o TM")
    except MetodoInvalidoError as e:
        print(e)
        valido = False
 
 
if valido:
    n = 1000
    h = (b - a) / n
    area = 0.0
    constant = 0
    shift = 0
 
    if method == "RRM":
        shift = 1
    if method == "MPM":
        constant = h / 2
 
    try:
        try:
            if method == "TM":
                f_0 = f_x.replace("x", str(a))
                area += (h / 2) * eval(f_0)
                for i in range(1, n):
                    xi = a + i * h
                    f_xi = f_x.replace("x", str(xi))
                    area += h / 2 * 2 * eval(f_xi)
                f_xn = f_x.replace("x", str(b))
                area += (h / 2) * eval(f_xn)
            else:
                for i in range(shift, n + shift):
                    xi = a + i * h
                    height = f_x.replace("x", str(xi + constant))
                    area += h * eval(height)
        except ZeroDivisionError:
            raise FuncionNoDefinidaError("La función no está definida en algún punto del intervalo")
    except FuncionNoDefinidaError as e:
        print(e)
        valido = False
 
    if valido:
        print(f"The integration of {f_x} is {area:.3f}")