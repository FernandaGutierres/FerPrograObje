#Implementamos nuestras librerias necesarias para programar

import  tkinter as tk
from os.path import commonpath
from struct import pack_into
from tkinter import ttk, messagebox, Frame

from pyexpat.errors import messages
from select import select
from tkcalendar import DateEntry


#Creamos una clase para armar nuestra agenda Fernandita


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenta de Fernanda ")
        self.root.geometry("600x600")#El 600 es ancho y el 600 es largo
        self.root.config(bg="yellow" )#Codigo permite poner color de la interfaz grafica

        #
        frame_entrada=tk.Frame(self.root)
        frame_entrada.pack(padx=15, pady=15)

        #Agregamos a nuestras etiquetas Fecha

        tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(frame_entrada, width= 10, background="purple", foreground="rose", borderwidth=5)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        # Agregamos a nuestras etiquetas Hora

        tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.time_entry= tk.Entry(frame_entrada)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        # Agregamos a nuestras etiquetas Descripcion

        tk.Label(frame_entrada, text="Descripcion:").grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(frame_entrada)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)



        #Frame para los botones de control
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(padx=15, pady=15)

        #Crear nuestro boton para agregar la lista
        tk.Button(frame_botones,text="agragar",command=self.agregar_evento).pack(side=tk.LEFT, padx=10, pady=10)

        #Creamos nuestro boton para eliminar la lista
        tk.Button(frame_botones,text="eliminar",command=self.eliminar_evento).pack(side=tk.LEFT, padx=10, pady=10)

        #Creamos nuestro boton para salir dde la lista
        tk.Button(frame_botones,text="salir", command=self.root.quit).pack(side=tk.LEFT, padx=10, pady=10)

        # Frame para la lista de eventos
        frame_lista = tk.Frame(self.root)
        frame_lista.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Lista de eventos con Treeview
        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")

        # Configuración de las columnas
        self.tree.column("Fecha", anchor="center", width=100)
        self.tree.column("Hora", anchor="center", width=100)
        self.tree.column("Descripción", anchor="center", width=200)

        # Encabezados de las columnas
        self.tree.heading("Fecha", text="Fecha", anchor="center")
        self.tree.heading("Hora", text="Hora", anchor="center")
        self.tree.heading("Descripción", text="Descripción", anchor="center")

        # Empaquetar Treeview
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Método para agregar evento

    def agregar_evento(self):
        fecha = self.date_entry.get()
        hora = self.time_entry.get()
        descripcion = self.desc_entry.get()

        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Alerta del sistema", "Rellena los campos")
            return

        # Insertar en la tabla
        self.tree.insert("", "end", values=(fecha, hora, descripcion))

        # Limpiar campos de entrada
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

        # Método para eliminar evento

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if seleccion:
            confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar el dato?")
            if confirmar:
                self.tree.delete(seleccion)
        else:
            messagebox.showwarning("Mensaje de alerta", "Selecciona un dato para eliminar")


root = tk.Tk()
app = AgendaApp(root)
root.mainloop()