import tkinter as tk
from tkinter import messagebox

def agregar_caracter(caracter):
    expresion_actual = entry_expresion.get()
    entry_expresion.delete(0, tk.END)
    entry_expresion.insert(tk.END, expresion_actual + str(caracter))

def calcular():
    expresion = entry_expresion.get()

    try:
        resultado = eval(expresion)
        resultado_label.config(text=f"Resultado: {resultado:.2f}")
    except Exception as e:
        messagebox.showerror("Error", f"Error en la expresión:\n{str(e)}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Profesional")

# Crear y colocar widgets con un diseño más atractivo
entry_expresion = tk.Entry(ventana, font=("Helvetica", 14), justify="right")
entry_expresion.grid(row=0, column=0, columnspan=4, padx=20, pady=(20, 0), ipady=10)

# Botones para números
for i in range(10):
    tk.Button(ventana, text=str(i), command=lambda i=i: agregar_caracter(i), font=("Helvetica", 12)).grid(row=1 + i // 3, column=i % 3, padx=5, pady=5)

# Botones para operadores
operadores = ['+', '-', '*', '/']
for i, operador in enumerate(operadores):
    tk.Button(ventana, text=operador, command=lambda operador=operador: agregar_caracter(operador), font=("Helvetica", 12)).grid(row=i + 1, column=3, padx=5, pady=5)

calcular_button = tk.Button(ventana, text="=", command=calcular, font=("Helvetica", 14), bg="#4CAF50", fg="white")
calcular_button.grid(row=4, column=0, columnspan=4, pady=10)

resultado_label = tk.Label(ventana, text="Resultado:", font=("Helvetica", 16, "bold"))
resultado_label.grid(row=5, column=0, columnspan=4, pady=(0, 20))

# Iniciar el bucle principal
ventana.mainloop()
