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
from numpy import can_cast, mat, matrix
from pkg_resources import PathMetadata 
import pymysql.cursors
import numpy as np

#ciclos mineros 
ciclominero1 = ['regado_marina','extraccion_marina','acuñadura','limpieza_pata','escaner','mapeo_geomecanico',
'shotcrete_fibra','perforacion_pernos','lechado_pernos','instalacion_malla','hilteo_malla','proyeccion_shotcrete',
'marcacion_topografica','perforacion_avance','carguio_explosivos','tronadura']
discriminados = []
discriminados.append(list())
discriminados.append(list())
discriminados.append(list())
discriminados.append(list())



#memoria algoritmo priorizacion 
ptipo = []
psiglas = []
pnumeros = []
pdireccion = []
pestado = []
ptam = []
pruta = []
pdistancia = [] 
pnivel = []
pmacrobloque = []
pid = []
pcodigo = [] 
psector = []
pref = []
pdirref = []
frentesord = []
for i in range(14):
    frentesord.append(list())

pop = []
pestadoavance =[]
pobs = []
pfecha =[]
pcriticidad =[]
pdirestadofr =[]
pidestadofr =[]
pestadosfrentes = []
for j in range(7):
    pestadosfrentes.append(list())

priorizacion = []
priorizacion.append(list())
priorizacion.append(list())
priorizacion.append(list())
priorizacion.append(list())

priorizacion2 = []
priorizacion2.append(list())
priorizacion2.append(list())
priorizacion2.append(list())
priorizacion2.append(list())

priorizacion3 = []
priorizacion3.append(list())

priorizacion4 = []
priorizacion4.append(list())
priorizacion4.append(list())
priorizacion4.append(list())
priorizacion4.append(list())
priorizacion4.append(list())
tamyfrentes = []
tamyfrentes.append(list())
tamyfrentes.append(list())




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

#memoria algoritmo 2 
matrizpriorizacion = []
print(matrizpriorizacion)
basematriz = []
basematriz.append('id(s)')
basematriz.append('08:00')
basematriz.append('08:30')
basematriz.append('09:00')
basematriz.append('09:30')
basematriz.append('10:00')
basematriz.append('10:30')
basematriz.append('11:00')
basematriz.append('11:30')
basematriz.append('12:00')
basematriz.append('12:30')
basematriz.append('13:00')
basematriz.append('13:30')
basematriz.append('14:00')
basematriz.append('14:30')
basematriz.append('15:00')
basematriz.append('15:30')
basematriz.append('16:00')
basematriz.append('16:30')
basematriz.append('17:00')
basematriz.append('17:30')
basematriz.append('18:00')
basematriz.append('18:30')
basematriz.append('19:00')
basematriz.append('19:30')
siglarecursos = ['RM','E','AC','LP','SC','MG','SHF','PP','L','M','H','SH','MT','PA','C','Q']
tams = ['1','3','1','1','1','1','1','3','3','3','3','2','1','3','3','1']
tameme = ['1','3','1','1','1','1','1','4','4','4','4','2','1','4','3','1']
taml = ['1','4','1','1','1','1','1','5','5','5','5','2','1','3','1']
memalg2 = []
memalg2.append(siglarecursos)
memalg2.append(tams)
memalg2.append(tameme)
memalg2.append(taml)





matrizpriorizacion.append(basematriz)







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

    ''' txtsigla=Label(frameingreso,text="Sigla de referencia")
    txtsigla.grid(row="2",column="0")
    entrysigla= ttk.Combobox(frameingreso)
    entrysigla.grid(row="2",column="1")
    entrysigla['values'] = ('CAB','CAL','ZA','FRI','FRE')'''
  

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
        
# algoritmo 1

    
    cursor=bd13.cursor()
    totalfrentes = cursor.execute("select * from frentes")
    print("TOTAL FRENTES")
    print(totalfrentes)


# Definir listas para priorizacion

# ruta critica ( las que si tienen primero)

    print("RUTA CRITICA")
    rutacri = []
    cursor.execute("select id_frente from frentes where ruta_critica = 'si'")
    resusi = cursor.fetchall()
    print ("SI")
    for x in resusi:
        rutacri.append(x)
        print(x)
    cursor.execute("select id_frente from frentes where ruta_critica = 'no'")
    resuno = cursor.fetchall()
    print ("NO")
    for y in resuno:
        rutacri.append(y)
        print(y)
    print("RUTA CRITICA")
    print(rutacri)
    

# urgencia (la que tenga mas metros por hacer primero)

    print("URGENCIA")
    urgencia = []
    cursor.execute("select id_frente from estado_frentes order by estado_avance desc")
    mari = cursor.fetchall()
    for z in mari:
        urgencia.append(z)
        print (z)
    print("URGENCIA")
    print(urgencia)

