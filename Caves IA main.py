from ast import Index
from email.headerregistry import SingleAddressHeader
from http.client import NOT_ACCEPTABLE
from itertools import permutations
from logging import CRITICAL
from msilib.schema import ProgId
from operator import index
from re import L
from sys import api_version
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter
from tkinter.font import BOLD
from turtle import clear
from unittest import signals
from urllib.request import AbstractBasicAuthHandler
from zoneinfo import available_timezones
from numpy import append, can_cast, mat, matrix
from pkg_resources import PathMetadata 
import pymysql.cursors
import numpy as np

#ciclos mineros 
ciclominero1 = ['regado_marina','extraccion_marina','acuñadura','limpieza_pata','escaner','mapeo_geomecanico',
'shotcrete_fibra','perforacion_pernos','lechado_pernos','instalacion_malla','hilteo_malla','proyeccion_shotcrete',
'marcacion_topografica','perforacion_avance','carguio_explosivos','tronadura']


#memoria para mostrar tablas frente
tipos = []
tipos.append('tipo')
siglas = []
siglas.append('sigla')
numeros = []
numeros.append('numero')
numeroreferencias = []
numeroreferencias.append('numero referencia')
direcciones = []
direcciones.append('direccion')
direccionreferencias = []
direccionreferencias.append('direccion refencia')
estados = []
estados.append('estado')
tamanios= []
tamanios.append('tamaño')
rutas  = []
rutas.append('ruta critica')
distancias = []
distancias.append('distancia marina')
niveles = []
niveles.append('nivel')
macrobloques = []
macrobloques.append('macrobloque')
sector = []
sector.append('sector')
ides = []
ides.append('id')

#memoria para mostrar tabla equipos 

flota = []
flota.append('Flota')
codigoequipo = []
codigoequipo.append('Codigo equipo')
cantidad = []
cantidad.append('Cantidad')
niveleq = []
niveleq.append('Nivel')

#memoria para mostrar tabla avances 

avance = []
avance.append('Avance')
nivel = []
nivel.append('Nivel')
notaactividad = []
notaactividad.append('Nota actividad')
pkacumulado = []
pkacumulado.append('Distancia acumulada')
fechaav = []
fechaav.append('Fecha')
idfrenteav = []
idfrenteav.append('Id frente')

#memoria para mostrar tabla estadoservicios

estadoservicio = []
estadoservicio.append('Estado servicio')
notaestado = []
notaestado.append('void')
pkservicio = []
pkservicio.append('Distancia')
notapk = []
notapk.append('void')
fecha = []
fecha.append('Fecha')
idfrente = []
idfrente.append('Id frente')

#memoria para mostrar tabla estadofrentes

operacion = []
operacion.append('Operacion')
estadoavance = []
estadoavance.append('Estado avance')
observaciones = []
observaciones.append('Observaciones')
fechaf = []
fechaf.append('Fecha')
criticidad = []
criticidad.append('Criticidad')
direccion = []
direccion.append('Direccion')
idfrentef = []
idfrentef.append('Id frente')

#memoria para mostrar tabla estado equipos

flotae = []
flotae.append('Flota')
nivel = []
nivel.append('Nivel')
fechae = []
fechae.append('Fecha')
estadoe = []
estadoe.append('Estado')
codigoe = []
codigoe.append('Codigo Equipo')

#coneccion bd red local para crear cursores

