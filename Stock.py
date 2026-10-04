import tkinter as tk
from time import sleep
from tkinter import ttk
from Database import tabla_stock


class Stock(tk.Toplevel):
    def __init__(self, _window):
        super().__init__(_window)
        self.title("Ventana de Stock")
        self.geometry("1200x600")

        self.connect = tabla_stock()
        self.cursor = self.connect.cursor(buffered=True)
        self.result = 0

        self.cursor.execute("SHOW TABLES")

        for i in self.cursor:
            print(i)

        self.valor_inventario = 0
        self.crud_buttons()

        ####################- LABELS & ENTRY'S -########################
        tk.Label(self, text="").grid(row=1, column=0, pady=15)
        tk.Label(self, text="id").grid(row=2, column=0, padx=5)
        self.id_entry = tk.Entry(self)
        self.id_entry.grid(row=2, column=1)

        tk.Label(self, text="Nombre").grid(row=3, column=0, padx=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=3, column=1)

        tk.Label(self, text="Fabricante").grid(row=4, column=0, padx=5)
        self.fab_entry = tk.Entry(self)
        self.fab_entry.grid(row=4, column=1)

        tk.Label(self, text="Cantidad").grid(row=5, column=0, padx=5)
        self.cant_entry = tk.Entry(self)
        self.cant_entry.grid(row=5, column=1)

        tk.Label(self, text="Costo").grid(row=6, column=0, padx=5)
        self.cost_entry = tk.Entry(self)
        self.cost_entry.grid(row=6, column=1)

        ####################- LABELS & ENTRY'S -########################
        columnas = (
            "ID",
            "Nombre",
            "Fabricante",
            "Cantidad",
            "Costo",
            "Valor de Inventario"
        )

        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=10)

        for i in columnas:
            self.tabla.heading(i, text=i)
            self.tabla.column(i, width=120)

        self.tabla.grid(row=7, column=0, columnspan=5,pady=15)

    def crud_buttons(self):
        button_save = tk.Button(self, text="Guardar", command=self.save_data, width=12)
        button_save.grid(row=2, column=2)

        button_select = tk.Button(self, text="Seleccionar", command=self.select_data, width=12)
        button_select.grid(row=3, column=2)

        button_modify = tk.Button(self, text="Modificar", command=self.modify_data, width=12)
        button_modify.grid(row=4, column=2)

        button_delete = tk.Button(self, text="Eliminar", command=self.delete_data, width=12)
        button_delete.grid(row=5, column=2)

        button_close = tk.Button(self, text="Cerrar", command=self.destroy, width=12)
        button_close.grid(row=7, column=4, columnspan=2)

    def save_data(self):
        ids = self.id_entry.get()
        name = self.name_entry.get()
        fab = self.fab_entry.get()
        cant = self.cant_entry.get()
        cost = self.cost_entry.get()
        valor_inventario = self.calcular()
        ##########

        self.tabla.insert("", "end", values=(
            ids,
            name,
            fab,
            cant,
            cost,
            valor_inventario
        ))

        sql = """INSERT INTO stock(
        id_02, nombre, fabricante, cantidad, costo, valor_invent)
              VALUES(%s, %s, %s, %s, %s, %s)"""

        datos = (
            ids,
            name,
            fab,
            cant,
            cost,
            valor_inventario
        )

        self.cursor.execute(sql, datos)
        self.connect.commit()

        if self.cursor.rowcount > 0:
            print("Datos guardados con exito")
        else:
            print("Error al guardar datos")

    def select_data(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.fab_entry.delete(0, tk.END)
        self.cant_entry.delete(0, tk.END)
        self.cost_entry.delete(0, tk.END)

        selected = self.tabla.focus()
        values = self.tabla.item(selected, "values")

        sql = """SELECT id FROM stock WHERE
              id_02=%s AND nombre=%s AND fabricante=%s AND
              cantidad=%s AND costo=%s"""

        datos = (
            values[0],
            values[1],
            values[2],
            values[3],
            values[4],
        )

        self.cursor.execute(sql, datos)
        self.connect.commit()
        row = self.cursor.fetchone()

        if row:
            self.result = row[0]

        print(self.result)

        self.id_entry.insert(0, values[0])
        self.name_entry.insert(0, values[1])
        self.fab_entry.insert(0, values[2])
        self.cant_entry.insert(0, values[3])
        self.cost_entry.insert(0, values[4])

    def modify_data(self):
        ids = self.id_entry.get()
        name = self.name_entry.get()
        fab = self.fab_entry.get()
        cant = self.cant_entry.get()
        cost = self.cost_entry.get()
        valor_inventario = self.calcular()

        selected = self.tabla.focus()

        self.tabla.item(selected, text="", values=(
            self.id_entry.get(),
            self.name_entry.get(),
            self.fab_entry.get(),
            self.cant_entry.get(),
            self.cost_entry.get(),
            self.calcular()
        ))

        sql = """UPDATE stock SET 
              id_02=%s,
              nombre=%s,
              fabricante=%s,
              cantidad=%s,
              costo=%s,
              valor_invent=%s
              WHERE id=%s"""

        datos = (
            ids,
            name,
            fab,
            cant,
            cost,
            valor_inventario,
            self.result
        )

        self.cursor.execute(sql, datos)
        self.connect.commit()

        if self.cursor.rowcount > 0:
            print("Datos actualizados")
        else:
            print("Error al actualizar datos")

        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.fab_entry.delete(0, tk.END)
        self.cant_entry.delete(0, tk.END)
        self.cost_entry.delete(0, tk.END)

    def delete_data(self):
        selected = self.tabla.selection()

        for i in selected:
            self.tabla.delete(i)

        sql = """DELETE FROM stock WHERE id=%s"""

        self.cursor.execute(sql, (self.result,))
        self.connect.commit()

        if self.cursor.rowcount > 0:
            print("Datos eliminados")
        else:
            print("Error al eliminar datos")

    def calcular(self):
        costo = int(self.cost_entry.get())
        cant = int(self.cant_entry.get())

        valor_inventario = costo * cant

        return valor_inventario
