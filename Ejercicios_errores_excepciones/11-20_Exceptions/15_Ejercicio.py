# Tu tarea es identificar y corregir sólo lo que está dentro de try
# de modo que al ejecutarlo aparezca en consola: Programa correcto.

try:
    texto = "5"
    numero = 3
    resultado = texto - numero
    redondeo = roundd(resultado)
    print("Programa correcto")
except TypeError:
    print("No se puede operar str con int.")
finally:
    print("Bloque finalizado.")