bd1 = pymysql.connect(host='localhost',
                             user='root',
                             password='1312',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd2 = pymysql.connect(host='localhost',
                             user='root',
                             password='1312',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd3 = pymysql.connect(host='localhost',
                             user='root',
                             password='1312',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd4 = pymysql.connect(host='localhost',
                             user='root',
                             password='1312',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd5 = pymysql.connect(host='localhost',
                             user='root',
                             password='1312',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd6 = pymysql.connect(host='localhost',
                             user='root',
                             password='1312',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd7 = pymysql.connect(host='localhost',
                             user='root',
                             password='1312',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd8 = pymysql.connect(host='localhost',
                             user='root',
                             password='1312',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd9 = pymysql.connect(host='localhost',
                             user='root',
                             password='1312',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd10 = pymysql.connect(host='localhost',
                             user='root',
                             password='1312',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd11 = pymysql.connect(host='localhost',
                             user='root',
                             password='1312',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd12 = pymysql.connect(host='localhost',
                             user='root',
                             password='1312',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd13 = pymysql.connect(host='localhost',
                             user='root',
                             password='1312',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd14 = pymysql.connect(host='localhost',
                             user='root',
                             password='1312',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

def addbdfrentes():
    win4=Tk()
    win4.geometry('300x340')
    frameingreso = Frame(win4)
    frameingreso.pack()

    txtid=Label(frameingreso,text="ID Frente")
    txtid.grid(row="0",column="0")
    entryid= Entry(frameingreso)
    entryid.grid(row="0",column="1")

    txttipo=Label(frameingreso,text="Tipo de frente")
    txttipo.grid(row="1",column="0")
    entrytipo= ttk.Combobox(frameingreso)
    entrytipo.grid(row="1",column="1")
    entrytipo['values'] = ('Cabecera','Calle','Zanja','Fronton Inyeccion','Fronton extraccion')

    txtsigla=Label(frameingreso,text="Sigla de frente")
    txtsigla.grid(row="2",column="0")
    entrysigla= ttk.Combobox(frameingreso)
    entrysigla.grid(row="2",column="1")
    entrysigla['values'] = ('CAB','CAL','ZA','FRI','FRE')

    txtsigla=Label(frameingreso,text="Sigla de referencia")
    txtsigla.grid(row="2",column="0")
    entrysigla= ttk.Combobox(frameingreso)
    entrysigla.grid(row="2",column="1")
    entrysigla['values'] = ('CAB','CAL','ZA','FRI','FRE')
  
    txtnumero=Label(frameingreso,text="Numero de frente")
    txtnumero.grid(row="3",column="0")
    entrynumero= Entry(frameingreso)
    entrynumero.grid(row="3",column="1")

    txtnumeroreferencias=Label(frameingreso,text="Numero referencia")
    txtnumeroreferencias.grid(row="4",column="0")
    entrynumeroreferencias= Entry(frameingreso)
    entrynumeroreferencias.grid(row="4",column="1")

    txtdireccion=Label(frameingreso,text="Direccion de frente")
    txtdireccion.grid(row="5",column="0")
    entrydireccion= ttk.Combobox(frameingreso)
    entrydireccion.grid(row="5",column="1")
    entrydireccion['values'] = ('N','S','E','O')

    txtdireccionreferencias=Label(frameingreso,text="Direccion referencia")
    txtdireccionreferencias.grid(row="6",column="0")
    entrydireccionreferencias= ttk.Combobox(frameingreso)
    entrydireccionreferencias.grid(row="6",column="1")
    entrydireccionreferencias['values'] = ('N','S','E','O')

    txtestado=Label(frameingreso,text="Estado de frente")
    txtestado.grid(row="7",column="0")
    entryestado= ttk.Combobox(frameingreso)
    entryestado.grid(row="7",column="1")
    entryestado['values'] = ('Activo','Inactivo')

    txttamaño =Label(frameingreso,text="Tamaño de frente")
    txttamaño.grid(row="8",column="0")
    entrytamaño= ttk.Combobox(frameingreso)
    entrytamaño.grid(row="8",column="1")
    entrytamaño['values'] = ('C','M','G')

    txtrutacritica=Label(frameingreso,text="Ruta critica")
    txtrutacritica.grid(row="9",column="0")
    entryrutacritica= ttk.Combobox(frameingreso)
    entryrutacritica.grid(row="9",column="1")
    entryrutacritica['values'] = ('Si','No')

    txtdistanciamarina=Label(frameingreso,text="Distancia Marina")
    txtdistanciamarina.grid(row="10",column="0")
    entrydistanciamarina= Entry(frameingreso)
    entrydistanciamarina.grid(row="10",column="1")

    txtnivelfrente=Label(frameingreso,text="Nivel")
    txtnivelfrente.grid(row="11",column="0")
    entrynivelfrente= ttk.Combobox(frameingreso)
    entrynivelfrente.grid(row="11",column="1")
    entrynivelfrente['values'] = ('PD','HD','INY','EXT','CH')

    txtmacrobloque=Label(frameingreso,text="Macrobloque")
    txtmacrobloque.grid(row="12",column="0")
    entrymacrobloque= ttk.Combobox(frameingreso)
    entrymacrobloque.grid(row="12",column="1")
    entrymacrobloque['values'] = ('S01','S02','S03','S04','S05')

    txtsector=Label(frameingreso,text="Sector")
    txtsector.grid(row="13",column="0")
    entrysector= ttk.Combobox(frameingreso)
    entrysector.grid(row="13",column="1")
    entrysector['values'] = ('S1','S2')

    txtcodigo=Label(frameingreso,text="Codigo empresa")
    txtcodigo.grid(row="14",column="0")
    entrycodigo= Entry(frameingreso)
    entrycodigo.grid(row="14",column="1")


    def llenarfrente():
        tipo =entrytipo.get()
        sigla = entrysigla.get()
        numero = entrynumero.get()
        numeroreferencias = entrynumeroreferencias.get()
        direccion = entrydireccion.get()
        direccionreferencias = entrydireccionreferencias.get()
        estado =entryestado.get()
        tamaño = entrytamaño.get()
        ruta =entryrutacritica.get()
        distancia =entrydistanciamarina.get()
        nivel = entrynivelfrente.get() 
        macrobloque =entrymacrobloque.get()
        sector = entrysector.get()
        id = entryid.get()
        codigoempresa = entrycodigo.get()
        cursor=bd1.cursor()
        sql =  "insert into frentes(tipo,sigla,numero,numero_referencia,direccion,direccion_referencia,estado,tamaño,ruta_critica,distancia_marina,nivel,macrobloque,sector,id_frente,codigo_empresa) value('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (tipo,sigla,numero,numeroreferencias,direccion,direccionreferencias,estado,tamaño,ruta,distancia,nivel,macrobloque,sector,id,codigoempresa)
        try:
         cursor.execute(sql)
         print (sql)
         cursor.close()
         bd1.commit()
         bd1.close()
        except Exception as e:
            print("exception : ")
            
       # cursor.close()
        #bd.commit()
       # bd.close()
    
        win4.destroy()

    botonllenarbd=Button(frameingreso,text="Añadir a la Bd",command=llenarfrente)
    botonllenarbd.grid(row="15")


def addequipo():
    win4=Tk()
    frameingreso = Frame(win4)
    frameingreso.pack()

    def llenarequipo():
        flota= entryflota.get()
        codigo = entrycod.get()
        cantidade= entrycantidade.get()
        nivele= entrynivele.get()
       
        cursor=bd2.cursor()
        sql =  "insert into equipos(flota,codigo_equipo,cantidad,nivel) value('%s','%s','%s','%s')" % (flota,codigo,cantidade,nivele)
        try:
         cursor.execute(sql)
         cursor.close()
         bd2.commit()
         bd2.close()
        except Exception as e:
         print(e)
       # cursor.close()
        #bd.commit()
       # bd.close()
        
        win4.destroy()


    txtflota =Label(frameingreso,text="Flota") #lista desplegable
    txtflota.grid(row="0",column="0")
    entryflota = ttk.Combobox(frameingreso)
    entryflota.grid(row="0",column="1")
    entryflota['values'] = ('Jumbo fortificación','Jumbo avance','LHD','Manitou','Roboshot','Mixer','Camión marina','Retroexcavadora')

    txtcodigo=Label(frameingreso,text="Codigo_equipo")
    txtcodigo.grid(row="1",column="0")
    entrycod= Entry(frameingreso)
    entrycod.grid(row="1",column="1")

    txtcantidade=Label(frameingreso,text="Cantidad")
    txtcantidade.grid(row="2",column="0")
    entrycantidade= Entry(frameingreso)
    entrycantidade.grid(row="2",column="1")

    txtnivele=Label(frameingreso,text="Nivel de equipo") 
    txtnivele.grid(row="3",column="0")
    entrynivele= ttk.Combobox(frameingreso)
    entrynivele.grid(row="3",column="1")
    entrynivele['values'] = ('HD','PD','CH','INY','EXT','TI')


    botonllenarbd=Button(frameingreso,text="Añadir a la Bd",command=llenarequipo)
    botonllenarbd.grid(row="4")


def modificarfrente():
    win4=Tk()
    win4.geometry('300x380')
    frameingreso = Frame(win4)
    frameingreso.pack()

    txtid=Label(frameingreso,text="ID Frente")
    txtid.grid(row="0",column="0")
    entryid= Entry(frameingreso)
    entryid.grid(row="0",column="1")

    txttipo=Label(frameingreso,text="Tipo ")
    txttipo.grid(row="1",column="0")
    entrytipo= ttk.Combobox(frameingreso)
    entrytipo.grid(row="1",column="1")
    entrytipo['values'] = ('Cabecera','Calle','Zanja','Fronton Inyeccion','Fronton extraccion')

    txtsigla=Label(frameingreso,text="Sigla")
    txtsigla.grid(row="2",column="0")
    entrysigla= ttk.Combobox(frameingreso)
    entrysigla.grid(row="2",column="1")
    entrysigla['values'] = ('CAB','CAL','ZA','FRI','FRE')
  
    txtnumero=Label(frameingreso,text="Numero")
    txtnumero.grid(row="3",column="0")
    entrynumero= Entry(frameingreso)
    entrynumero.grid(row="3",column="1")

    txtnumeroreferencias=Label(frameingreso,text="Numero referencia")
    txtnumeroreferencias.grid(row="4",column="0")
    entrynumeroreferencias= Entry(frameingreso)
    entrynumeroreferencias.grid(row="4",column="1")

    txtdireccion=Label(frameingreso,text="Direccion")
    txtdireccion.grid(row="5",column="0")
    entrydireccion= ttk.Combobox(frameingreso)
    entrydireccion.grid(row="5",column="1")
    entrydireccion['values'] = ('N','S','E','O')

    txtdireccionreferencias=Label(frameingreso,text="Direccion referencia")
    txtdireccionreferencias.grid(row="6",column="0")
    entrydireccionreferencias= ttk.Combobox(frameingreso)
    entrydireccionreferencias.grid(row="6",column="1")
    entrydireccionreferencias['values'] = ('N','S','E','O')

    txtestado=Label(frameingreso,text="Estado")
    txtestado.grid(row="7",column="0")
    entryestado= ttk.Combobox(frameingreso)
    entryestado.grid(row="7",column="1")
    entryestado['values'] = ('Activo','Inactivo')

    txttamaño =Label(frameingreso,text="Tamaño")
    txttamaño.grid(row="8",column="0")
    entrytamaño= ttk.Combobox(frameingreso)
    entrytamaño.grid(row="8",column="1")
    entrytamaño['values'] = ('C','M','G')

    txtrutacritica=Label(frameingreso,text="Ruta critica")
    txtrutacritica.grid(row="9",column="0")
    entryrutacritica= ttk.Combobox(frameingreso)
    entryrutacritica.grid(row="9",column="1")
    entryrutacritica['values'] = ('Si','No')

    txtdistanciamarina=Label(frameingreso,text="Distancia Marina")
    txtdistanciamarina.grid(row="10",column="0")
    entrydistanciamarina= Entry(frameingreso)
    entrydistanciamarina.grid(row="10",column="1")

    txtnivelfrente=Label(frameingreso,text="Nivel")
    txtnivelfrente.grid(row="11",column="0")
    entrynivelfrente= ttk.Combobox(frameingreso)
    entrynivelfrente.grid(row="11",column="1")
    entrynivelfrente['values'] = ('HD','PD','CH','INY','EXT','TI')

    txtmacrobloque=Label(frameingreso,text="Macrobloque")
    txtmacrobloque.grid(row="12",column="0")
    entrymacrobloque= ttk.Combobox(frameingreso)
    entrymacrobloque.grid(row="12",column="1")
    entrymacrobloque['values'] = ('S01','S02','S03','S04','S05')

    txtsector=Label(frameingreso,text="Sector")
    txtsector.grid(row="13",column="0")
    entrysector= ttk.Combobox(frameingreso)
    entrysector.grid(row="13",column="1")
    entrysector['values'] = ('S1','S2')

    txtcodigo=Label(frameingreso,text="Codigo empresa")
    txtcodigo.grid(row="14",column="0")
    entrycodigo= Entry(frameingreso)
    entrycodigo.grid(row="14",column="1")


def ingresomain(rut):
    rutt=rut
    win3 = Tk()
    win3.config(bg="cornflowerblue")
    win3.geometry('500x300')
    framemain = Frame(win3)
    framemain.pack(expand=1)
    framemain.config(bg="royalblue", width="500", height="300", relief="sunken")

    botonFrentes = Button(framemain,text="CREAR NUEVO FRENTE",command=addbdfrentes)
    botonFrentes.grid(row="2", column="1")

    botonTopografia = Button(framemain,text="CREAR NUEVO EQUIPO",command=addequipo)
    botonTopografia.grid(row="3", column="1")


    def verfrentesrut():
        numfilas = 1
        numcolumnas = 14
        win4 = Tk()
        win4.title('Frentes asociados al RUT')
        tabla=Frame(win4)
        tabla.pack()
        def creartablafrentes():
               for f in range(numfilas):
                    for j in range(numcolumnas):
                            x = Entry(tabla)
                            x.grid(row = f, column = j)
                            if (j==0):
                                x.insert(END,tipos[f])
                            if (j==1):
                                x.insert(END,siglas[f])
                            if (j==2):
                                x.insert(END,numeros[f])
                            if (j==3):
                                x.insert(END,numeroreferencias[f])    
                            if (j==4):
                                x.insert(END,direcciones[f])
                            if (j==5):
                                x.insert(END,direccionreferencias[f])
                            if (j==6):
                                x.insert(END,estados[f])
                            if (j==7):
                                x.insert(END,tamanios[f])
                            if (j==8):
                                x.insert(END,rutas[f])
                            if (j==9):
                                x.insert(END,distancias[f])
                            if (j==10):
                                x.insert(END,niveles[f])
                            if (j==11):
                                x.insert(END,macrobloques[f])
                            if (j==12):
                                x.insert(END,sector[f])
                            if (j==13):
                             x.insert(END,ides[f])   
                        
        cursor = bd3.cursor()
        cursor2 =  bd3.cursor()
        sql2 = 'SELECT * from usuarios'
        sql = 'SELECT * from frentes'
        try:
            cursor.execute(sql)
            cursor2.execute(sql2)
            data = cursor.fetchall()
            users = cursor2.fetchall()

            for p in data:
                codigo=p['codigo_empresa']
                if (codigo==rutt):
                    numfilas = numfilas + 1

            for i in data:
                tipo = i['tipo']
                sigla = i['sigla']
                numero = i['numero']
                numeroreferencia = i['numero_referencia']
                direccion = i['direccion']
                direccionreferencia = i['direccion_referencia']
                estado = i['estado']
                tamaño = i['tamaño']
                ruta = i['ruta_critica']
                distancia = i['distancia_marina']
                nivel = i['nivel']
                macrobloque = i['macrobloque']
                sectores = i['sector']
                id = i['id_frente']
                codigo=i['codigo_empresa']
                if(codigo==rutt):
                    tipos.append(tipo)
                    siglas.append(sigla)
                    numeros.append(numero)
                    numeroreferencias.append(numeroreferencia)
                    direcciones.append(direccion)
                    direccionreferencias.append(direccionreferencia)
                    estados.append(estado)
                    tamanios.append(tamaño)
                    rutas.append(ruta)
                    distancias.append(distancia)
                    niveles.append(nivel)
                    macrobloques.append(macrobloque)
                    sector.append(sectores)
                    ides.append(id)
            cursor.close()
            bd3.commit()
            bd3.close
        except Exception as e:
            print(e)
        creartablafrentes()
  

    def vereequipos():
        numfilas = 1
        numcolumnas = 4
        win4 = Tk()
        win4.title('Recurso_equipos')
        tabla = Frame(win4)
        tabla.pack()
        def creartablaequipos():
            for f in range(numfilas):
                for j in range(numcolumnas):
                    x = Entry(tabla)
                    x.grid(row = f, column = j)
                    if(j==0):
                        x.insert(END,flota[f])
                    if(j==1):
                        x.insert(END,codigoequipo[f])
                    if(j==2):
                        x.insert(END,cantidad[f])
                    if(j==3):
                        x.insert(END,niveleq[f])
        
        cursor = bd4.cursor()
    
        sql =  "SELECT * from recurso_equipos"
        try: 
            cursor.execute(sql)
            data = cursor.fetchall()
            
            for i in data:
                flotaa = i ['flota']
                flota.append(flotaa)
                codigoequipoo = i ['codigo_equipo']
                codigoequipo.append(codigoequipoo)
                cantidadd = i ['cantidad']
                cantidad.append(cantidadd)
                niveleqq = i ['nivel']
                niveleq.append(niveleqq)
                numfilas = numfilas + 1

            cursor.close()
            bd4.commit()
            bd4.close()
        except Exception as e :
                print("exception : ",e)      
        creartablaequipos()

        #bd.commit()
        #cursor.close()
        #bd.close()'''
        
    def verestadoservicios():
        numfilas = 1
        numcolumnas = 6
        win4 = Tk()
        win4.title('Estado servicios')
        tabla = Frame(win4)
        tabla.pack()
        def creartablaservicios():
            for f in range(numfilas):
                for j in range(numcolumnas):
                    x = Entry(tabla)
                    x.grid(row = f, column = j)
                    if(j==0):
                        x.insert(0,estadoservicio[f])
                    if(j==1):
                        x.insert(0,notaestado[f])
                    if(j==2):
                        x.insert(0,pkservicio[f])
                    if(j==3):
                        x.insert(0,notapk[f])
                    if(j==4):
                        x.insert(0,fecha[f])
                    if(j==5):
                        x.insert(0,idfrente[f])

        cursor = bd5.cursor()

        sql =  "SELECT * from estado_servicios"
        try: 
            cursor.execute(sql)
            data = cursor.fetchall()

            for i in data:
                estadoservicioo = i ['estado_servicio']
                estadoservicio.append(estadoservicioo)
                notaestadoo = i ['nota_estado']
                notaestado.append(notaestadoo)
                pkservicioo = i ['pk_servicio']
                pkservicio.append(pkservicioo)
                notapka = i ['nota_pk']
                notapk.append(notapka)
                fechaa = i ['fecha']
                fecha.append(fechaa)
                idfrentee = i ['id_frente']
                idfrente.append(idfrentee)
                numfilas = numfilas + 1

            cursor.close()
            bd5.commit()
            bd5.close()
        except Exception as e :
                print("exception : ",e )
        creartablaservicios()

        #bd.commit()
        #cursor.close()
        #bd.close()'''


    def veravances():
        numfilas = 1
        numcolumnas = 6
        win4 = Tk()
        win4.title('Avances')
        tabla=Frame(win4)
        tabla.pack()
        def creartablaavance(): 
            for f in range(numfilas):
                for j in range (numcolumnas):
                    x = Entry(tabla)
                    x.grid(row = f, column = j)
                    if(j==0):
                            x.insert(0,avance[f])
                    if(j==1):
                            x.insert(0,nivel[f])
                    if(j==2):
                            x.insert(0,notaactividad[f])
                    if(j==3):
                            x.insert(0,pkacumulado[f])
                    if(j==4):
                            x.insert(0,fechaav[f])
                    if(j==5):
                            x.insert(0,idfrenteav[f])

        cursor = bd6.cursor()

        sql =  "SELECT * from avances"
        try:
            cursor.execute(sql)
            data = cursor.fetchall()

            for i in data:
                avancee = i ['avance']
                avance.append(avancee)
                nivelav = i ['nivel']
                nivel.append(nivelav)
                notaactividadd = i ['nota_actividad']
                notaactividad.append(notaactividadd)
                pkacumuladoo = i ['pk_acumulado']
                pkacumulado.append(pkacumuladoo)
                fechaavv = i ['fecha']
                fechaav.append(fechaavv)
                idfrenteavv = i ['id_frente']
                idfrenteav.append(idfrenteavv)
                numfilas = numfilas + 1

            cursor.close()
            bd6.commit()
            bd6.close()
        except Exception as e :
            print("exception : ",e )
        creartablaavance()

        #bd.commit()
        #cursor.close()
        #bd.close()'''


    def estadofrentes():
        numfilas = 1
        numcolumnas = 7
        win4 = Tk()
        win4.title('Estado frentes')
        tabla = Frame(win4)
        tabla.pack()
        def creartablaestadofrentes():
            for f in range(numfilas):
                for j in range(numcolumnas):
                    x = Entry(tabla)
                    x.grid(row = f, column = j)
                    if(j==0):
                        x.insert(0,operacion[f])
                    if(j==1):
                        x.insert(0,estadoavance[f])
                    if(j==2):
                        x.insert(0,observaciones[f])
                    if(j==3):
                        x.insert(0,fechaf[f])
                    if(j==4):
                        x.insert(0,criticidad[f])
                    if(j==5):
                        x.insert(0,direccion[f])
                    if(j==6):
                        x.insert(0,idfrentef[f])

        cursor = bd7.cursor()
        sql = "SELECT * from estado_frentes"  
        try:
            cursor.execute(sql)
            data = cursor.fetchall()

            for i in data:
                operacionn = i ['operacion']
                operacion.append(operacionn)
                estadoavancee = i ['estado_avance']
                estadoavance.append(estadoavancee)
                observacioness = i ['observaciones']
                observaciones.append(observacioness)
                fechaff = i ['fecha']
                fechaf.append(fechaff)
                criticidadd = i ['criticidad']
                criticidad.append(criticidadd)
                direccionn = i ['direccion']
                direccion.append(direccionn)
                idfrenteff = i['id_frente']
                idfrentef.append(idfrenteff)
                numfilas = numfilas + 1
            
            cursor.close()
            bd7.commit()
            bd7.close()
        except Exception as e :
                print("exception : ",e )
        creartablaestadofrentes()


    def verestadoequipos():
        numfilas = 1
        numcolumnas = 5
        win4 = Tk()
        win4.title('Estado equipos')
        tabla = Frame(win4)
        tabla.pack()
        def creartablaestadoequipos():
            for f in range(numfilas):
                for j in range(numcolumnas):
                    x = Entry(tabla)
                    x.grid(row = f, column = j)
                    if(j==0):
                        x.insert(END,flotae[f])
                    if(j==1):
                        x.insert(END,nivel[f])
                    if(j==2):
                        x.insert(END,fechae[f])
                    if(j==3):
                        x.insert(END,estadoe[f])    
                    if(j==4):
                        x.insert(END,codigoe[f])

        cursor = bd8.cursor()

        sql = "SELECT * from estado_equipos"
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            
            for i in data:
                flotaee = i ['flota']
                flotae.append(flotaee)
                nivell = i ['nivel']
                nivel.append(nivell)
                fechaee = i ['fecha']
                fechae.append(fechaee)
                estadoee = i ['estado']
                estadoe.append(estadoee)
                codigoee = i ['codigo_equipo']
                codigoe.append(codigoee)
                numfilas = numfilas + 1
            
            cursor.close()
            bd8.commit()
            bd8.close()
        except Exception as e :
            print("exception : ",e )
        creartablaestadoequipos()

        #bd.commit()
        #cursor.close()
        #bd.close()'''


# algoritmo 1
    
    cursor=bd13.cursor()
    totalfrentes = cursor.execute("select * from frentes")
    print("TOTAL FRENTES")
    print(totalfrentes)

# Definir listas para priorizacion

# Ruta critica 
    print("RUTA CRITICA")
    rutacri = []
    rs = []
    rn = []
    cursor.execute("select id_frente from frentes where ruta_critica = 'si'")
    resusi = cursor.fetchall()
    for x in resusi:
        e = x['id_frente']
        rutacri.append(e)
        rs.append(e)
    cursor.execute("select id_frente from frentes where ruta_critica = 'no'")
    resuno = cursor.fetchall()
    for x in resuno:
        e = x['id_frente']
        rutacri.append(e)
        rn.append(e)

    print("P1", rutacri)

# Urgencia

    print("URGENCIA")
    urgencia = []
    p2 = []
    cursor.execute("select id_frente from frentes order by largo desc")
    mari = cursor.fetchall()
    for z in mari:
        p = z['id_frente']
        urgencia.append(p)
    for u in urgencia:
        for r in rs:
            if u ==r:
                p2.append(u)
    for u in urgencia:
        for r in rn:
            if u ==r:
                p2.append(u)
    
    print("P2", p2)

# Tronadura proxima

    print("TRONADURA PROXIMA") 
    troprosi = []
    troprono = []
    idaux = []
    operaux = []
    dista = []
    distasi= []
    distano = []
    cursor.execute("select id_frente,operacion from estado_frentes")
    trop = cursor.fetchall()
    for t in trop:
        fren = t['id_frente']
        idaux.append(fren)
        oper = t['operacion']
        operaux.append(oper)
    for o in operaux:
        for c in ciclominero1:
            if c == o:
                aux = ciclominero1.index(c)
                dis = 15-aux
                dista.append(dis)

    for i, num in enumerate(dista):
        menor= None
        posi = None
        if (num != 0):
            if (num not in distasi and num not in distano):
                if (num <= 4):
                    menor = num
                    posi = i
        if menor != None:
            troprosi.append(idaux[posi])
            distasi.append(menor)
    
    for i, num in enumerate(dista):
        x = 1
        if (num == 0 or num > 4):
            menoraux = num
            posiaux = i
            x=2
        if x == 2:  
            troprono.append(idaux[posiaux])
            distano.append(menoraux)

# Urgencia tronadura prox

    tp = []

    for u in urgencia:
        for r in troprosi:
            if u == r:
                tp.append(u)

    for p in p2:
        if (p not in tp):
            tp.append(p)
    
    print("P3", tp)

# foco

    print("FOCO")
    p4 = []
    foco = []
    cursor.execute("select id_frente from frentes where foco = '1'")
    foc = cursor.fetchall()
    for b in foc:
        t = b['id_frente']
        foco.append(t)

    for p in tp:
        for f in foco:
            if f == p:
                p4.append(p)

    for p in tp:
        if (p not in p4):
            p4.append(p)

    print("P4", p4)

# extraccion marina

    print("EXTRACCION MARINA")
    idtro = []
    p5 = []
    cursor.execute("select id_frente from estado_frentes where operacion = 'tronadura' ")
    tro = cursor.fetchall()
    for c in tro:
        x = c['id_frente']
        idtro.append(x)

    for p in p4:
        for i in idtro:
            if p == i:
                p5.append(p)

    for p in p4:
        if (p not in p5):
            p5.append(p)
        
    print("P5", p5)

# distancia a pique 

    print("DISTANCIA A PIQUE") 
    dista = []
    pf = []
    cursor.execute("select id_frente from frentes order by distancia_marina desc")
    marip = cursor.fetchall()
    for d in marip:
        x = d['id_frente']
        dista.append(x)
    
    for d in dista:
        for i in idtro:
            if d == i:
                pf.append(d)
    
    for p in p5:
        if (p not in pf):
            pf.append(p)

    print("PRIORIZACIÓN", pf)


# Algoritmo 2 (sin sectorización)

    cursor=bd14.cursor()
    totalfrentes = cursor.execute("select * from frentes")
    print("ALGORITMO 2")

    l1= []
    tamf = []
    opf = []
    tamor = []
    opeor = []

    cursor.execute("select id_frente, tamaño from frentes")
    tamfn = cursor.fetchall()
    for x in tamfn:
        tamf.append(x)

    for p in pf:
        for t in tamf:
            if (p == t['id_frente']):
                tamor.append(t['tamaño'])

    
    cursor.execute("select id_frente, operacion from estado_frentes")
    opfn = cursor.fetchall()
    for x in opfn:
        opf.append(x)

    for p in pf:
        for o in opf:
            if (p == o['id_frente']):
                opeor.append(o['operacion'])


    # indice = [ ID - TAMAÑO - ESTADO_FRENTE - 8:00 - 8:30 - 9:00 - 09:30 - 10:00 - 10:30 - 11:00 - 11:30 - 12:00 - 12:30 - 13:00 - 13:30 - 14:00 - 14:30 - 15:00 - 15:30 - 16:00 - 16:30 - 17:00 - 17:30 - 18:00 - 18:30 - 19:00 - 19:30 ]
    
    # tamaños y duraciones c=1 m=2 g=3

    tfc = ['rm','e','e','e','-','ac','-','lp','-','sc','mg','shf','-','-','pp','pp','pp','l','l','l','-','-','m','m','m','h','h','h','sh','sh','-','-','mt','pa','pa','pa','c','c','c','q']

    print("tamaño chico", tfc)
    
    tfm = ['rm','e','e','e','-','ac','-','lp','-','sc','mg','shf','-','-','pp','pp','pp','pp','l','l','l','l','-','-','m','m','m','m','h','h','h','h','sh','sh','-','-','mt','pa','pa','pa','pa','c','c','c','q']
        
    print("tamaño mediano", tfm)

    tfg = ['rm','e','e','e','e','-','ac','-','lp','-','sc','mg','shf','-','-','pp','pp','pp','pp','pp','l','l','l','l','l','-','-','m','m','m','m','m','h','h','h','h','h','sh','sh','-','-','mt','pa','pa','pa','pa','pa','c','c','c','q']

    print("tamaño grande", tfg)

    # rescato id ( prio ) , tam , est
    #id
    for i in range(totalfrentes):
        l1.append([])
        for j in range(1):
            l1[i].append(pf[i])
    #tam
    for i in range(totalfrentes):
        l1.append([])
        for j in range(1):
            l1[i].append(tamor[i])
    #estado       
    for i in range(totalfrentes):
        l1.append([])
        for j in range(1):
            if opeor[i] == 'regado_marina':
                l1[i].append('rm')
            if opeor[i] == 'extraccion_marina':
                l1[i].append('e')
            if opeor[i] == 'acuñadura':
                l1[i].append('ac')
            if opeor[i] == 'limpieza_pata':
                l1[i].append('lp')
            if opeor[i] == 'escaner':
                l1[i].append('sc')
            if opeor[i] == 'mapeo_geomecanico':
                l1[i].append('mg')
            if opeor[i] == 'shotcrete_fibra':
                l1[i].append('shf')
            if opeor[i] == 'perforacion_pernos':
                l1[i].append('pp')
            if opeor[i] == 'lechado_pernos':
                l1[i].append('l')
            if opeor[i] == 'instalacion_malla':
                l1[i].append('m')
            if opeor[i] == 'hilteo_malla':
                l1[i].append('h')
            if opeor[i] == 'proyeccion_shotcrete':
                l1[i].append('sh')
            if opeor[i] == 'marcacion_topografica':
                l1[i].append('mt')
            if opeor[i] == 'perforacion_avance':
                l1[i].append('pa')
            if opeor[i] == 'carguio_explosivos':
                l1[i].append('c')
            if opeor[i] == 'tronadura':
                l1[i].append('q')

    # guarda espacios hasta las 9:30

    for i in range(totalfrentes):
        l1.append([])
        for j in range(3):
            l1[i].append('-')

    # selecciona segun tipo

    posi = 0

    for i in range(totalfrentes):
        if (l1[i][1] == 'C'):
            for j in range(1):
                for t in range(40):
                        #busca inicio act con tfc 
                    if (l1[i][2] == tfc[t]):
                        posi = t+1 #siguiente de lista act 
                        break
                for k in range(21):
                    if (k+posi<40):
                        po = k+posi
                        if(tfc[po]!='q'):
                            l1[i].append(tfc[po])   
                        if(tfc[po]== 'q'):
                            indite = k
                    if (k+posi>=40): 
                        if (l1[i][2] != 'q'):
                            num = 21-indite
                            while (num>0):
                                if (num == 1):
                                    l1[i].append('q')
                                if (num !=1):
                                    l1[i].append('-')
                                num = num - 1
                            if (num == 0):
                                break   
                        po = k
                        l1[i].append(tfc[po]) 
                        
    posi = 0

    for i in range(totalfrentes):
        if (l1[i][1] == 'M'):
            for j in range(1):
                for t in range(45):
                    if (l1[i][2] == tfm[t]):
                        posi = t+1
                        break
                for k in range(21):
                    if (k+posi<45):
                        po = k+posi
                        if(tfm[po]!='q'):
                            l1[i].append(tfm[po])
                        if(tfm[po]=='q'):
                            indite = k
                    if (k+posi>=45):
                        if (l1[i][2] != 'q'):
                            num = 21-indite
                            while (num>0):
                                if (num == 1):
                                    l1[i].append('q')
                                if (num !=1):
                                    l1[i].append('-')
                                num = num - 1
                            if (num == 0):
                                break    
                        po = k
                        l1[i].append(tfm[po])

    posi = 0

    for i in range(totalfrentes):
        if (l1[i][1] == 'G'):
            for j in range(1):
                for t in range(51):
                    if (l1[i][2] == tfg[t]):
                        posi = t+1
                        break
                #agrega lista
                for k in range(21):
                    #no es tronadura, ciclo sin terminar
                    if (k+posi<51):
                        po = k+posi
                        if(tfg[po]!='q'):
                            l1[i].append(tfg[po])
                        if(tfg[po]=='q'):
                            indite = k
                    #es tronadura, ciclo terminado
                    if (k+posi>=51):
                        if (l1[i][2] != 'q'):
                            num = 21-indite
                            while (num>0):
                                if (num == 1):
                                    l1[i].append('q')
                                if (num !=1):
                                    l1[i].append('-')
                                num = num - 1
                            if (num == 0):
                                break 
                        po = k
                        l1[i].append(tfg[po])


    #llena la memoria de las listas a los 26 espacios 

    for i in range(totalfrentes):
        aux= len(l1[i])
        for j in range(aux,21):
            l1[i].append('-')

    # imprimir matiz

    print("[ ID - TAM - EST -08:00-08:30-09:00-09:30-10:00-10:30-11:00-11:30-12:00-12:30-13:00-13:30-14:00-14:30-15:00-15:30-16:00-16:30-17:00-17:30-18:00-18:30-19:00-19:30]")
    
    for i in range(totalfrentes):
        print(l1[i],len(l1[i]))


    # Restriccion recursos

    l2 = []
    #id
    for i in range(totalfrentes):
        l2.append([])
        for j in range(1):
            l2[i].append(pf[i])
    #tam
    for i in range(totalfrentes):
        l2.append([])
        for j in range(1):
            l2[i].append(tamor[i])
    #estado        
    for i in range(totalfrentes):
        l2.append([])
        for j in range(1):
            if opeor[i] == 'regado_marina':
                l2[i].append('rm')
            if opeor[i] == 'extraccion_marina':
                l2[i].append('e')
            if opeor[i] == 'acuñadura':
                l2[i].append('ac')
            if opeor[i] == 'limpieza_pata':
                l2[i].append('lp')
            if opeor[i] == 'escaner':
                l2[i].append('sc')
            if opeor[i] == 'mapeo_geomecanico':
                l2[i].append('mg')
            if opeor[i] == 'shotcrete_fibra':
                l2[i].append('shf')
            if opeor[i] == 'perforacion_pernos':
                l2[i].append('pp')
            if opeor[i] == 'lechado_pernos':
                l2[i].append('l')
            if opeor[i] == 'instalacion_malla':
                l2[i].append('m')
            if opeor[i] == 'hilteo_malla':
                l2[i].append('h')
            if opeor[i] == 'proyeccion_shotcrete':
                l2[i].append('sh')
            if opeor[i] == 'marcacion_topografica':
                l2[i].append('mt')
            if opeor[i] == 'perforacion_avance':
                l2[i].append('pa')
            if opeor[i] == 'carguio_explosivos':
                l2[i].append('c')
            if opeor[i] == 'tronadura':
                l2[i].append('q')

    # guarda espacios hasta las 9:30

    for i in range(totalfrentes):
        l2.append([])
        for j in range(3):
            l2[i].append('-')

    # ordena restringiendo recursos

    # llena primer frente para comparar
    
    #aqui parte 
    for i in range(1):
        for j in range(6,27):
            aux = l1[i][j]
            l2[i].append(aux)

    # compara 

    #recorre frentes
    for i in range(totalfrentes):
        contador = 0
        #recorre posicion en la tabla 
        for j in range(6,27):
            #bloqueo vertical
            if(i+1>=totalfrentes):
                break
            f2 = l1[i+1][j-contador]
            contador2 = 0
            bandera = 0
            #compara vertical
            while (i-contador2>=0):
                f1 = l2[i-contador2][j]
                if(f2!=f1):
                    bandera = bandera
                    if (f2=='rm' and f1=='l') or (f1=='rm' and f2=='l'): # restringe recurso cuadrilla
                        bandera = bandera + 1
                    if (f2=='rm' and f1=='m') or (f1=='rm' and f2=='m') :
                        bandera = bandera + 1
                    if (f2=='rm' and f1=='h') or (f1=='rm' and f2=='h'):
                        bandera = bandera + 1
                    if (f2=='rm' and f1=='c') or (f1=='rm' and f2=='c'):
                        bandera = bandera + 1
                    if (f2=='l' and f1=='m') or (f1=='l' and f2=='m'):
                        bandera = bandera + 1
                    if (f2=='l' and f1=='h') or (f1=='l' and f2=='h'):
                        bandera = bandera + 1
                    if (f2=='l' and f1=='c') or (f1=='l' and f2=='c'):
                        bandera = bandera + 1
                    if (f2=='m' and f1=='h') or (f1=='m' and f2=='h'):
                        bandera = bandera + 1
                    if (f2=='m' and f1=='c') or (f1=='m' and f2=='c'):
                        bandera = bandera + 1
                    if (f2=='h' and f1=='c') or (f1=='h' and f2=='c'):
                        bandera = bandera + 1
                    if (f2=='e' and f1=='lp') or (f1=='e' and f2=='lp'): # restringe recurso LHD
                        bandera = bandera + 1
                    if (f2=='sc' and f1=='mg') or (f1=='sc' and f2=='mg'): # restringe recurso topografo
                        bandera = bandera + 1
                    if (f2=='sc' and f1=='mt') or (f1=='sc' and f2=='mt'):
                        bandera = bandera + 1
                    if (f2=='mg' and f1=='mt') or (f1=='mg' and f2=='mt'):
                        bandera = bandera + 1
                    if (f2=='shf' and f1=='sh') or (f1=='shf' and f2=='sh'): # restringe recurso roboshot
                        bandera = bandera + 1
                    if (f2=='pp' and f1=='pa') or (f1=='pp' and f2=='pa'): # restringe recurso jumbo
                        bandera = bandera + 1

                if f2=='-' and f1=='-':
                    bandera = bandera
                if f2==f1 and f2!='-':
                    bandera = bandera + 1
                contador2 = contador2 + 1
            if (bandera==0):
                l2[i+1].append(f2)
            if (bandera>0):
                l2[i+1].append('-')
                contador = contador + 1

                    
                    
    # imprimir matiz recursos

    print("ASIGNACION DE RECURSOS auxiliar")
    print("[ ID - TAM - EST -08:00-08:30-09:00-09:30-10:00-10:30-11:00-11:30-12:00-12:30-13:00-13:30-14:00-14:30-15:00-15:30-16:00-16:30-17:00-17:30-18:00-18:30-19:00-19:30]")
    
    for i in range(totalfrentes):
        print(l2[i],len(l2[i]))


    def ventanamatriz():
        win4 = Tk()
        win4.geometry('1080x200')
        frame = Frame(win4)
        frame.pack()
        extra = ['id','tam','est','08:00','08:30','09:00','09:30','10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30','18:00','18:30','19:00','19:30']
        for uwu in range(0,27):
            j = Entry(frame,width=5)
            j.grid(row = 0, column = uwu)
            j.insert(END,extra[uwu])


        for f in range(0,len(l2)):
                    for j in range(0,len(l2[f])):
                            x = Entry(frame,width=5)
                            x.grid(row = f+1, column = j)
                            x.insert(END,l2[f][j])


    def insertarestadofrentesbd():

         win4=Tk()
         win4.geometry('300x200')
         frame= Frame(win4)
         frame.pack()
         
         txtoperacion = Label(frame,text='operacion')
         txtoperacion.grid(row='0',column='0')

         txtestadoavance = Label(frame,text='estado avance')
         txtestadoavance.grid(row='1',column='0')

         txtobservaciones = Label(frame,text='observaciones')
         txtobservaciones.grid(row='2',column='0')

         txtfecha = Label(frame,text='fecha')
         txtfecha.grid(row='3',column='0')

         txtcriticidad = Label(frame,text='criticidad')
         txtcriticidad.grid(row='4',column='0')

         txtdireccion = Label(frame,text='direccion')
         txtdireccion.grid(row='5',column='0')

         txtidfrente = Label(frame,text='id frente')
         txtidfrente.grid(row='6',column='0')

    botonEstadofrentes = Button(framemain,text="VER FRENTES ASOCIADOS AL RUT",command=verfrentesrut)
    botonEstadofrentes.grid(row="4", column="1")

    botonEstadoEquipos= Button(framemain,text="VER RECURSO EQUIPOS",command=vereequipos)
    botonEstadoEquipos.grid(row="5", column="1")

    botonEstadoservicios= Button(framemain,text="ESTADO SERVICIOS",command=verestadoservicios)
    botonEstadoservicios.grid(row="6", column="1") 

    botonavances= Button(framemain,text="AVANCES",command=veravances)
    botonavances.grid(row="7", column="1") 

    botonverestadofrentes = Button(framemain,text="ESTADO FRENTES", command=estadofrentes)
    botonverestadofrentes.grid(row="8", column="1")

    botonverestadoequipos = Button(framemain,text="VER ESTADO EQUIPOS",command=verestadoequipos)
    botonverestadoequipos.grid(row="9", column="1")

    insertarestadofrentes = Button(framemain,text='INPUT ESTADO FRENTES',command=insertarestadofrentesbd)
    insertarestadofrentes.grid(row='11',column="1")

    vermatriz = Button(framemain,text='VER MATRIZ ',command=ventanamatriz)
    vermatriz.grid(row='12',column="1")


def botoningresar():
    #ingresomain()
    
    #selecciona la data a comparar
    rut = entryuser.get()
    password = entrypass.get()
    cursor = bd9.cursor()
    sql =  "SELECT rut,contraseña,codigo_empresa from usuarios"

    try: 
        cursor.execute(sql)
        data = cursor.fetchall()
        
    except Exception as e :
        print("exception : ")
    bd9.commit()
    cursor.close()
    bd9.close()
    #captura mi rut y mi contraseña 
    for i in data:
        k=i['codigo_empresa']
        j=i['contraseña']
        i=i['rut']

        if(i==rut):
            win.destroy()
            if(j==password):
                ingresomain(k)


def botonregistrar():
    win2=Tk()
    frameingresar=Frame(win2)
    frameingresar.pack()

    txtrut=Label(frameingresar,text="Rut")
    txtrut.grid(row="1", column="0")
    entryrut=Entry(frameingresar)
    entryrut.grid(row="1",column="1")
    txtpass=Label(frameingresar,text="Contraseña")
    txtpass.grid(row="2", column="0")
    entrypass=Entry(frameingresar)
    entrypass.grid(row="2",column="1")

    txtcpro=Label(frameingresar,text="Codigo empresa")
    txtcpro.grid(row="3", column="0")
    entrycpro=Entry(frameingresar)
    entrycpro.grid(row="3",column="1")


    def addbdusuario():
        rut = entryrut.get()
        password = entrypass.get()
        codigo = entrycpro.get()
        cursor=bd10.cursor()
        sql =  "insert into usuarios (Rut,Contraseña,Codigo_empresa) value('%s','%s','%s')" % (rut,password,codigo)
        try:
         cursor.execute(sql)
         cursor.close()
         bd10.commit()
         bd10.close()
        except Exception as e:
         print(e)
        #bd.commit()
        #cursor.close()
        #bd.close()
        win2.destroy()
        
    botonbd=Button(frameingresar,text="add bd",command=addbdusuario)
    botonbd.grid(row="4",column="1")


win=Tk() #ventanalogin
win.title("CAVES IA")
frame1=Frame(win)
frame1.pack()


#----SECCION LOGIN ----
imagen=tkinter.PhotoImage(file="icon login.png")
pimagen=Label(frame1,image=imagen).pack(side=LEFT)
txtuser=Label(frame1, text="Nombre de usuario:")
txtuser.pack()
entryuser=Entry(frame1)
entryuser.pack()
txtpass=Label(frame1, text="Contraseña")
txtpass.pack()
entrypass=Entry(frame1, show="*")
entrypass.pack()
botoningresarr=Button(frame1, text="Ingresar",command=botoningresar) #boton login
botonregistrarr=Button(frame1,text="Registrar",command=botonregistrar)
botoningresarr.pack()
botonregistrarr.pack()
win.mainloop()