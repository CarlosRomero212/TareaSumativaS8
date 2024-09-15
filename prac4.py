import tkinter as tk

def leer_datos_mascotas():
    def obtener_datos():
        mascota1 = entry_mascota1.get()
        mascota2 = entry_mascota2.get()
        mascota3 = entry_mascota3.get()
        print(f"Mascota 1: {mascota1}, Mascota 2: {mascota2}, Mascota 3: {mascota3}")
        ventana.destroy()

    ventana = tk.Tk()
    ventana.title("Datos de Mascotas")
    ventana.geometry("300x300")

    label_mascota1 = tk.Label(ventana, text="Ingrese los datos de la Mascota 1:")
    label_mascota1.pack()
    entry_mascota1 = tk.Entry(ventana)
    entry_mascota1.pack()

    label_mascota2 = tk.Label(ventana, text="Ingrese los datos de la Mascota 2:")
    label_mascota2.pack()
    entry_mascota2 = tk.Entry(ventana)
    entry_mascota2.pack()

    label_mascota3 = tk.Label(ventana, text="Ingrese los datos de la Mascota 3:")
    label_mascota3.pack()
    entry_mascota3 = tk.Entry(ventana)
    entry_mascota3.pack()

    boton = tk.Button(ventana, text="Aceptar", command=obtener_datos)
    boton.pack()

    ventana.mainloop()

leer_datos_mascotas()