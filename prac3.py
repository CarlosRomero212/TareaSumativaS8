import tkinter as tk

def leer_cedula_nombre():
    def obtener_datos():
        cedula = entry_cedula.get()
        nombre = entry_nombre.get()
        print(f"Cédula: {cedula}, Nombre: {nombre}")
        ventana.destroy()

    ventana = tk.Tk()
    ventana.title("Cédula y Nombre")
    ventana.geometry("300x200")

    label_cedula = tk.Label(ventana, text="Ingrese su número de cédula:")
    label_cedula.pack()

    entry_cedula = tk.Entry(ventana)
    entry_cedula.pack()

    label_nombre = tk.Label(ventana, text="Ingrese su nombre completo:")
    label_nombre.pack()

    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()

    boton = tk.Button(ventana, text="Aceptar", command=obtener_datos)
    boton.pack()

    ventana.mainloop()

leer_cedula_nombre()