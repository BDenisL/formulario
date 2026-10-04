import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="mysql_projects"
    )

    return conexion

conect = conectar()
cursor = conect.cursor()

def create_db():
    cursor.execute("CREATE DATABASE mydatabase")

    cursor.execute("SHOW DATABASES")

    for i in cursor:
        print(i)

def delete_database():
    cursor.execute("DROP IF EXISTIS DATABASE mydatabase")

def delete_table(nombre_tabla):
    sql = f"DROP TABLE IF EXISTS `{nombre_tabla}`"

    cursor.execute(sql)
    conect.commit()

def tabla_cliente():
    delete_table("clientes")
    cursor.execute(f"CREATE TABLE clientes("
                   f"id INT AUTO_INCREMENT PRIMARY KEY,"
                   f"nombre VARCHAR(50),"
                   f"apellido VARCHAR(50),"
                   f"DNI VARCHAR(20),"
                   f"edad VARCHAR(2),"
                   f"telefono VARCHAR(30),"
                   f"email VARCHAR(100),"
                   f"direccion VARCHAR(100),"
                   f"ciudad VARCHAR(50),"
                   f"provincia VARCHAR(50),"
                   f"codigo_postal VARCHAR(20))")

    return conect


def tabla_empleado():
    delete_table("empleado")
    cursor.execute(f"CREATE TABLE empleado("
                   f"id INT AUTO_INCREMENT PRIMARY KEY,"
                   f"nombre VARCHAR(50),"
                   f"apellido VARCHAR(50),"
                   f"nro_seg_soc VARCHAR(30),"
                   f"dni VARCHAR(20),"
                   f"nac VARCHAR(6),"
                   f"telefono VARCHAR(30),"
                   f"email VARCHAR(100),"
                   f"direccion VARCHAR(100),"
                   f"cargo VARCHAR(20),"
                   f"sueldo VARCHAR(10),"
                   f"horas INT,"
                   f"liquidacion VARCHAR(20))")

    return conect

def tabla_proveedor():
    delete_table("proveedor")
    cursor.execute(f"CREATE TABLE proveedor("
                   f"id INT AUTO_INCREMENT PRIMARY KEY,"
                   f"nombre VARCHAR(50),"
                   f"documento VARCHAR(30),"
                   f"telefono VARCHAR(30),"
                   f"email VARCHAR(100),"
                   f"servicios VARCHAR(100),"
                   f"direccion VARCHAR(100),"
                   f"ciudad VARCHAR(50),"
                   f"provincia VARCHAR(50),"
                   f"codigo_postal VARCHAR(20))")

    return conect


def tabla_stock():
    delete_table("stock")
    cursor.execute(f"CREATE TABLE stock("
                   f"id INT AUTO_INCREMENT PRIMARY KEY,"
                   f"id_02 VARCHAR(80),"
                   f"nombre VARCHAR(50),"
                   f"fabricante VARCHAR(100),"
                   f"cantidad VARCHAR(25),"
                   f"costo VARCHAR(25),"
                   f"valor_invent INT)")

    return conect

