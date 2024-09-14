import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Función para agregar un registro a la tabla
def agregar_dato():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    edad = entrada_edad.get()

    if nombre and apellido and edad.isdigit():
        tabla_datos.insert("", tk.END, values=(nombre, apellido, edad))
        entrada_nombre.delete(0, tk.END)
        entrada_apellido.delete(0, tk.END)
        entrada_edad.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia",
                               "Por favor ingrese datos válidos. Asegúrese de que la edad sea un número.")


# Función para limpiar la tabla de datos
def limpiar_tabla():
    for item in tabla_datos.get_children():
        tabla_datos.delete(item)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Registro Creado por Fernanda")  # Título descriptivo
ventana.geometry("600x600")  # Tamaño de la ventana
ventana.config(bg="#f5b7b1")  # Color de fondo de la ventana

# Estilo para centrar el texto en la tabla
style = ttk.Style()
style.configure("Treeview.Heading", anchor="center", background="lightgray",
                foreground="black")  # Colores de los encabezados
style.configure("Treeview", rowheight=25, background="white", foreground="black")  # Fondo y texto de las filas

# Etiquetas y campos de texto
label_nombre = tk.Label(ventana, text="Ingrese su Nombre:", bg="lightblue", fg="black")
label_nombre.pack(pady=5)
entrada_nombre = tk.Entry(ventana, width=40)
entrada_nombre.pack()

label_apellido = tk.Label(ventana, text="Ingrese su Apellido:", bg="lightblue", fg="black")
label_apellido.pack(pady=5)
entrada_apellido = tk.Entry(ventana, width=40)
entrada_apellido.pack()

label_edad = tk.Label(ventana, text="Ingrese su Edad:", bg="lightblue", fg="black")
label_edad.pack(pady=5)
entrada_edad = tk.Entry(ventana, width=40)
entrada_edad.pack()

# Botón para agregar los datos
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato, bg="green", fg="white")
boton_agregar.pack(pady=10)

# Tabla (Treeview) para mostrar los datos
tabla_datos = ttk.Treeview(ventana, columns=("Nombre", "Apellido", "Edad"), show="headings", style="mystyle.Treeview")
tabla_datos.heading("Nombre", text="Nombre")
tabla_datos.heading("Apellido", text="Apellido")
tabla_datos.heading("Edad", text="Edad")

# Configurar el ancho de las columnas y centrar su contenido
tabla_datos.column("Nombre", anchor="center", width=100)
tabla_datos.column("Apellido", anchor="center", width=100)
tabla_datos.column("Edad", anchor="center", width=50)
tabla_datos.pack(pady=10)

# Colorear las filas de la tabla (alternando colores)
tabla_datos.tag_configure('oddrow', background="lightyellow")
tabla_datos.tag_configure('evenrow', background="lightgreen")


# Asignar colores alternos a las filas al insertar los datos
def agregar_dato():
    nombre = entrada_nombre.get()
    apellido = entrada_apellido.get()
    edad = entrada_edad.get()

    if nombre and apellido and edad.isdigit():
        if len(tabla_datos.get_children()) % 2 == 0:
            tabla_datos.insert("", tk.END, values=(nombre, apellido, edad), tags=('evenrow',))
        else:
            tabla_datos.insert("", tk.END, values=(nombre, apellido, edad), tags=('oddrow',))

        entrada_nombre.delete(0, tk.END)
        entrada_apellido.delete(0, tk.END)
        entrada_edad.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia",
                               "Por favor ingrese datos válidos. Asegúrese de que la edad sea un número.")


# Botón para limpiar la tabla
boton_limpiar = tk.Button(ventana, text="Limpiar",
                          command=limpiar_tabla,
                          bg="red",
                          fg="white")
boton_limpiar.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()