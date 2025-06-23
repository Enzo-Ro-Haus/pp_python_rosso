# Tu tarea es identificar y corregir sólo lo que está dentro de try
# de modo que al ejecutarlo aparezca en consola: Programa correcto.

try:
    lista = [1, 2, 3, 4]
    print(lista.pop(2)
    elemento = lista[10]
    print("Programa correcto")
except Exception:
    print("Algo salió mal.")
finally:
    print("Fin del bloque.")