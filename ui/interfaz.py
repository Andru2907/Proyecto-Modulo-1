import tkinter as tk
from tkinter import ttk
from api.consulta import importando


class Interfaz:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('800x600')

        # Primer campo de entrada
        self.label1 = tk.Label(text="Ingrese el nombre del departamento:")
        self.label1.pack()
        self.entry1 = tk.Entry()
        self.entry1.pack()

        # Segundo campo de entrada
        self.label2 = tk.Label(text="Ingrese el numero de datos que quiere ver:")
        self.label2.pack()
        self.entry2 = tk.Entry()
        self.entry2.pack()

        # Botón para enviar los datos
        enviar_btn = tk.Button(self.root, text="Enviar", command=self.enviar_datos)
        enviar_btn.pack()

        # Creando un Treeview para la tabla
        self.table = ttk.Treeview(self.root)
        self.table.pack(fill="both", expand=True)

        # Configurar encabezados de columnas
        self.table.column("#0", width=0, stretch=tk.NO)

    def enviar_datos(self):
        nom_dep = self.entry1.get()
        nom_dep = nom_dep.upper()#para covertir el texto en mayusculas
        limit_reg = int(self.entry2.get())
        resultado = importando(limit_reg, nom_dep)

        # Obtener las llaves del diccionario y crear columnas en la tabla
        llaves = ["ciudad_municipio_nom", "departamento_nom", "edad", "fuente_tipo_contagio", "estado", "pais_origen"]
        self.table["columns"] = llaves
        
        # Configurar encabezados de columnas
        self.table.column("#0", width=0, stretch=tk.NO)
        self.table.column("ciudad_municipio_nom", anchor=tk.CENTER, width=200, stretch=tk.NO)
        self.table.column("departamento_nom", anchor=tk.CENTER, width=200, stretch=tk.NO)
        self.table.column("edad", anchor=tk.CENTER, width=100, stretch=tk.NO)
        self.table.column("fuente_tipo_contagio", anchor=tk.CENTER, width=150, stretch=tk.NO)
        self.table.column("estado", anchor=tk.CENTER, width=100, stretch=tk.NO)
        self.table.column("pais_origen", anchor=tk.CENTER, width=100, stretch=tk.NO)

        self.table.heading("ciudad_municipio_nom", text="Ciudad de ubicación")
        self.table.heading("departamento_nom", text="Departamento")
        self.table.heading("edad", text="Edad")
        self.table.heading("fuente_tipo_contagio", text="Tipo")
        self.table.heading("estado", text="Estado")
        self.table.heading("pais_origen", text="Pais Origen")
        # Eliminar filas existentes en la tabla
        for row in self.table.get_children():
            self.table.delete(row)

        # Insertar datos en la tabla
        for index, row in resultado.iterrows():
            ciudad = row["ciudad_municipio_nom"]
            depto = row["departamento_nom"]
            edad = row["edad"]
            tipo = row["fuente_tipo_contagio"]
            estado = row["estado"]
            pais_origen = ("Sin información")
            self.table.insert(parent="", index=index, text="", values=(ciudad, depto, edad, tipo, estado, pais_origen))
