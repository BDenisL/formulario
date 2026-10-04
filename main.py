from Cliente import *
from Empleado import Empleado
from Stock import Stock
from Facturacion import Facturacion
from Proveedor import Proveedor


class App:
    def __init__(self, _window):
        self.root = _window
        self.root.title("Ventana Principal")
        self.root.iconify()

        self.secondary_window = []
        self.second_window = None
        self.client_window()

    def client_window(self):
        self.secondary_window.append(self.second_window)
        if self.second_window is not None:
            self.close_window(self.second_window)

        self.second_window = Cliente(self.root)
        self.init_buttons(self.second_window)

    def employee_window(self):
        self.secondary_window.append(self.second_window)

        self.close_window(self.second_window)

        self.second_window = Empleado(self.root)
        self.init_buttons(self.second_window)

    def stock_window(self):
        self.secondary_window.append(self.second_window)

        self.close_window(self.second_window)

        self.second_window = Stock(self.root)
        self.init_buttons(self.second_window)

    def facc_window(self):
        self.secondary_window.append(self.second_window)

        self.close_window(self.second_window)

        self.second_window = Facturacion(self.root)
        self.init_buttons(self.second_window)

    def proveedor_window(self):
        self.secondary_window.append(self.second_window)

        self.close_window(self.second_window)

        self.second_window = Proveedor(self.root)
        self.init_buttons(self.second_window)

    def close_window(self, ventana):
        try:
            ventana.destroy()
        except tk.TclError:
            pass

        if ventana in self.secondary_window:
            self.secondary_window.remove(ventana)

        if not self.secondary_window:
            self.root.destroy()

    def init_buttons(self, ventana):
        button_client = tk.Button(ventana, text="Cliente", command=self.client_window, width=33)
        button_client.grid(row=0, column=0)

        button_e = tk.Button(ventana, text="Empleados", command=self.employee_window, width=33)
        button_e.grid(row=0, column=1)

        button_stock = tk.Button(ventana, text="Stock", command=self.stock_window, width=33)
        button_stock.grid(row=0, column=2)

        button_people = tk.Button(ventana, text="Proveedor", command=self.proveedor_window, width=33)
        button_people.grid(row=0, column=3)

        button_facc = tk.Button(ventana, text="Facturacion", command=self.facc_window, width=33)
        button_facc.grid(row=0, column=4)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