# tronadura proxima ( cual esta mas proxima a tronadura primero ) ***
    
    print("TRONADURA PROXIMA")
    tropro = []
    tropra = []
    idtrop = []
    
    cursor.execute("select id_frente,operacion from estado_frentes")
    trop = cursor.fetchall()

    print('aqui abajo es :')
    
    for tropa in trop:
        fren = tropa['id_frente']
        opera = tropa['operacion']
        for esq in ciclominero1:
            if(esq==opera):
                aux = ciclominero1.index(esq)
                tropra.append(aux)
                idtrop.append(fren)
    tamtopra = len(tropra)-1
    for la in range(0,tamtopra):
        for le in range(0,tamtopra):
            if(tropra[le]<tropra[le+1]):
                        auxtropra=tropra[le]
                        auxfrente=idtrop[le]

                        tropra[le]=tropra[le+1]
                        idtrop[le]=idtrop[le+1]

                        tropra[le+1]=auxtropra  
                        idtrop[le+1]=auxfrente


    print(tropra,idtrop)






    

# foco ( definido por el usuario previa la primera priorizacion )

    print("FOCO")
    foco = []
    cursor.execute("select id_frente from frentes")
    foc = cursor.fetchall()
    for b in foc:
        foco.append(b)
        print (b)
    print(foco)

# extraccion marina ( la termino en en tronadura primero ) ***

    num=1
    extra = []
    for i in range(totalfrentes):
        extra.append(num)
        num=num+1
    print("EXTRACCION MARINA")
    cursor.execute("select id_frente,operacion from estado_frentes")
    marp = cursor.fetchall()
    for c in marp:
        print (c)
    print(extra)

# distancia a pique ( la que tenga mayor distancia marina primero)

    print("DISTANCIA A PIQUE")
    dista = []
    cursor.execute("select id_frente from frentes order by distancia_marina desc")
    marip = cursor.fetchall()
    for d in marip:
        dista.append(d)
        print (d)
    print(dista)


