import sqlite3

class Connection():

    def CrearConexion():
        try:
            conexion=sqlite3.Connection('Dispositivos.db')
            cursor = conexion.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS Bloques (Id_Bloque  INTEGER PRIMARY KEY, NombreBloque TEXT NOT NULL)''');
            cursor.execute('''CREATE TABLE IF NOT EXISTS Oficinas (Id_Oficinas INTEGER PRIMARY KEY,Id_Bloque INTEGER, NombreOficina TEXT NOT NULL , FOREIGN KEY (Id_Bloque) REFERENCES Bloques(Id_Bloque) )''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS Dispositivos (Id_Oficinas INTEGER,id INTEGER PRIMARY KEY,serial TEXT NOT NULL,fecha_ingreso datatime NOT NULL,fecha_garantia datatime NOT NULL,tipo TEXT NOT NULL,marca TEXT NOT NULL,modelo TEXT NOT NULL, FOREIGN KEY (Id_Oficinas) REFERENCES Oficinas(Id_Oficinas) )''')
            conexion.commit()
            print(conexion,"creada con exito")
            return  cursor
        except sqlite3.Error as e:
            print(e)
    def EjecutarConsultasInsertBloque(ejecutar,valores=None):

        try:
            conexion = sqlite3.Connection('Dispositivos.db')
            cursor = conexion.cursor()

            cursor.execute(ejecutar)
            conexion.commit()
            conexion.rollback()
            return cursor.fetchall()
        except sqlite3.Error as e:
            conexion.rollback()

    CrearConexion()