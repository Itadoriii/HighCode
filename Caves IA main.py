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


def botoningresar():
    cursor = bd.cursor()
    sql =  "SELECT rut from usuarios"
    try: 
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
    except Exception as e :
        print("exception : ")

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
        except Exception as e:
         print(e)
        bd.commit()
        cursor.close()
        bd.close()
        win2.destroy()
    

   
  

    botonbd=Button(frameingresar,text="add bd", command=addbdusuario)
    botonbd.grid(row="7",column="1")




win=Tk()
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