# priorizacion final

    print("PRIORIZACION")
    prio = [[],
            [],
            [],
            [],
            [],
            []]

    for j in range(totalfrentes):
        prio[0].append(rutacri[j])
    
    for j in range(totalfrentes):
        prio[1].append(urgencia[j])
    
    for j in range(totalfrentes):
        prio[2].append(tropra[j])

    for j in range(totalfrentes):
        prio[3].append(foco[j])

    for j in range(totalfrentes):
        prio[4].append(extra[j])

    for j in range(totalfrentes):
        prio[5].append(dista[j])


    print("PRIORIZACION")

    print(prio[0])
    print(prio[1])
    print(prio[2])
    print(prio[3])
    print(prio[4])
    print(prio[5])

        

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

    


	   

    def priorizarfrentes():
        num = 0
        cursor = bd10.cursor()
        sql2 = 'select * from estado_frentes'
        sql = 'select  * from frentes'
        try:
            cursor.execute(sql)
            dataa = cursor.fetchall()
            
            cursor.execute(sql2)
            dataestado = cursor.fetchall()
            cursor.close()
            bd10.commit()
            bd10.close()
            for j in dataestado:
                operacion = j['operacion']
                estado_avance = j['estado_avance']
                obs = j['observaciones']
                fecha = j['fecha']
                criticidad = j['criticidad']
                direccionestado = j['direccion']
                id_frente = j['id_frente']
                pop.append(operacion)
                pestadoavance.append(estado_avance)
                pobs.append(obs)
                pfecha.append(fecha)
                pcriticidad.append(criticidad)
                pdirestadofr.append(direccionestado)
                pidestadofr.append(id_frente)
            for l in range(6):
                match l :
                    case 0:
                        pestadosfrentes[0].append(pop)
                    case 1:
                        pestadosfrentes[1].append(pestadoavance)
                    case 2:
                        pestadosfrentes[2].append(pobs)
                    case 3:
                        pestadosfrentes[3].append(fecha)
                    case 4:
                        pestadosfrentes[4].append(pcriticidad)
                    case 5:
                        pestadosfrentes[5].append(pdirestadofr)
                    case 6:
                        pestadosfrentes[6].append(pidestadofr)
            
           
            for i in dataa:
                codigo = i['codigo_empresa']
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
                    num = num+1
                    ptipo.append(tipo)
                    psiglas.append(sigla)
                    pnumeros.append(numero)
                    pref.append(numeroreferencia)
                    pdireccion.append(direccion)
                    pdirref.append(direccionreferencia)
                    pestado.append(estado)
                    ptam.append(tamaño)
                    pruta.append(ruta)
                    pdistancia.append(distancia)
                    pnivel.append(nivel)
                    pmacrobloque.append(macrobloque)
                    psector.append(sectores)
                    pid.append(id)
                    pcodigo.append(codigo)
            
            for k in range(14):
                match k :
                    case 0:
                        frentesord[0].append(ptipo)
                    case 1:
                        frentesord[1].append(psiglas)
                    case 2:
                        frentesord[2].append(pnumeros)
                    case 3:
                        frentesord[3].append(pdireccion)
                    case 4:
                        frentesord[4].append(pestado)
                    case 5:
                        frentesord[5].append(ptam)
                    case 6:
                        frentesord[6].append(pruta)
                    case 7:
                        frentesord[7].append(pdistancia)
                    case 8:
                        frentesord[8].append(pnivel)
                    case 9:
                        frentesord[9].append(pmacrobloque)
                    case 10:
                        frentesord[10].append(pid)
                    case 11:
                        frentesord[11].append(pcodigo)
                    case 12:
                        frentesord[12].append(psector)
                    case 13:
                        frentesord[13].append(pref)
                    case 14:
                        frentesord[14].append(pdirref)
            aux = int(0)
            aux2 = int(0)

            #inserta los indices de tronadura en la primera priorizacion y tronadura en la columna 3 

            for p in pop:
                if(p=='tronadura'):
                    priorizacion[0].append(aux)
                    priorizacion[2].append(p)
                    aux=aux+1
                else:
                    discriminados[0].append(p)
                    discriminados[1].append(aux)
                    aux=aux+1
            #inserta id frentes en priorizacion y id frentes en discriminados 
            for u in pidestadofr:
                aux2 = pidestadofr.index(u)
                aux45 = pidestadofr.index(u)
                for d in priorizacion[0]:
                    if(d==aux2):
                        priorizacion[1].append(u)
                for t in discriminados[1]:
                    if(t==aux45):
                        discriminados[2].append(u)
            #aqui se inserta la distancia marina 
            for w in pdistancia:
                aux3=pdistancia.index(w)
                for d in priorizacion[0]:
                    if(d==aux3):
                        priorizacion[3].append(w)
            print('priorizacion 1:(extraccion marina)')     
            print (priorizacion[1])
            #aqui se ordena segun la distancia marina 
            tam=len(priorizacion[3])-1
            #para guardar la memoria 
            auxp3=[]
            for tr in priorizacion[3]:
                auxp3.append(tr) 
           #ordena p3 3 orden mayor a menor d marina
            for u in range(0,tam):
                for q in range(0,tam):
                    if(priorizacion[3][q]<priorizacion[3][q+1]):
                        aux4=priorizacion[3][q]
                        priorizacion[3][q]=priorizacion[3][q+1]
                        priorizacion[3][q+1]=aux4
            #ordena indices en priorizacion 2[0]
            aux5=int(0)
            for jaja in priorizacion[3]:
                for xd in auxp3:
                    aux5=aux5+1
                    if(xd==jaja):
                        priorizacion2[0].append(aux5)
                        priorizacion2[3].append(jaja)
                aux5 =0
            #inserta tronadura 
            aux6=len(priorizacion2[0])
            for uwu in range(0,aux6):
                priorizacion2[2].append('tronadura')

            
            for wak  in priorizacion2[0]:
                for fro in priorizacion[1]:
                    if(wak==priorizacion[1].index(fro)+1):
                        priorizacion2[1].append(fro)
            
            for caca in discriminados[0]:
                auxd = int(0)
                for cece in ciclominero1:
                    if(caca==cece):
                        discriminados[3].append(auxd+1)
                    else: 
                        auxd = auxd+1
            #ordena frentes restantes 
            aux7 = len(discriminados[3])
            aux8 = len(discriminados[2])
            tammm = len(discriminados[3])-1
            for oeo in range(0,tammm):
                for eoe in range(0,tammm):
                    if(discriminados[3][eoe]<discriminados[3][eoe+1]):
                        aux7=discriminados[3][eoe]
                        aux8=discriminados[2][eoe]
                        discriminados[3][eoe]=discriminados[3][eoe+1]
                        discriminados[2][eoe]=discriminados[2][eoe+1]
                        discriminados[3][eoe+1]=aux7
                        discriminados[2][eoe+1]=aux8

            priorizacion3[0]= priorizacion2[1]+discriminados[2]
            
            print('priorizacion 2 (distancia de pv):')      
            print(priorizacion2[1])
            print('priorizacion 3 (tronadura proxima ):') 
            print(priorizacion3[0])
            priorizacion4[0] = priorizacion2 [1]
            priorizacion4[1] = discriminados [2]
            

            tamxd = len(priorizacion4[1])
            tamxd2 = len(pid)
            tamxd3 = len(priorizacion4[1])-1
            aux9=int(0)

            for waca in range(0,tamxd):
                miaux = priorizacion4[1][waca]
                for weke in range (0,tamxd2):
                    miaux2 = pid[weke]
                    miaux3 = ptam[weke]
                    if(miaux==miaux2):
                        priorizacion4[2].append(miaux3)
            tamxd3 = len(priorizacion4[2])
            for orden in range (0,tamxd3):
                if(priorizacion4[2][orden]=='G'):
                    aux777 = priorizacion4[1][orden]
                    priorizacion4[3].append(aux777)
            for orden1 in range (0,tamxd3):
                if(priorizacion4[2][orden1]=='M'):
                    aux777 = priorizacion4[1][orden1]
                    priorizacion4[3].append(aux777)
            for orden2 in range (0,tamxd3):
                if(priorizacion4[2][orden2]=='C'):
                    aux777 = priorizacion4[1][orden2]
                    priorizacion4[3].append(aux777)
            
            priorizacion4[4]=priorizacion4[0]+priorizacion4[3]
            print('priorizacion 4 (Urgencia ):')
            print(priorizacion4)
            

            tamyfrentes[0]=priorizacion4[4]
            for jajant in frentesord[10][0]:
                for yapo in tamyfrentes[0]:
                    auxjajant = tamyfrentes[0].index(yapo)
                    if(jajant==yapo):
                        
                        busqueda =frentesord[5][0][auxjajant]
                        tamyfrentes[1].append(busqueda)
            print(tamyfrentes[1])
          
            #aqui se muestra data segun la priorizacion que se desee 
     
        except Exception as e:
            print('exception :',e)
       
        
     
            
                
        

        
        

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


    def algoritmo2():
        
        numlistasmatrix = len(priorizacion4[4])
        #define memoria para el numero de frentes
        for matrizlargo in range (0,numlistasmatrix):
            matrizpriorizacion.append(list())
        #inserta frentes en la columna íd (0)
        setid = len(matrizpriorizacion)+1    
        for i in range(1,setid-1):
            aux1 = priorizacion4[4][i-1]
            matrizpriorizacion[i].append(aux1)
        #llenar memoria con 0s de 8 a 9:30 y de 18:30 a 19:30
        tamcolumnas = len(matrizpriorizacion[0])
        tamfilas = len(matrizpriorizacion)
        for j in range(1,tamfilas):
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            matrizpriorizacion[j].append('0')
            #inserto tronadura en los frentes correspondientes
        tamtrondadura = len(priorizacion2[1])
        for k in range (1,tamtrondadura+1):
            for l in range(1,tamcolumnas):
                if(k==l):
                    matrizpriorizacion[k][l+3]='RM'
        #funcion para saber que tam es el frente 
        def quetames(frente):
            auxtamanio = len(tamyfrentes[0])
            for frentes in range(0,auxtamanio):
                if (tamyfrentes[0][frentes]==frente):
                    return(tamyfrentes[1][frentes])

        #se inserta el ciclo siguiente segun tam de frente para los frentes que terminaron el tronadura 
        auxtamfrentes = len(matrizpriorizacion)
        auxcolumnas = len(matrizpriorizacion[0])-1
        print(auxtamfrentes)
        for eme in range(1,auxtamfrentes):
            for caca in range(1,auxcolumnas):
                if(matrizpriorizacion[eme][caca]=='RM'):
                    frente = matrizpriorizacion[eme][0]
                    tamanio = quetames(frente)
                    match tamanio :
                        case 'C':
                            print('C')
                        case 'M':
                            print('M')
                        case 'G':
                            print('G')
                            #QUE LO BUSQUE EN SU RESPECTIVA LISTA E INSERTE LAS WEAS         
        
    
  
        def vermatrizconsola():
            for uwu in range (0,tamfilas):
                print ('\n')
                print (matrizpriorizacion[uwu])
        vermatrizconsola()
        
        
        
        

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

    algoritmopriorizacion = Button(framemain,text='Priorizacion',command=priorizarfrentes)
    algoritmopriorizacion.grid(row='10', column='1')

    insertarestadofrentes = Button(framemain,text='INPUT ESTADO FRENTES',command=insertarestadofrentesbd)
    insertarestadofrentes.grid(row='11',column="1")

    botonalgoritmo2 = Button(framemain,text='Algoritmo 2',command=algoritmo2)
    botonalgoritmo2.grid(row='12',column='1')


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
