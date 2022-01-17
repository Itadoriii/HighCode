from ast import Index
from email.headerregistry import SingleAddressHeader
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter
from tkinter.font import BOLD
from unittest import signals 
import pymysql.cursors

#memoria para mostrar tablas 
tipos =[]
tipos.append('tipo')
siglas = []
siglas.append('sigla')
numeros = []
numeros.append('numero')
direcciones = []
direcciones.append('direccion')
estados = []
estados.append('direccion')
tamanios= []
tamanios.append('tamaño')
rutas  = []
rutas.append('ruta')
distancias = []
distancias.append('distancia')
niveles = []
niveles.append('nivel')
macrobloques = []
macrobloques.append('macrobloque')
ides= []
ides.append('id')
#memoria para mostrar equipos 

#memoria para mostrar avances 
frentesid = []
frentesid.append('id_frente')


#coneccion bd red local para crear cursores
bd = pymysql.connect(host='localhost',
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


def addbdfrentes():
    win4=Tk()
    win4.geometry('300x300')
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

    txtdireccion=Label(frameingreso,text="Direccion")
    txtdireccion.grid(row="4",column="0")
    entrydireccion= ttk.Combobox(frameingreso)
    entrydireccion.grid(row="4",column="1")
    entrydireccion['values'] = ('N','S','E','O')

    txtestado=Label(frameingreso,text="Estado")
    txtestado.grid(row="5",column="0")
    entryestado= ttk.Combobox(frameingreso)
    entryestado.grid(row="5",column="1")
    entryestado['values'] = ('Activo','Inactivo')

    txttamaño =Label(frameingreso,text="Tamaño")
    txttamaño.grid(row="6",column="0")
    entrytamaño= Entry(frameingreso)
    entrytamaño.grid(row="6",column="1")

    txtrutacritica=Label(frameingreso,text="Ruta critica")
    txtrutacritica.grid(row="7",column="0")
    entryrutacritica= ttk.Combobox(frameingreso)
    entryrutacritica.grid(row="7",column="1")
    entryrutacritica['values'] = ('N','S','E','O')

    txtdistanciamarina=Label(frameingreso,text="Distancia Marina")
    txtdistanciamarina.grid(row="8",column="0")
    entrydistanciamarina= Entry(frameingreso)
    entrydistanciamarina.grid(row="8",column="1")

    txtnivelfrente=Label(frameingreso,text="Nivel")
    txtnivelfrente.grid(row="9",column="0")
    entrynivelfrente= ttk.Combobox(frameingreso)
    entrynivelfrente.grid(row="9",column="1")
    entrynivelfrente['values'] = ('PD','HD','INY','EXT','CH')

    txtmacrobloque=Label(frameingreso,text="Macrobloque")
    txtmacrobloque.grid(row="10",column="0")
    entrymacrobloque= Entry(frameingreso)
    entrymacrobloque.grid(row="10",column="1")

    txtcodigo=Label(frameingreso,text="Codigo")
    txtcodigo.grid(row="11",column="0")
    entrycodigo= Entry(frameingreso)
    entrycodigo.grid(row="11",column="1")

    def llenarfrente():
        tipo =entrytipo.get()
        sigla = entrysigla.get()
        numero = entrynumero.get()
        direccion = entrydireccion.get()
        estado =entryestado.get()
        tamaño = entrytamaño.get()
        ruta =entryrutacritica.get()
        distancia =entrydistanciamarina.get()
        nivel = entrynivelfrente.get() 
        macrobloque =entrymacrobloque.get()
        id = entryid.get()
        codigoempresa = entrycodigo.get()
        cursor=bd3.cursor()
        sql =  "insert into frentes(tipo,sigla,numero,direccion,estado,tamaño,ruta_critica,distancia_marina,nivel,macrobloque,id_frente,codigo_empresa) value('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (tipo,sigla,numero,direccion,estado,tamaño,ruta,distancia,nivel,macrobloque,id,codigoempresa)
        try:
         cursor.execute(sql)
         print (sql)
         cursor.close()
         bd3.commit()
         bd3.close()
        except Exception as e:
            print("exception : ")
            
       # cursor.close()
        #bd.commit()
       # bd.close()
    
        win4.destroy()

    botonllenarbd=Button(frameingreso,text="Añadir a la Bd",command=llenarfrente)
    botonllenarbd.grid(row="12")

def addequipo():
    win4=Tk()
    frameingreso = Frame(win4)
    frameingreso.pack()

    def llenarequipo():
        flota= entryflota.get()
        codigo = entrycod.get()
       
        cursor=bd2.cursor()
        sql =  "insert into equipos(flota,codigo_equipo) value('%s','%s')" % (flota,codigo)
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





    txtflota =Label(frameingreso,text="ID")
    txtflota.grid(row="0",column="0")
    entryflota = Entry(frameingreso)
    entryflota.grid(row="0",column="1")

    txtcodigo=Label(frameingreso,text="Avance")
    txtcodigo.grid(row="1",column="0")
    entrycod= Entry(frameingreso)
    entrycod.grid(row="1",column="1")

    

    botonllenarbd=Button(frameingreso,text="Añadir a la Bd",command=llenarequipo)
    botonllenarbd.grid(row="2")

  


    


def ingresomain(rut):
    rutt=rut
    win3 = Tk()
    win3.config(bg="lightblue")
    win3.geometry('600x400')
    framemain = Frame(win3)
    framemain.config(bg="blue",width=480,height=320,relief="sunken")
    framemain.pack()
    

    botonFrentes = Button(framemain,text="CREAR NUEVO FRENTE",command=addbdfrentes)
    botonFrentes.grid(row="2", column="1")

    botonTopografia = Button(framemain,text="CREAR NUEVO EQUIPO",command=addequipo)
    botonTopografia.grid(row="3", column="1")

    def verfrentesrut():
        numfilas = 1
        numcolumnas = 12
        win3.destroy()
        win4 = Tk()
        tabla=Frame(win4)
        tabla.pack()
        def creartablafrentes():
               for f in range(numfilas):
                    for j in range(numcolumnas):
                            x = Entry(tabla)
                            x.grid(row = f, column = j)
                            if (j==1):
                                x.insert(END,tipos[f])
                            if (j==2):
                                x.insert(END,siglas[f])
                            if (j==3):
                                x.insert(END,numeros[f])
                            if (j==4):
                                x.insert(END,direcciones[f])
                            if (j==5):
                                x.insert(END,estados[f])
                            if (j==6):
                                x.insert(END,tamanios[f])
                            if (j==7):
                                x.insert(END,rutas[f])
                            if (j==8):
                                x.insert(END,distancias[f])
                            if (j==9):
                                x.insert(END,niveles[f])
                            if (j==10):
                                x.insert(END,macrobloques[f])
                            if (j==11):
                             x.insert(END,ides[f])
                        
                        
        cursor = bd2.cursor()
        cursor2 =  bd2.cursor()
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
                direccion = i['direccion']
                estado = i['estado']
                tamaño = i['tamaño']
                ruta = i['ruta_critica']
                distancia = i['distancia_marina']
                nivel = i['nivel']
                macrobloque = i['macrobloque']
                id = i['id_frente']
                codigo=i['codigo_empresa']
                if(codigo==rutt):
                    tipos.append(tipo)
                    siglas.append(sigla)
                    numeros.append(numero)
                    direcciones.append(direccion)
                    estados.append(estado)
                    tamanios.append(tamaño)
                    rutas.append(ruta)
                    distancias.append(distancia)
                    niveles.append(nivel)
                    macrobloques.append(macrobloque)
                    ides.append(id)
            cursor.close()
            bd2.commit()
            bd2.close
        except Exception as e:
            print(e)
        creartablafrentes()

        


    def vereequipos():
        win3.destroy()
        win4 = Tk()
        tabla = Frame(win4)
        tabla.pack()
        cursor = bd3.cursor()
    
        sql =  "SELECT * from equipos"
        try: 
            cursor.execute(sql)
            data = cursor.fetchall()
            cursor.close()
            bd3.commit()
            bd3.close()
        except Exception as e :
             print("exception : ")

        numfilas=len(data)
        print(numfilas)
        numcolumnas = 2
        for i in range(numfilas):
            for j in range (numcolumnas):
                x = Entry(tabla)
                x.grid(row = i, column = j)
                x.insert(0,'holaxd')

        #bd.commit()
        #cursor.close()
        #bd.close()'''
        



    def verestadoservicios():
        win3.destroy()
        cursor = bd.cursor()
        sql =  "SELECT * from estado_servicios"
        try: 
            cursor.execute(sql)
            data = cursor.fetchall()
            print(data)
            cursor.close()
            bd.commit()
            bd.close()
        except Exception as e :
         print("exception : ",e )
    #bd.commit()
    #cursor.close()
    #bd.close()'''

    def favances():
        columnas = 8
        numfilas = 1 
        win3.destroy()
        win4 = Tk()
        tabla=Frame(win4)
        tabla.pack()
        def creartablaavances():
            print('avances')
            #programar tabla aqui xd 
            for i in range(numfilas):
                for j in range (columnas):
                    x = Entry(tabla)
                    x.grid(row = i, column = j)
                    if(j==1):
                        x.insert(END,frentesid[i])

        cursor = bd3.cursor()
        sql =  "SELECT * from frentes "
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            cursor.close()
            for p in data:
                codigo=p['codigo_empresa']
                if (codigo==rutt):
                    numfilas = numfilas + 1
                    frenteid = p['id_frente']
                    frentesid.append(frenteid)

        except Exception as e :
            print(e)
        creartablaavances()


        
        

    botonEstadofrentes = Button(framemain,text="VER FRENTES ASOCIADOS AL RUT",command=verfrentesrut)
    botonEstadofrentes.grid(row="4", column="1")

    botonEstadoEquipos= Button(framemain,text="VER EQUIPOS EQUIPOS",command=vereequipos)
    botonEstadoEquipos.grid(row="5", column="1")

    botonEstadoservicios= Button(framemain,text="ESTADO SERVICIOS",command=verestadoservicios)
    botonEstadoservicios.grid(row="6", column="1") 

    botonavances= Button(framemain,text="AVANCES",command=favances)
    botonavances.grid(row="7", column="1") 



def botoningresar():
    #ingresomain()
    
    #selecciona la data a comparar
    rut = entryuser.get()
    password = entrypass.get()
    cursor = bd.cursor()
    sql =  "SELECT rut,contraseña,codigo_empresa from usuarios"
    try: 
        cursor.execute(sql)
        data = cursor.fetchall()
        
    except Exception as e :
        print("exception : ")
    bd.commit()
    cursor.close()
    bd.close()
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

    txtcpro=Label(frameingresar,text="Codigo proyecto")
    txtcpro.grid(row="3", column="0")
    entrycpro=Entry(frameingresar)
    entrycpro.grid(row="3",column="1")

   

    def addbdusuario():
        rut = entryrut.get()
        password = entrypass.get()
        codigo = entrycpro.get()
        cursor=bd.cursor()
        sql =  "insert into usuarios (Rut,Contraseña,Codigo_empresa) value('%s','%s','%s')" % (rut,password,codigo)
        try:
         cursor.execute(sql)
         cursor.close()
         bd.commit()
         bd.close()
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
