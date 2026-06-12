#Digito verificador

#Obtener el numero sin digito verificador y pedir al usuario que ingrese el rol como string
rol = input("Ingrese el rol sin digito verificador: ")
#Invertir el numero rol para facilitar el calculo del digito verificador
rol_invertido = rol[::-1]
#Multiplicar los digitos por la secuencia
multiplicadores = [2, 3, 4, 5, 6, 7]
suma = 0
#iniciar ciclo para multiplicar cada digito por su multiplicador y sumar los resultados
for i in range(len(rol_invertido)):
    digito = int(rol_invertido[i])
    multiplicador = multiplicadores[i % len(multiplicadores)]
    suma += digito * multiplicador