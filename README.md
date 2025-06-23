## 📚 Descripción General

Este README contiene las soluciones comentadas para los ejercicios de manejo de errores en Python. Cada sección aborda un tipo de excepción o constructo `try-except`, con ejemplos de código que **crean** y **corrigen** errores.

---

## 🛠️ Índice de Ejercicios

1. **SyntaxError**
2. **NameError**
3. **TypeError**
4. **ZeroDivisionError**
5. **IndexError**
6. **Bloques `try-except`** (ejercicios 11–20)

---

## 1. SyntaxError 🚨

* **Creación del error**

  ```python
  # def saludar()        # Falta dos puntos al definir la función
  #     print("Hola")
  ```

* **Corrección**

  ```python
  if True:
      print("¡Funciona!")  # ¡Éxito sin errores de sintaxis! ✅
  ```

---

## 2. NameError 🔍

* **Creación del error**

  ```python
  # print(mensaje)      # 'mensaje' no está definido aún
  ```

* **Corrección**

  ```python
  mensaje = "¡Hola, programador!"
  print(mensaje)       # Ahora sí funciona ✔️
  ```

---

## 3. TypeError 🤔

* **Creación del error**

  ```python
  # resultado = numero + "texto"   # No puedes sumar int y str
  ```

* **Corrección**

  ```python
  def duplicar(x):
      return x * 2

  print(len(duplicar("hola")))    # Convierte todo en cadena, ¡sin problemas! 🎉
  ```

---

## 4. ZeroDivisionError ➗

* **Creación del error**

  ```python
  # valor = 100 / 0   # División por cero → ¡Crash! 💥
  ```

* **Corrección**

  ```python
  def calcular_coeficiente(a, b):
      return a / b   # Asegúrate de que b ≠ 0

  print(calcular_coeficiente(100, 2))  # Salida: 50.0 👍
  ```

---

## 5. IndexError 📏

* **Creación del error**

  ```python
  palabras = ["uno", "dos", "tres"]
  # letra = palabras[1][5]   # Índice fuera de rango
  ```

* **Corrección**

  ```python
  colores = ["rojo", "verde", "azul"]
  print(colores[0])          # "rojo" — índice válido ✔️
  ```

---

## 6. Try–Except 😎

Para los ejercicios **11–20**, hemos usado bloques `try-except` con excepciones específicas:

```python
try:
    # … tu lógica aquí …
    print("Programa correcto 🎯")
except ZeroDivisionError:
    print("No podés dividir por cero. 🛑")
except ValueError:
    print("Ingresaste un valor no numérico. ❌")
except IndexError:
    print("Índice fuera de rango. 📋")
except KeyError as e:
    print(f"Falta la clave {e}. 🔑")
except AttributeError:
    print("Objeto sin ese método. 📛")
finally:
    print("Fin del bloque. 🏁")
```

Cada ejercicio ajusta estas excepciones al contexto del problema: conversiones, accesos a listas o diccionarios, división, etc.

---

¡Y eso es todo! 🌟 Gracias por revisar estos ejemplos y ¡feliz codificación! 🚀

