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
#Calcular el digito verificador usando el modulo 11
resto = suma % 11
if resto == 0:
    digito_verificador = '0'
elif resto == 1:
    digito_verificador = 'K'
else:
    digito_verificador = str(11 - resto)
#Mostrar el resultado al usuario
print(f"El digito verificador es: {digito_verificador}")
print("ROL completo:", rol + "-" + str(digito_verificador))