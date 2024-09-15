import tkinter as tk

def leer_datos_persona():
    def obtener_datos():
        datos = [entry.get() for entry in entradas]
        print(f"Datos personales: {datos}")
        ventana.destroy()

    ventana = tk.Tk()
    ventana.title("Datos de una Persona")
    ventana.geometry("400x500")

    etiquetas = [
        "Nombre", "Apellido", "Edad", "Género", "Dirección", 
        "Teléfono", "Email", "Ocupación", "Nacionalidad", "Estado civil"
    ]

    entradas = []
    for etiqueta in etiquetas:
        label = tk.Label(ventana, text=f"Ingrese {etiqueta}:")
        label.pack()
        entry = tk.Entry(ventana)
        entry.pack()
        entradas.append(entry)

    boton = tk.Button(ventana, text="Aceptar", command=obtener_datos)
    boton.pack()

    ventana.mainloop()

leer_datos_persona()