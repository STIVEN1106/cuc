from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import sqlite3
import Connection

root=Tk()
root.title("Prueba universidad cuc")
root.geometry("800x800")

Id_Oficinas =int
id =int
serial=str
fecha_ingreso=str
fecha_garantia=str
tipo=str
marca=str
modelo=str

def salir():
    valor=messagebox.askquestion('SALIR',"SALIR DE LA APLICACION")
    if valor=="yes":
        root.destroy()
def limpierCampos():
    Id_Oficinas.set("")
    id.set("")
    serial.set("")
    fecha_ingreso.set("")
    fecha_garantia.set("")
    tipo.set("")
    marca.set("")
    modelo.set("")
def Mensaje():
    acerca='''Prueba universidad CUC'''

def crear():
    Valores=None
    Connection.Connection.CrearConexion()
    try:
        dato=Id_Oficinas.set(""),id.get(""),serial.get(""), fecha_ingreso.get(""),fecha_garantia.get(""), tipo.get(""), marca.get(""),modelo.get("")
        consulta= "insert into oficinas values (?,?,?,?,?,?,?,?)",(dato)
        Connection.Connection.EjecutarConsultasInsertBloque(consulta,Valores)
    except :
        messagebox.showwarning("advertencia","ocurrio un error")
        pass
    limpierCampos()
    mostrar()
def mostrar():
    Valores = None
    Connection.Connection.CrearConexion()
    registros=tree.get_hildren()
    for elemento  in registros:
        tree.delete(elemento)
    try:
        consulta="select * from dispositivos"
        Connection.Connection.EjecutarConsultasInsertBloque(consulta,Valores)
        for row in Connection.Connection.EjecutarConsultasInsertBloque(consulta,Valores):
            tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
    except:
        pass

###################################################################################

tree=ttk.Treeview(height=10,columns=('#0','#1','#2','#3','#4','#5','#6','#7'))
tree.place(x=0,y=130)
tree.column('#0',width=100)
tree.heading('#0',text="ID_OFICINA",anchor=CENTER)
tree.column('#1',width=100)
tree.heading('#1',text="ID_DISPOSITIVO",anchor=CENTER)
tree.column('#2',width=100)
tree.heading('#2',text="SERIAL",anchor=CENTER)
tree.column('#3',width=100)
tree.heading('#3',text="FECHA_INGRESO",anchor=CENTER)
tree.column('#4',width=100)
tree.heading('#4',text="FECHA_GARANTIA",anchor=CENTER)
tree.column('#5',width=100)
tree.heading('#5',text="TIPO",anchor=CENTER)
tree.column('#6',width=100)
tree.heading('#6',text="MARCA",anchor=CENTER)
tree.column('#7',width=100)
tree.heading('#7',text="MODELO",anchor=CENTER)

root.mainloop()


###################################################

def Actualizar():
    Valores = None
    Connection.Connection.CrearConexion()
    try:
        dato = Id_Oficinas.set(""), id.get(""), serial.get(""), fecha_ingreso.get(""), fecha_garantia.get(""), tipo.get(""), marca.get(""), modelo.get("")
        consulta = f"update  oficinas set  id={id.get("")},serial={serial.get("")},fecha_ingreso={fecha_ingreso.get("")},fecha_garantia={fecha_garantia.get("")},tipo={tipo.get("")},marca={marca.get("")},modelo={ modelo.get("")} where Id_Oficinas= {Id_Oficinas.get("")}" (dato)
        Connection.Connection.EjecutarConsultasInsertBloque(consulta, Valores)
    except:
        messagebox.showwarning("advertencia", "ocurrio un error")
        pass

    limpierCampos()
    mostrar()


menubar=Menu(root)
menubasadeat=Menu(menubar,tearoff=0)
me



