# Tu tarea es identificar y corregir sólo lo que está dentro de try
# de modo que al ejecutarlo aparezca en consola: Programa correcto.

try:
    datos = {"a": "uno", "b": 2}
    total = datos["c"] + 10
    mensaje = datos["a"] + 5
    print("Programa correcto")
except KeyError:
    print("Clave no encontrada.")
else:
    print("Todo OK con el diccionario.")