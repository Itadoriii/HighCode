from ast import Index
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter 
import pymysql.cursors

#coneccion bd red local
bd = pymysql.connect(host='localhost',
                             user='root',
                             password='1312',
                             database='cavestest',
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
botoningresarr.pack()






win.mainloop()
