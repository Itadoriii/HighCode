from ast import Index
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter
from tkinter.font import BOLD 
import pymysql.cursors

#coneccion bd red local
bd = pymysql.connect(host='localhost',
                             user='root',
                             password='1312',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

def addbdfrentes():
    win4=Tk()
    win4.geometry('300x270')
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
    entrytipo['values'] = ('1','2','3','4','5')

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
    entryestado['values'] = ('0','1')

    txttamaño =Label(frameingreso,text="Tamaño")
    txttamaño.grid(row="6",column="0")
    entrytamaño= Entry(frameingreso)
    entrytamaño.grid(row="6",column="1")

    txtrutacritica=Label(frameingreso,text="Ruta critica")
    txtrutacritica.grid(row="7",column="0")
    entryrutacritica= ttk.Combobox(frameingreso)
    entryrutacritica.grid(row="7",column="1")
    entryrutacritica['values'] = ('1','2','3','4')

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

    def llenarfrente():
        tipo =int(entrytipo.get())
        sigla = entrysigla.get()
        numero = entrynumero.get()
        direccion = entrydireccion.get()
        estado =int(entryestado.get())
        tamaño = entrytamaño.get()
        ruta =int(entryrutacritica.get())
        distancia =int(entrydistanciamarina.get())
        nivel = entrynivelfrente.get() 
        macrobloque =entrymacrobloque.get()
        id = entryid.get()
        cursor=bd.cursor()
        sql =  "insert into frentes(Tipo,Sigla,Numero,Direccion,Estado,Tamaño,Ruta_Critica,Distancia_Marinas,Nivel,Macrobloque,Id_Frente) value('%d','%s','%s','%s','%d','%s','%d','%d','%s','%s','%s')" % (tipo,sigla,numero,direccion,estado,tamaño,ruta,distancia,nivel,macrobloque,id)
        try:
         cursor.execute(sql)
         print (sql)
         cursor.close()
         bd.commit()
         bd.close()
        except Exception as e:
         print(e)
       # cursor.close()
        #bd.commit()
       # bd.close()
        
        win4.destroy()

    botonllenarbd=Button(frameingreso,text="Añadir a la Bd",command=llenarfrente)
    botonllenarbd.grid(row="11")

def addbdtopografia():
    win4=Tk()
    frameingreso = Frame(win4)
    frameingreso.pack()

    def llenartopografia():
        id = entryidt.get()
        avance = int(entryavance.get())
        nivel = entrynivel.get()
        notact = entrynotaact.get()
        pk = entrypkacumulado.get()
        fecha = entryfecha.get()
        hora = entryhora.get()
        cursor=bd.cursor()
        sql =  "insert into topografia(Avance,Nivel,Nota_actividad,Pk_acumulado,Fecha,Hora,Id_Frente) value('%d','%s','%s','%s','%s','%s','%s')" % (avance,nivel,notact,pk,fecha,hora,id)
        try:
         cursor.execute(sql)
         cursor.close()
         bd.commit()
         bd.close()
        except Exception as e:
         print(e)
       # cursor.close()
        #bd.commit()
       # bd.close()
        
        win4.destroy()





    txtidt =Label(frameingreso,text="ID")
    txtidt.grid(row="0",column="0")
    entryidt = Entry(frameingreso)
    entryidt.grid(row="0",column="1")

    txtavance=Label(frameingreso,text="Avance")
    txtavance.grid(row="1",column="0")
    entryavance= Entry(frameingreso)
    entryavance.grid(row="1",column="1")

    txtnivel=Label(frameingreso,text="Nivel")
    txtnivel.grid(row="2",column="0")
    entrynivel= ttk.Combobox(frameingreso)
    entrynivel.grid(row="2",column="1")
    entrynivel['values'] = ('PD','HD','INY','EXT','CH','TI','TS')

    txtnotaact=Label(frameingreso,text="Nota Actividad")
    txtnotaact.grid(row="3",column="0")
    entrynotaact= Entry(frameingreso)
    entrynotaact.grid(row="3",column="1")

    txtpkacumulado=Label(frameingreso,text="Pk Acumulado")
    txtpkacumulado.grid(row="4",column="0")
    entrypkacumulado= Entry(frameingreso)
    entrypkacumulado.grid(row="4",column="1")

    txtfecha=Label(frameingreso,text="Fecha")
    txtfecha.grid(row="5",column="0")
    entryfecha= Entry(frameingreso)
    entryfecha.grid(row="5",column="1")

    txthora=Label(frameingreso,text="Hora")
    txthora.grid(row="6",column="0")
    entryhora= Entry(frameingreso)
    entryhora.grid(row="6",column="1")
    botonllenarbd=Button(frameingreso,text="Añadir a la Bd",command=llenartopografia)
    botonllenarbd.grid(row="10")

  


    


def ingresomain():
    
    win3 = Tk()
    win3.config(bg="lightblue")
    win3.geometry('580x420')
    framemain = Frame(win3)
    framemain.config(bg="blue",width=480,height=320,relief="sunken")
    framemain.pack()
    

    botonFrentes = Button(framemain,text="LLENAR FRENTES",command=addbdfrentes)
    botonFrentes.grid(row="2", column="1")

    botonTopografia = Button(framemain,text="LLENAR TOPOGRAFIA",command=addbdtopografia)
    botonTopografia.grid(row="3", column="1")

    def verestadofrentes():
        win3.destroy()
        cursor = bd.cursor()
        sql =  "SELECT * from estado_frentes"
        try: 

            cursor.execute(sql)
            data = cursor.fetchall()
            print(data)
            cursor.close()
            bd.commit()
            bd.close()
        except Exception as e :
            print("exception : ")
        #bd.commit()
        #cursor.close()
        #bd.close()'''
        ingresomain()


    def verestadoequipos():
        win3.destroy()
        cursor = bd.cursor()
        sql =  "SELECT * from estado_equipos"
        try: 
            cursor.execute(sql)
            data = cursor.fetchall()
            print(data)
            cursor.close()
            bd.commit()
            bd.close()
        except Exception as e :
             print("exception : ")
        #bd.commit()
        #cursor.close()
        #bd.close()'''
        ingresomain()
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
         print("exception : ")
    #bd.commit()
    #cursor.close()
    #bd.close()'''
        ingresomain()

    botonEstadofrentes = Button(framemain,text="ESTADO FRENTES",command=verestadofrentes)
    botonEstadofrentes.grid(row="4", column="1")

    botonEstadoEquipos= Button(framemain,text="ESTADO EQUIPOS",command=verestadoequipos)
    botonEstadoEquipos.grid(row="5", column="1")

    botonEstadoservicios= Button(framemain,text="ESTADO SERVICIOS",command=verestadoservicios)
    botonEstadoservicios.grid(row="6", column="1") 


def botoningresar():
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
        j=i['contraseña']
        i=i['rut']
        if(i==rut):
            win.destroy()
            if(j==password):
                ingresomain()

  

def botonregistrar():
    win2=Tk()
    frameingresar=Frame(win2)
    frameingresar.pack()

    txtrut=Label(frameingresar,text="Rut")
    txtrut.grid(row="0", column="0")
    entryrut=Entry(frameingresar)
    entryrut.grid(row="0",column="1")

    txtdv=Label(frameingresar,text="Dv")
    txtdv.grid(row="1", column="0")
    entrydv=Entry(frameingresar)
    entrydv.grid(row="1",column="1")

    txtpass=Label(frameingresar,text="Contraseña")
    txtpass.grid(row="2", column="0")
    entrypass=Entry(frameingresar)
    entrypass.grid(row="2",column="1")

    txtcpro=Label(frameingresar,text="Codigo proyecto")
    txtcpro.grid(row="3", column="0")
    entrycpro=Entry(frameingresar)
    entrycpro.grid(row="3",column="1")

    txtccon=Label(frameingresar,text="Codigo contrato")
    txtccon.grid(row="4", column="0")
    entryccon=Entry(frameingresar)
    entryccon.grid(row="4",column="1")

    txtgrupo=Label(frameingresar,text="Grupo")
    txtgrupo.grid(row="5", column="0")
    entrygrupo=Entry(frameingresar)
    entrygrupo.grid(row="5",column="1")

    txtturno=Label(frameingresar,text="Turno")
    txtturno.grid(row="6", column="0")
    entryturno=Entry(frameingresar)
    entryturno.grid(row="6",column="1")

    def addbdusuario():
        rut = int(entryrut.get())
        dv = entrydv.get()
        password = entrypass.get()
        codigoproyecto = entrycpro.get()
        codigocontrato = entryccon.get()
        grupo = entrygrupo.get()
        turno = entryturno.get()
        cursor=bd.cursor()
        sql =  "insert into usuarios (Rut,Dv,Password,Codigo_proyecto,Codigo_contrato,Grupo,Turno) value('%d','%s','%s','%s','%s','%s','%s')" % (rut,dv,password,codigoproyecto,codigocontrato,grupo,turno)
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
        ingresomain()

    botonbd=Button(frameingresar,text="add bd",command=addbdusuario)
    botonbd.grid(row="7",column="1")


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
