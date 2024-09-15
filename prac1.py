
import tkinter as tk

def mostrar_datos():
    ventana = tk.Tk()
    ventana.title("Datos Personales")
    ventana.geometry("300x200")

    nombre = "Carlos Arnoldo"
    edad = "20 años"

    # Crear un frame centrado para los datos
    frame = tk.Frame(ventana)
    frame.pack(expand=True)

    label_nombre = tk.Label(frame, text=nombre, font=("Arial", 16))
    label_nombre.pack()

    label_edad = tk.Label(frame, text=edad, font=("Arial", 16))
    label_edad.pack()

    ventana.mainloop()

mostrar_datos()