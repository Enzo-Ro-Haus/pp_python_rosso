# Tu tarea es identificar y corregir sólo lo que está dentro de try
# de modo que al ejecutarlo aparezca en consola: Programa correcto.

try:
    valor = int(input("Ingresá un valor: "))
    cuadrado = valoor ** 2
    doble = cuadrado.copy()
    print("Programa correcto")
except ValueError:
    print("Eso no es un número entero.")
else:
    print("Salió todo bien.")