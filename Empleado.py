import tkinter as tk
from tkinter import ttk
from Database import tabla_empleado


class Empleado(tk.Toplevel):
    def __init__(self, vna):
        super().__init__(vna)
        self.title("Ventana Empleado")
        self.geometry("1200x620")


        self.connect = tabla_empleado()
        self.cursor = self.connect.cursor(buffered=True)
        self.result = 0

        self.cursor.execute("SHOW TABLES")

        for i in self.cursor:
            print(i)


        self.crud_buttons()

############################- LABELS & ENTRY'S -#########################################
        tk.Label(self, text="").grid(row=1, column=0, pady=10)
        tk.Label(self, text="Nombre").grid(row=2, column=0, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=2, column=1, pady=5)

        tk.Label(self, text="Apellido").grid(row=3, column=0, pady=5)
        self.surn_entry = tk.Entry(self)
        self.surn_entry.grid(row=3, column=1, pady=5)

        tk.Label(self, text="Nro. Seg. Social").grid(row=4, column=0, pady=5)
        self.cuit_entry = tk.Entry(self)
        self.cuit_entry.grid(row=4, column=1, pady=5)

        tk.Label(self, text="DNI").grid(row=5, column=0, pady=5)
        self.dni_entry = tk.Entry(self)
        self.dni_entry.grid(row=5, column=1, pady=5)

        tk.Label(self, text="F. de Nac").grid(row=6, column=0, pady=5)
        self.nac_entry = tk.Entry(self)
        self.nac_entry.grid(row=6, column=1, pady=5)

        tk.Label(self, text="Telefono").grid(row=7, column=0, pady=5)
        self.phone_entry = tk.Entry(self)
        self.phone_entry.grid(row=7, column=1)

        tk.Label(self, text="Email").grid(row=8, column=0, pady=5)
        self.mail_entry = tk.Entry(self)
        self.mail_entry.grid(row=8, column=1)

        tk.Label(self, text="Direccion").grid(row=9, column=0, pady=5)
        self.address_entry = tk.Entry(self)
        self.address_entry.grid(row=9, column=1)

        tk.Label(self, text="Puesto").grid(row=10, column=0, pady=5)
        self.pos_entry = tk.Entry(self)
        self.pos_entry.grid(row=10, column=1, pady=5)

        tk.Label(self, text="Sueldo").grid(row=11, column=0, pady=5)
        self.salary_entry = tk.Entry(self)
        self.salary_entry.grid(row=11, column=1)

        tk.Label(self, text="Horas Trabajadas").grid(row=12, column=0, pady=5)
        self.hours_entry = tk.Entry(self, width=20)
        self.hours_entry.grid(row=12, column=1)


    ############################- TABLAS -#########################################
        columnas = (
            "Nombre",
            "Apellido",
            "Nro. Seg. Social",
            "DNI",
            "F. Nac",
            "Telefono",
            "Email",
            "Direccion",
            "Cargo",
            "Sueldo",
            "Horas Trabajadas",
            "Liquidacion"
        )

        self.tablas = ttk.Treeview(
            self,
            columns=columnas,
            show="headings",
            height=10
        )

        for i in columnas:
            self.tablas.heading(i, text=i)
            self.tablas.column(i, width=90)

        self.tablas.grid(
            row=13,
            column=0,
            columnspan=5,
            pady=25
        )

    def crud_buttons(self):
        button_save = tk.Button(self, text="Guardar", command=self.save_data, width=12)
        button_save.grid(row=4, column=2)

        button_select = tk.Button(self, text="Seleccionar", command=self.select_data, width=12)
        button_select.grid(row=5, column=2)

        button_modify = tk.Button(self, text="Modificar", command=self.modify_data, width=12)
        button_modify.grid(row=6, column=2)

        button_delete = tk.Button(self, text="Eliminar", command=self.delete_data, width=12)
        button_delete.grid(row=7, column=2)

        button_close = tk.Button(self, text="Cerrar", command=self.destroy,width=12)
        button_close.grid(row=13, column=5, columnspan=2)

    def save_data(self):
        name = self.name_entry.get()
        surn = self.surn_entry.get()
        cuit = self.cuit_entry.get()
        dni = self.dni_entry.get()
        nac = self.nac_entry.get()
        phone = self.phone_entry.get()
        email = self.mail_entry.get()
        address = self.address_entry.get()
        pos = self.pos_entry.get(),
        salary = self.salary_entry.get()
        hours = self.hours_entry.get()
        total = int(self.sueldo())

        new_puesto = "".join(pos)

        self.tablas.insert("", "end", values=(
            name,
            surn,
            cuit,
            dni,
            nac,
            phone,
            email,
            address,
            pos,
            salary,
            hours,
            total
        ))

        sql = """INSERT INTO empleado(
        nombre, apellido, nro_seg_soc, dni, 
        nac, telefono, email, direccion, cargo,
        sueldo, horas, liquidacion) 
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        datos = (
            name,
            surn,
            cuit,
            dni,
            nac,
            phone,
            email,
            address,
            new_puesto,
            salary,
            hours,
            total
        )

        self.cursor.execute(sql, datos)
        self.connect.commit()

        if self.cursor.rowcount > 0:
            print("Datos guardados con exito")
        else:
            print("Error al almacenar datos")


        self.cursor.execute("SELECT * FROM empleado")
        rows = self.cursor.fetchall()

        for row in rows:
            print(row)


    def select_data(self):
        self.name_entry.delete(0, tk.END)
        self.surn_entry.delete(0, tk.END)
        self.cuit_entry.delete(0, tk.END)
        self.dni_entry.delete(0, tk.END)
        self.nac_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.mail_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.pos_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)
        self.hours_entry.delete(0, tk.END)


        selected = self.tablas.focus()
        values = self.tablas.item(selected, "values")

        sql = """SELECT id FROM empleado WHERE
              nombre=%s AND apellido=%s AND nro_seg_soc=%s
              AND dni=%s AND nac=%s AND telefono=%s AND
              email=%s AND direccion=%s AND cargo=%s
              AND sueldo=%s AND horas=%s"""

        datos = (
            values[0],
            values[1],
            values[2],
            values[3],
            values[4],
            values[5],
            values[6],
            values[7],
            values[8],
            values[9],
            values[10],
        )

        self.cursor.execute(sql, datos)
        self.connect.commit()
        empleado_id = self.cursor.fetchone()

        if empleado_id:
            self.result = empleado_id[0]

        print(self.result)

        self.name_entry.insert(0, values[0])
        self.surn_entry.insert(0, values[1])
        self.cuit_entry.insert(0, values[2])
        self.dni_entry.insert(0, values[3])
        self.nac_entry.insert(0, values[4])
        self.phone_entry.insert(0, values[5])
        self.mail_entry.insert(0, values[6])
        self.address_entry.insert(0, values[7])
        self.pos_entry.insert(0, values[8])
        self.salary_entry.insert(0, values[9])
        self.hours_entry.insert(0, values[10])

    def modify_data(self):
        name = self.name_entry.get()
        surn = self.surn_entry.get()
        cuit = self.cuit_entry.get()
        dni = self.dni_entry.get()
        nac = self.nac_entry.get()
        phone = self.phone_entry.get()
        email = self.mail_entry.get()
        address = self.address_entry.get()
        pos = self.pos_entry.get(),
        salary = self.salary_entry.get()
        hours = self.hours_entry.get()
        total = int(self.sueldo())
        new_puesto = "".join(pos)


        selected = self.tablas.focus()

        self.tablas.item(selected, text="", values=(
            name,
            surn,
            cuit,
            dni,
            nac,
            phone,
            email,
            address,
            pos,
            salary,
            hours,
            total
        ))

        sql = """UPDATE empleado SET 
              nombre=%s, apellido=%s, 
              nro_seg_soc=%s, dni=%s,
              nac=%s, telefono=%s, email=%s,
              direccion=%s, cargo=%s, sueldo=%s,
              horas=%s, liquidacion=%s WHERE id=%s"""

        datos = (
            name,
            surn,
            cuit,
            dni,
            nac,
            phone,
            email,
            address,
            new_puesto,
            salary,
            hours,
            total,
            self.result
        )

        self.cursor.execute(sql, datos)
        self.connect.commit()

        if self.cursor.rowcount > 0:
            print("Datos actualizados correctamente")
        else:
            print("Error al actualizar datos")

        self.name_entry.delete(0, tk.END)
        self.surn_entry.delete(0, tk.END)
        self.cuit_entry.delete(0, tk.END)
        self.dni_entry.delete(0, tk.END)
        self.nac_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.pos_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)
        self.hours_entry.delete(0, tk.END)

    def delete_data(self):
        selected = self.tablas.selection()

        for i in selected:
            self.tablas.delete(i)

        sql = """DELETE FROM empleado WHERE id=%s"""

        self.cursor.execute(sql, (self.result,))
        self.connect.commit()

        if self.cursor.rowcount > 0:
            print("Datos Eliminados con exito")
        else:
            print("Error al eliminar datos")

    def sueldo(self):
        salary = int(self.salary_entry.get())
        hours = int(self.hours_entry.get())

        total = (salary * hours) / 30

        return total