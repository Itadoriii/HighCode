from ast import Index
from tkinter import *
from tkinter import ttk
from tkinter import Tk, Label, Button,Entry, Frame, END
from tkinter import filedialog
import tkinter 
import pandas as pd



nombre1,apellido1,edad1,correo1,telefono1 = [],[],[],[],[]

def mostrartabla():
    ventana=Tk()
    ventana.config(bg='#3c4350')
    ventana.resizable(0,0)
    ventana.title('INPUT TABLA FRENTES')
    frame1 = Frame(ventana, bg='#3c4350')
    frame1.grid(column=0, row=0, sticky='nsew')
    frame2 = Frame(ventana, bg='#3c4350')
    frame2.grid(column=1, row=0, sticky='nsew')
    nombre = Label(frame1, text ='FRENTE', width=10).grid(column=0, row=0, pady=20, padx= 10)
    ingresa_nombre = Entry(frame1,  width=20, font = ('Arial',12))
    ingresa_nombre.grid(column=1, row=0)
    apellido = Label(frame1, text ='ESTADO', width=10).grid(column=0, row=1, pady=20, padx= 10)
    ingresa_apellido = Entry(frame1, width=20, font = ('Arial',12))
    ingresa_apellido.grid(column=1, row=1)
    edad = Label(frame1, text ='DIRECCION', width=10).grid(column=0, row=2, pady=20, padx= 10)
    ingresa_edad = Entry(frame1,  width=20, font = ('Arial',12))
    ingresa_edad.grid(column=1, row=2)
    correo = Label(frame1, text ='TAMAÑO', width=10).grid(column=0, row=3, pady=20, padx= 10)
    ingresa_correo = Entry(frame1,  width=20, font = ('Arial',12))
    ingresa_correo.grid(column=1, row=3)
    telefono = Label(frame1, text ='RUTA', width=10).grid(column=0, row=4, pady=20, padx= 10)
    ingresa_telefono = Entry(frame1, width=20, font = ('Arial',12))
    ingresa_telefono.grid(column=1, row=4)

    def agregar_datos():
	    global nombre1, apellido1, dni1, correo1, telefono1

	    nombre1.append(ingresa_nombre.get())
	    apellido1.append(ingresa_apellido.get())
	    edad1.append(ingresa_edad.get())
	    correo1.append(ingresa_correo.get())
	    telefono1.append(ingresa_telefono.get())

	    ingresa_nombre.delete(0,END)
	    ingresa_apellido.delete(0,END)
	    ingresa_edad.delete(0,END)
	    ingresa_correo.delete(0,END)
	    ingresa_telefono.delete(0,END)
    def guardar_datos():	
	    global nombre1,apellido1,edad1,correo1,telefono1
	    datos = {'FRENTE':nombre1,'ESTADo':apellido1, 'DIRECCION':edad1, 'TAMAÑO':correo1, 'RUTA':telefono1 } 
	    nom_excel  = str(nombre_archivo.get() + ".xlsx")	
	    df = pd.DataFrame(datos,columns =  ['FRENTE', 'ESTADo', 'DIRECCION', 'TAMAÑO', 'RUTA']) 
	    df.to_excel(nom_excel)
	    nombre_archivo.delete(0,END)

    agregar = Button(frame1, width=20, font = ('Arial',12, 'bold'), text='Agregar', bg='red',bd=5, command =agregar_datos)
    agregar.grid(columnspan=2, row=5, pady=20, padx= 10)
    archivo = Label(frame2, text ='Ingrese Nombre del archivo', width=25, bg='gray16',font = ('Arial',12, 'bold'), fg='white')
    archivo.grid(column=0, row=0, pady=10, padx= 10)
    nombre_archivo = Entry(frame2, width=23, font = ('Arial',12),highlightbackground = "purple", highlightthickness=4)
    nombre_archivo.grid(column=0, row=1, pady=1, padx= 10)
    guardar = Button(frame2, width=20, font = ('Arial',12, 'bold'), text='Guardar', bg='red',bd=5, command =guardar_datos)
    guardar.grid(column=0, row=2, pady=20, padx= 10)
    ventana.mainloop()



















