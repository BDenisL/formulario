import tkinter as tk
from tkinter import ttk

# num. de serie
# nombre del prod
# precio unitario
# cantidad
# descuento
# precio
# Lograr hacer descuento general
#
# OPERACIONES A TENER EN CUENTA
# POR PRODUCTO =
# total_prod = preciou * cant - (precio * cant * desc / 100)
#
# TOTAL =
# subtotal = subtotal + total_prod
#
# function factura():
# restotal = subtotal * (desc_general / 100)

class Facturacion(tk.Toplevel):
    def __init__(self, window):
        super().__init__(window)
        self.title("Ventana de Factura")
        self.geometry("1200x600")

        self.total_prod = 0
        self.subtotal_ = 0
        self.total = 0

        self.crud_buttons()

        tk.Label(self, text="").grid(row=1, column=0, pady=10)
        tk.Label(self, text="Nro. Serie").grid(row=2, column=0, pady=5)
        self.num_entry = tk.Entry(self)
        self.num_entry.grid(row=2, column=1)

        tk.Label(self, text="Nombre Producto").grid(row=3, column=0, pady=5)
        self.prodname_entry = tk.Entry(self)
        self.prodname_entry.grid(row=3, column=1)

        tk.Label(self, text="Precio Unitario").grid(row=4, column=0, pady=5)
        self.uprecio_entry = tk.Entry(self)
        self.uprecio_entry.grid(row=4, column=1)

        tk.Label(self, text="Cantidad").grid(row=5, column=0, pady=5)
        self.prodcant_entry = tk.Entry(self)
        self.prodcant_entry.grid(row=5, column=1)

        tk.Label(self, text="Descuento").grid(row=6, column=0, pady=5)
        self.descuento_entry = tk.Entry(self)
        self.descuento_entry.grid(row=6, column=1)

        tk.Label(self, text="Subtotal").grid(row=7, column=3)
        self.subtotal = tk.Label(self, text="Resultado")
        self.subtotal.grid(row=7, column=4)

        tk.Label(self, text="Descuento").grid(row=8, column=3)
        self.descuento_general_entry = tk.Entry(self)
        self.descuento_general_entry.grid(row=8, column=4)

        tk.Label(self, text="Total").grid(row=10, column=3)
        self.restotal = tk.Label(self, text="Resultado")
        self.restotal.grid(row=10, column=4)

        columnas = (
            "Nro. de Serie",
            "Nombre Producto",
            "Precio Unit.",
            "Cantidad",
            "Descuento",
            "Total"
        )

        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=10)

        for i in columnas:
            self.tabla.heading(i, text=i)
            self.tabla.column(i, width=100)

        self.tabla.grid(row=7, column=0, columnspan=4, rowspan=10, pady=15)

    def crud_buttons(self):
        button_save = tk.Button(self, text="Guardar", command=self.save_data, width=12)
        button_save.grid(row=2, column=2)

        button_select = tk.Button(self, text="Seleccionar", command=self.select_data, width=12)
        button_select.grid(row=3, column=2)

        button_modify = tk.Button(self, text="Modificar", command=self.modify_data, width=12)
        button_modify.grid(row=4, column=2)

        button_delete = tk.Button(self, text="Eliminar", command=self.delete_data, width=12)
        button_delete.grid(row=5, column=2)

        button_gdesc  = tk.Button(self, text="Factura", command=self.desc_general, width=12)
        button_gdesc.grid(row=9, column=4)

        button_close = tk.Button(self, text="Cerrar", command=self.destroy, width=12)
        button_close.grid(row=11, column=3, columnspan=2, pady=15)

    def save_data(self):
        num_serie = self.num_entry.get()
        name = self.prodname_entry.get()
        precio_base = self.uprecio_entry.get()
        cant = self.prodcant_entry.get()
        desc = self.descuento_entry.get()
        total_prod = self.total_producto()

        self.tabla.insert("", "end", values=(
            num_serie,
            name,
            precio_base,
            cant,
            desc,
            total_prod
        ))

        self.subtotal.config(text=f"{self.subtotal_}")

    def select_data(self):
        self.num_entry.delete(0, tk.END)
        self.prodname_entry.delete(0, tk.END)
        self.uprecio_entry.delete(0, tk.END)
        self.prodcant_entry.delete(0, tk.END)
        self.descuento_entry.delete(0, tk.END)

        selected = self.tabla.focus()
        values = self.tabla.item(selected, "values")


        self.num_entry.insert(0, values[0])
        self.prodname_entry.insert(0, values[1])
        self.uprecio_entry.insert(0, values[2])
        self.prodcant_entry.insert(0, values[3])
        self.descuento_entry.insert(0, values[4])

    def modify_data(self):
        selected_row = self.tabla.focus()

        self.restar(self.total_prod)
        self.total_producto()

        self.tabla.item(selected_row, text="", values=(
            self.num_entry.get(),
            self.prodname_entry.get(),
            self.uprecio_entry.get(),
            self.prodcant_entry.get(),
            self.descuento_entry.get(),
            self.total_prod
        ))

        self.num_entry.delete(0, tk.END)
        self.prodname_entry.delete(0, tk.END)
        self.uprecio_entry.delete(0, tk.END)
        self.prodcant_entry.delete(0, tk.END)
        self.descuento_entry.delete(0, tk.END)

        self.subtotal.config(text=f"{self.subtotal_}")

    def delete_data(self):
        selected = self.tabla.selection()
        self.restar(self.total_prod)

        for i in selected:
            self.tabla.delete(i)

        self.subtotal.config(text=f"{self.subtotal_}")

    def total_producto(self):
        self.total_prod = 0
        precio = float(self.uprecio_entry.get())
        cant = int(self.prodcant_entry.get())
        desc = float(self.descuento_entry.get())

        self.total_prod = precio * cant - (precio * cant * desc / 100)

        self.suma(self.total_prod)

        return self.total_prod

    def suma(self, total):
        self.subtotal_ = self.subtotal_ + total


        return self.subtotal_

    def restar(self, precio):
        self.subtotal_ = self.subtotal_ - precio

        return self.subtotal_

    def desc_general(self):
        self.total = 0
        desc_gen = int(self.descuento_general_entry.get())

        self.total = self.subtotal_ - (self.subtotal_ * desc_gen / 100)

        self.restotal.config(text=f"{self.total}")