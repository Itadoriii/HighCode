from ast import Index
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter 
import pandas as pd 
import Frentes4 # importo el archivo de frentes.py

#aqui se abre la segunda ventana cuando se valida el boton ingresar (poner if despues)
def botoningresar():
    frame1.destroy()#elimina frame 1
    frame2=Frame(win)
    frame2.config(width="800",height="600",bg="#3c4350")#tamanaño del frame
    win.resizable(width=False, height=False) #no se agranda la ventana
    frame2.propagate(0) # evita que los entrybotonestext  redimensionen el programa
    frame2.pack()
    mostrartablas=Button(frame2,width="100",height="10", text="INPUT TABLAS",command=Frentes4.mostrartabla)
    mostrartablas.place(x="45",y="10")
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
