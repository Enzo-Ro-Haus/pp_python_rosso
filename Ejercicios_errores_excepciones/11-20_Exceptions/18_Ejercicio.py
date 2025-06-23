# Completá cada bloque añadiendo los except específicos necesarios
# (no usar except hasta atrapar todos los errores presentes en el ejercicio)

try:
    datos = input("Ingresá dos números separados por coma: ")
    x_str, y_str, z_str = datos.split(",")
    x = int(x_str)
    y = int(y_str)
    z = int(z_str)
    print("El resultado es", 100 / (x - y))
    print("Programa correcto")

#Completar aquí