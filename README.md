# pp_python_rosso

# SOLUCIONES COMENTADAS DE TODOS LOS EJERCICIOS

# === 1_2_SyntaxError ===
# 1. Crear el error:
# Error forzado (no ejecutar este código):
# def saludar()  
#     print("Hola")

# 2. Corregir el error:
if True:
    print("¡Funciona!")

# === 3_4_NameError ===
# 3. Crear el error:
mensaje = "¡Hola, programador!"
print(mensaje)

# 4. Corregir el error:
contador = 10
print(contador + contador)

# === 5_6_TypeError ===
# 5. Crear el error:
numero = 5
otro_numero = 10
resultado = numero + otro_numero
print(resultado)

# 6. Corregir el error:
def duplicar(x):
    return x * 2

print(len(duplicar("hola")))

# === 7_8_ZeroDivisionError ===
# 7. Crear el error:
numeros = [10, 20, 0, 40]
promedio = sum(numeros) / len(numeros)
valor = promedio / numeros[2]
print(valor)

# 8. Corregir el error:
def calcular_coeficiente(a, b):
    return a / b

print(calcular_coeficiente(100, 2))

# === 9_10_IndexError ===
# 9. Crear el error:
palabras = ["uno", "dos", "tres"]
letra = palabras[1][5]
print(letra)

# 10. Corregir el error:
colores = ["rojo", "verde", "azul"]
print(colores[0])

# === 11-20: try-except ===

# 11. Corregir errores en try
try:
    x = int(input("Ingresá un número: "))
    resultado = 100 / x
    y = resultado + 10
    print("Programa correcto")
except ZeroDivisionError:
    print("No podés dividir por cero.")
except ValueError:
    print("Ingresaste un valor no numérico.")

# 12. Corregir errores en try
try:
    valor = int(input("Ingresá un valor: "))
    cuadrado = valor ** 2
    doble = cuadrado * 2
    print("Programa correcto")
except ValueError:
    print("Eso no es un número entero.")
else:
    print("Salió todo bien.")

# 13. Corregir errores en try
try:
    lista = [1, 2, 3, 4]
    print(lista.pop(2))
    elemento = lista[1]
    print("Programa correcto")
except Exception:
    print("Algo salió mal.")
finally:
    print("Fin del bloque.")

# 14. Corregir errores en try
try:
    datos = {"a": 1, "b": 2}
    total = datos.get("c", 0) + 10
    mensaje = str(datos["a"] + 5)
    print("Programa correcto")
except KeyError:
    print("Clave no encontrada.")
else:
    print("Todo OK con el diccionario.")

# 15. Corregir errores en try
try:
    texto = "5"
    numero = 3
    resultado = int(texto) - numero
    redondeo = round(resultado)
    print("Programa correcto")
except TypeError:
    print("No se puede operar str con int.")
finally:
    print("Bloque finalizado.")

# 16. Completar excepts específicos
try:
    a = int(input("A: "))
    b = int(input("B: "))
    c = [10, 20]
    resultado = c[a] / b
    palabra = resultado.upper()
    print("Programa correcto")
except ValueError:
    print("Error de valor")
except IndexError:
    print("Error de índice")
except ZeroDivisionError:
    print("División por cero")
except AttributeError:
    print("Error de atributo")

# 17. Completar excepts específicos
try:
    persona = {"nombre": "Ana", "edad": "veinte"}
    edad = int(persona["edad"])
    altura = persona.get("altura", 1.60)
    peso = persona.get("peso", 60)
    edad_total = edad + altura + peso
    print("Programa correcto")
except KeyError as e:
    print(f"Falta la clave {e}")
except ValueError:
    print("Edad inválida")
except TypeError:
    print("Tipos incompatibles al sumar")

# 18. Completar excepts específicos
try:
    datos = input("Ingresá tres números separados por coma: ")
    x_str, y_str, z_str = datos.split(",")
    x = int(x_str)
    y = int(y_str)
    z = int(z_str)
    print("El resultado es", 100 / (x - y))
    print("Programa correcto")
except ValueError:
    print("Error de valor")
except ZeroDivisionError:
    print("División por cero")

# 19. Completar excepts específicos
try:
    def funcion(z):
        return z.upper()
    valor = funcion("hola")
    print("Programa correcto")
except TypeError:
    print("Error en cantidad de argumentos")
except AttributeError:
    print("Objeto no tiene el método upper")

# 20. Completar excepts específicos
try:
    datos = ["5", "0"]
    numero = int(datos[0])
    divisor = int(datos[1])
    resultado = numero / divisor
    print("Programa correcto")
except IndexError:
    print("Índice fuera de rango")
except ValueError:
    print("Conversión inválida")
except ZeroDivisionError:
    print("División por cero")
