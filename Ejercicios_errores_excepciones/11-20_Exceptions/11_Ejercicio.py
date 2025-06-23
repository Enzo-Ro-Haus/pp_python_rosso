# Tu tarea es identificar y corregir sólo lo que está dentro de try
# de modo que al ejecutarlo aparezca en consola: Programa correcto.

try:
    x = input("Ingresá un número: ")
    resultado = 100 / x
    y = resultado + z
    print("Programa correcto")
except ZeroDivisionError:
    print("No podés dividir por cero.")