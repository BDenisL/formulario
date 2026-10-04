import tkinter as tk
from tkinter import ttk
from Database import tabla_cliente


class Cliente(tk.Toplevel):
    def __init__(self, _window):
        super().__init__(_window)
        self.title("Ventana Cliente")
        self.geometry("1200x600")

        self.cnnet = tabla_cliente()
        self.cursor = self.cnnet.cursor(buffered=True)
        self.result = 0

        self.cursor.execute("SHOW TABLES")

        for i in self.cursor:
            print(i)


        self.crud_buttons()
            ################ LABELS & ENTRY'S ################
        tk.Label(self, text="Nombre").grid(row=1, column=0, pady=5, padx=25)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1, pady=5)

        tk.Label(self, text="Apellido").grid(row=2, column=0, pady=5, padx=25)
        self.sur_entry = tk.Entry(self)
        self.sur_entry.grid(row=2, column=1, pady=5)

        tk.Label(self, text="DNI").grid(row=3, column=0, padx=25, pady=5)
        self.dni_entry = tk.Entry(self)
        self.dni_entry.grid(row=3, column=1, pady=5)

        tk.Label(self, text="Edad").grid(row=4, column=0, padx=25, pady=5)
        self.age_entry = tk.Entry(self)
        self.age_entry.grid(row=4, column=1, pady=5)

        tk.Label(self, text="Telefono").grid(row=5, column=0, pady=5, padx=25)
        self.phone_entry = tk.Entry(self)
        self.phone_entry.grid(row=5, column=1, pady=5)

        tk.Label(self, text="EMAIL").grid(row=6, column=0, pady=5, padx=25)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=6, column=1, pady=5)

        tk.Label(self, text="Direccion").grid(row=7, column=0, pady=5, padx=25)
        self.address_entry = tk.Entry(self)
        self.address_entry.grid(row=7, column=1, pady=5)

        tk.Label(self, text="Ciudad").grid(row=8, column=0, pady=5, padx=25)
        self.city_entry = tk.Entry(self)
        self.city_entry.grid(row=8, column=1, pady=5)

        tk.Label(self, text="Provincia").grid(row=9, column=0, pady=5, padx=25)
        self.prov_entry = tk.Entry(self)
        self.prov_entry.grid(row=9, column=1, pady=5)

        tk.Label(self, text="Codigo Postal").grid(row=10, column=0, pady=5, padx=25)
        self.postal_entry = tk.Entry(self)
        self.postal_entry.grid(row=10, column=1, pady=5, padx=25)

        ################ TABLAS ################
        self.columnas = (
            "Nombre",
            "Apellido",
            "DNI",
            "Edad",
            "Telefono",
            "EMAIL",
            "Direccion",
            "Ciudad",
            "Provincia",
            "Codigo Postal"
        )

        self.tabla = ttk.Treeview(self, columns=self.columnas, show="headings", height=10)

        for i in self.columnas:
            self.tabla.heading(i, text=i)
            self.tabla.column(i, width=90)

        self.tabla.grid(row=11,
                   column=0,
                   columnspan=5,
                   pady=5,
                   padx=10
        )


    def crud_buttons(self):
        button_save = tk.Button(self, text="Guardar", command=self.guardar,width=10)
        button_save.grid(row=3, column=2)

        button_select = tk.Button(self, text="Seleccionar", command=self.select_record, width=10)
        button_select.grid(row=4, column=2)

        button_modify = tk.Button(self, text="Modificar", command=self.modify,width=10)
        button_modify.grid(row=5, column=2, pady=10)

        button_delete = tk.Button(self, text="Eliminar", command=self.delete,width=10)
        button_delete.grid(row=6, column=2)

        button_close = tk.Button(self, text="Cerrar", width=10, command=self.destroy)
        button_close.grid(row=11, column=4, pady=10)

    def guardar(self):
        name = self.name_entry.get()
        surname = self.sur_entry.get()
        dni = self.dni_entry.get()
        age = self.age_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        city = self.city_entry.get()
        prov = self.prov_entry.get()
        postal = self.postal_entry.get()

        self.tabla.insert("", "end", values=(
            name,
            surname,
            dni,
            age,
            phone,
            email,
            address,
            city,
            prov,
            postal
        ))

        sql = """INSERT INTO clientes(
        nombre, apellido, dni, edad, telefono,
        email, direccion, ciudad, provincia, codigo_postal)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        datos = (
            name,
            surname,
            dni,
            age,
            phone,
            email,
            address,
            city,
            prov,
            postal
        )

        self.cursor.execute(sql, datos)
        self.cnnet.commit()
        #
        #
        # new_id_client = self.cursor.lastrowid
        # self.id_client.append(new_id_client)
        #
        # print(new_id_client)

        if self.cursor.rowcount > 0:
            print("Datos cargados correstamente")
        else:
            print("Error al cargar datos")

        self.cursor.execute("SELECT * FROM clientes")
        rows = self.cursor.fetchall()

        for row in rows:
            print(row)

        sql = "SELECT id FROM clientes WHERE nombre=%s"
        self.cursor.execute(sql, (name,))
        result = self.cursor.fetchone()

        if result:
            print(f"Name: ", name, "ID: ", result)
        else:
            print("no Data found")

        #
        # self.cursor.close()
        # self.cnnet.close()

    def select_record(self):
        self.name_entry.delete(0, tk.END)
        self.sur_entry.delete(0, tk.END)
        self.dni_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.city_entry.delete(0, tk.END)
        self.prov_entry.delete(0, tk.END)
        self.postal_entry.delete(0, tk.END)


        selected = self.tabla.focus()
        values = self.tabla.item(selected, "values")



        sql = """SELECT id FROM clientes WHERE
            nombre=%s AND apellido=%s AND DNI=%s AND edad=%s
            AND telefono=%s AND email=%s AND direccion=%s AND
            ciudad=%s AND provincia=%s AND codigo_postal=%s
            """

        datt = (
            values[0],
            values[1],
            values[2],
            values[3],
            values[4],
            values[5],
            values[6],
            values[7],
            values[8],
            values[9]
        )

        self.cursor.execute(sql, datt)
        self.cnnet.commit()
        row = self.cursor.fetchone()


        if row:
            self.result = row[0]

        print(self.result)

        self.name_entry.insert(0, values[0])
        self.sur_entry.insert(0, values[1])
        self.dni_entry.insert(0, values[2])
        self.age_entry.insert(0, values[3])
        self.phone_entry.insert(0, values[4])
        self.email_entry.insert(0, values[5])
        self.address_entry.insert(0, values[6])
        self.city_entry.insert(0, values[7])
        self.prov_entry.insert(0, values[8])
        self.postal_entry.insert(0, values[9])

    def modify(self):
        name = self.name_entry.get()
        surname = self.sur_entry.get()
        dni = self.dni_entry.get()
        age = self.age_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        city = self.city_entry.get()
        prov = self.prov_entry.get()
        postal = self.postal_entry.get()

        selected = self.tabla.focus()
        self.tabla.item(selected, text="", values=(
            name,
            surname,
            dni,
            age,
            phone,
            email,
            address,
            city,
            prov,
            postal
        ))

        sql = """UPDATE clientes SET 
                 nombre=%s,
                 apellido=%s,
                 DNI=%s,
                 edad=%s,
                 telefono=%s,
                 email=%s,
                 direccion=%s,
                 ciudad=%s,
                 provincia=%s,
                 codigo_postal=%s
            WHERE id=%s
            """

        datos = (
            name,
            surname,
            dni,
            age,
            phone,
            email,
            address,
            city,
            prov,
            postal,
            self.result
        )

        self.cursor.execute(sql, datos)
        self.cnnet.commit()

        if self.cursor.rowcount > 0:
            print("Datos actualizados correstamente")
        else:
            print("Error al actualizar datos")

        self.name_entry.delete(0, tk.END)
        self.sur_entry.delete(0, tk.END)
        self.dni_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.city_entry.delete(0, tk.END)
        self.prov_entry.delete(0, tk.END)
        self.postal_entry.delete(0, tk.END)

    def delete(self):
        selected = self.tabla.selection()

        for i in selected:
            self.tabla.delete(i)


        sql = """DELETE FROM clientes WHERE id=%s"""

        self.cursor.execute(sql, (self.result,))
        self.cnnet.commit()

        if self.cursor.rowcount > 0:
            print("Datos eliminados con exito")
        else:
            print("Error al eliminar datos")
