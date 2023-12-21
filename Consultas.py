from Api import API
from Connection import Connection
import sqlite3
class CrearConsultas():



    def InsertarBloques():
        BloquesPorInsertar = [{1: 'Bloque_A'}, {2: 'Bloque_B'}, {3: 'Bloque_c'}, {4: 'Bloque_d'}]

        for i in BloquesPorInsertar:
            clave_valor = i
            for c in clave_valor.keys():
                for m in clave_valor.values():
                    try:
                        valores = (c, str(m))  # Convertir 'm' a una cadena antes de la consulta
                        #print(valores)
                        consulta = f"INSERT INTO Bloques (Id_bloque,'NombreBloque') VALUES (({valores[0]}),('{valores[1]}'))"
                        #print(consulta)
                        Connection.EjecutarConsultasInsertBloque(consulta, valores)
                    except sqlite3.Error as e:
                        print(e)

    def InsertarOficinas():
        Valores = None
        Consulta='Select * from Bloques'
        cont_id = 0
        resultado=Connection.EjecutarConsultasInsertBloque(Consulta,Valores)
        Id_oficinas = 0
        #print(resultado)
        for i in resultado:

            if i[Id_oficinas]==1:
                cont = 0
                #print("entro1")
                m = 1
                for m in range(2):

                    cont+=1
                    cont_id += 1
                    Consulta = f'Insert into Oficinas (Id_Oficinas,Id_Bloque,NombreOficina) values ({cont_id},{i[Id_oficinas]},"oficina-{cont}") '
                    resultado = Connection.EjecutarConsultasInsertBloque(Consulta, Valores)
                    #Consulta=f"Select * from Oficinas"
                    #resultado = Connection.EjecutarConsultasInsertBloque(Consulta, Valores)
                    #print(resultado)

            if i[Id_oficinas]==2:
                cont = 0
                #print("entro2")
                m = 1
                for m in range(1):
                    cont+=1
                    cont_id+=1
                    Consulta = f'Insert into Oficinas (Id_Oficinas,Id_Bloque,NombreOficina) values ({cont_id},{i[Id_oficinas]},"oficina-{cont}") '
                    resultado = Connection.EjecutarConsultasInsertBloque(Consulta, Valores)

            if i[Id_oficinas]==3:
                cont = 0
                #print("entro3")
                m = 1
                for m in range(3):
                    cont+=1
                    cont_id += 1
                    Consulta = f'Insert into Oficinas (Id_Oficinas,Id_Bloque,NombreOficina) values ({cont_id},{i[Id_oficinas]},"oficina-{cont}") '
                    resultado = Connection.EjecutarConsultasInsertBloque(Consulta, Valores)
            cont = 0

            if i[Id_oficinas]==4:
                cont = 0
                #print("entro4")
                m = 1
                for m in range(3):
                    cont+=1
                    cont_id += 1
                    Consulta = f'Insert into Oficinas (Id_Oficinas,Id_Bloque,NombreOficina) values ({cont_id},{i[Id_oficinas]},"oficina-{cont}") '
                    resultado = Connection.EjecutarConsultasInsertBloque(Consulta, Valores)
            cont = 0



    def InsertarDatosDispositivos():
        Valores=None
        Consulta='select count(*) from oficinas'
        resultado=Connection.EjecutarConsultasInsertBloque(Consulta,Valores)
        #print(resultado)
        PorAgregar = API.GetApi()

        #print(PorAgregar[0])
        cont = 1
        mul=3
        for m in resultado:


            inicio = 1
            fin = 30
            for i in range(inicio, fin , 1):
                ValoresBD=[PorAgregar[i]]

                mul=i
                for s in ValoresBD:
                    clave_valor=s
                    valores=clave_valor.values()
                    lista_de_valores=list(valores)
                    if (i%3)==0:
                        cont += 1
                    #print(lista_de_valores)
                    #print(i)
                    try:
                            consulta = f'INSERT INTO Dispositivos (Id_Oficinas,id,serial,fecha_ingreso,fecha_garantia,tipo,marca,modelo) values ({cont},"{lista_de_valores[0]}","{lista_de_valores[1]}","{lista_de_valores[2]}","{lista_de_valores[3]}","{lista_de_valores[4]}","{lista_de_valores[5]}","{lista_de_valores[6]}")'
                            #print(consulta)
                            Connection.EjecutarConsultasInsertBloque(consulta,Valores)
                    except sqlite3.Error as e:
                            print(e)
        cont += 1

    InsertarBloques()
    InsertarOficinas()
    InsertarDatosDispositivos()