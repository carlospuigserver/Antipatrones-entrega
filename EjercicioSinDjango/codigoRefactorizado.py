def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("No se puede dividir entre cero.")
        return None

def calcular(operacion, num1, num2):
    if operacion == 'suma':
        return suma(num1, num2)
    elif operacion == 'resta':
        return resta(num1, num2)
    elif operacion == 'multiplicacion':
        return multiplicacion(num1, num2)
    elif operacion == 'division':
        return division(num1, num2)
    else:
        print("Operación no soportada.")
        return None

# Obtener entrada del usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación (suma, resta, multiplicacion, division): ")

# Calcular y mostrar el resultado
resultado = calcular(operacion, num1, num2)
if resultado is not None:
    print(f"Resultado: {resultado}")
