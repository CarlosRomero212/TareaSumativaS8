import tkinter as tk

def leer_clave():
    def obtener_clave():
        clave = entry.get()
        print(f"Clave ingresada: {clave}")
        ventana.destroy()

    ventana = tk.Tk()
    ventana.title("Clave Secreta")
    ventana.geometry("300x200")

    label = tk.Label(ventana, text="Ingrese su clave:")
    label.pack()

    entry = tk.Entry(ventana, show="*")  # Los caracteres ingresados no se mostrarán
    entry.pack()

    boton = tk.Button(ventana, text="Aceptar", command=obtener_clave)
    boton.pack()

    ventana.mainloop()

leer_clave()
