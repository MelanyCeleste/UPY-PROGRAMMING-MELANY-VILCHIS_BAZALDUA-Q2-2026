#Digito verificador

#Obtener el numero sin digito verificador y pedir al usuario que ingrese el rol como string
rol = input("Ingrese el rol sin digito verificador: ")
#Invertir el numero rol para facilitar el calculo del digito verificador
rol_invertido = rol[::-1]