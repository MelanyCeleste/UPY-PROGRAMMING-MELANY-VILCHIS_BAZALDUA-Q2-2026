class DigitoVerificadorError(Exception):
    pass


check = True
while check:
    try:
        rol = input("Ingrese el rol: ")
        rol_sin_digito, digito = rol.split("-")
        check = False
    except ValueError:
        print("Rol inválido: No tiene el formato XXXXXXXXX-X")


valido = True

try:
    if not rol_sin_digito.isnumeric():
        raise ValueError("Los digitos del rol deben ser numéricos")
except ValueError as e:
    print(e)
    valido = False

try:
    if not digito.isnumeric():
        raise ValueError("El digito verificador debe ser numérico")
except ValueError as e:
    print(e)
    valido = False


if valido:
    invertido = rol_sin_digito[::-1]

    secuencia = [2, 3, 4, 5, 6, 7]
    suma = 0
    for index in range(len(invertido)):
        multiplicando = secuencia[index % 6]
        numero = int(invertido[index:index + 1])
        suma += numero * multiplicando

    total = suma % 11
    verificador = 11 - total

    try:
        if verificador != int(digito):
            raise DigitoVerificadorError(
                f"Error: El dígito verificador no coincide, se esperaba {verificador}"
            )
    except DigitoVerificadorError as e:
        print(e)
    else:
        print(f"{rol_sin_digito}-{verificador}")