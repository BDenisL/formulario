import tkinter as tk
from tkinter import ttk
from Database import tabla_proveedor


class Proveedor(tk.Toplevel):
    def __init__(self, _window):
        super().__init__(_window)
        self.title("Ventana Proveedor")
        self.geometry("1200x600")

        self.connect = tabla_proveedor()
        self.cursor = self.connect.cursor(buffered=True)
        self.result = 0

        self.cursor.execute("SHOW TABLES")

        for i in self.cursor:
            print(i)

        self.id = 0
        self.init_buttons()

        tk.Label(self, text="").grid(row=0, column=0, pady=15)
        tk.Label(self, text="Nombre").grid(row=1, column=0)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1)

        tk.Label(self, text="Documento").grid(row=2, column=0)
        self.document_entry = tk.Entry(self)
        self.document_entry.grid(row=2, column=1)

        tk.Label(self, text="Telefono").grid(row=3, column=0)
        self.phone_entry = tk.Entry(self)
        self.phone_entry.grid(row=3, column=1)

        tk.Label(self, text="Email").grid(row=4, column=0)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=4, column=1)

        tk.Label(self, text="Servicios").grid(row=5, column=0)
        self.services_entry = tk.Entry(self)
        self.services_entry.grid(row=5, column=1)

        tk.Label(self, text="Direccion").grid(row=6, column=0)
        self.address_entry = tk.Entry(self)
        self.address_entry.grid(row=6, column=1)

        tk.Label(self, text="Ciudad").grid(row=7, column=0)
        self.city_entry = tk.Entry(self)
        self.city_entry.grid(row=7, column=1)

        tk.Label(self, text="Provincia").grid(row=8, column=0)
        self.provin_entry = tk.Entry(self)
        self.provin_entry.grid(row=8, column=1)

        tk.Label(self, text="Codigo Postal").grid(row=9, column=0)
        self.postalcode_entry = tk.Entry(self)
        self.postalcode_entry.grid(row=9, column=1)

        columnas = (
            "ID",
            "Nombre",
            "Documento",
            "Telefono",
            "Email",
            "Servicios",
            "Direccion",
            "Ciudad",
            "Provicia",
            "Codigo Postal"
        )

        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=10)

        for i in columnas:
            self.tabla.heading(i, text=i)
            self.tabla.column(i, width=80)

        self.tabla.grid(row=10, column=0, columnspan=5, pady=25)

    def init_buttons(self):
        button_save = tk.Button(self, text="Guardar", command=self.save_data, width=12)
        button_save.grid(row=2, column=2)

        button_select = tk.Button(self, text="Seleccionar", command=self.select_data, width=12)
        button_select.grid(row=4, column=2)

        button_modify = tk.Button(self, text="Modificar", command=self.modify_data, width=12)
        button_modify.grid(row=6, column=2)

        button_delete = tk.Button(self, text="Eliminar", command=self.delete_data, width=12)
        button_delete.grid(row=8, column=2)

        button_close = tk.Button(self, text="Cerrar", command=self.destroy, width=12)
        button_close.grid(row=10, column=4, columnspan=4)

    def save_data(self):
        self.id += 1
        name = self.name_entry.get()
        document = self.document_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        services = self.services_entry.get()
        address = self.address_entry.get()
        city = self.city_entry.get()
        prov = self.provin_entry.get()
        postal = self.postalcode_entry.get()

        self.tabla.insert("", "end", values=(
            self.id,
            name,
            document,
            phone,
            email,
            services,
            address,
            city,
            prov,
            postal
        ))

        sql = """INSERT INTO proveedor(
        nombre, documento, telefono, email, 
        servicios, direccion, ciudad, 
        provincia, codigo_postal)
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        datos = (
            name,
            document,
            phone,
            email,
            services,
            address,
            city,
            prov,
            postal
        )

        self.cursor.execute(sql, datos)
        self.connect.commit()

        if self.cursor.rowcount > 0:
            print("Datos guardados con exito")
        else:
            print("Error")

    def select_data(self):
        self.id -= 1
        self.name_entry.delete(0, tk.END)
        self.document_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.services_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.city_entry.delete(0, tk.END)
        self.provin_entry.delete(0, tk.END)
        self.postalcode_entry.delete(0, tk.END)

        selected = self.tabla.focus()
        value = self.tabla.item(selected, "values")

        sql = """SELECT id FROM proveedor WHERE 
              nombre=%s AND documento=%s AND telefono=%s AND 
              email=%s AND servicios=%s AND direccion=%s
              AND ciudad=%s AND provincia=%s AND codigo_postal=%s"""

        datt = (
            value[1],
            value[2],
            value[3],
            value[4],
            value[5],
            value[6],
            value[7],
            value[8],
            value[9],
        )

        self.cursor.execute(sql, datt)
        self.connect.commit()
        rows = self.cursor.fetchone()

        if rows:
            self.result = rows[0]

        print(self.result)

        self.name_entry.insert(0, value[1])
        self.document_entry.insert(0, value[2])
        self.phone_entry.insert(0, value[3])
        self.email_entry.insert(0, value[4])
        self.services_entry.insert(0, value[5])
        self.address_entry.insert(0, value[6])
        self.city_entry.insert(0, value[7])
        self.provin_entry.insert(0, value[8])
        self.postalcode_entry.insert(0, value[9])

    def modify_data(self):
        name = self.name_entry.get()
        document = self.document_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        services = self.services_entry.get()
        address = self.address_entry.get()
        city = self.city_entry.get()
        prov = self.provin_entry.get()
        postal = self.postalcode_entry.get()

        selected = self.tabla.focus()

        self.tabla.item(selected, text="", values=(
            self.name_entry.get(),
            self.document_entry.get(),
            self.phone_entry.get(),
            self.email_entry.get(),
            self.services_entry.get(),
            self.address_entry.get(),
            self.city_entry.get(),
            self.provin_entry.get(),
            self.postalcode_entry.get()
        ))

        sql = """UPDATE proveedor SET 
              nombre=%s,
              documento=%s,
              telefono=%s,
              email=%s,
              servicios=%s,
              direccion=%s,
              ciudad=%s,
              provincia=%s,
              codigo_postal=%s"""

        datos = (
            name,
            document,
            phone,
            email,
            services,
            address,
            city,
            prov,
            postal
        )

        self.cursor.execute(sql, datos)
        self.connect.commit()

        if self.cursor.rowcount > 0:
            print("Datos modificados con exito")
        else:
            print("Error al modificar datos")

        self.name_entry.delete(0, tk.END)
        self.document_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.services_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.city_entry.delete(0, tk.END)
        self.provin_entry.delete(0, tk.END)
        self.postalcode_entry.delete(0, tk.END)

    def delete_data(self):
        selected = self.tabla.selection()

        for i in selected:
            self.tabla.delete(i)

        sql = """DELETE FROM proveedor WHERE id=%s"""

        self.cursor.execute(sql, (self.result,))
        self.connect.commit()

        if self.cursor.rowcount > 0:
            print("Datos Eliminados")
        else:
            print("Error al eliminar datos")