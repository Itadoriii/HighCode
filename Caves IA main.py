from ast import Index
from cProfile import run
import collections
import tkinter as tk 
from email.headerregistry import SingleAddressHeader
from http.client import NOT_ACCEPTABLE
from itertools import permutations
from logging import CRITICAL
from msilib.schema import ComboBox
from operator import index
from optparse import Values
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
from datetime import datetime
from mysqlx import Column
from numpy import append, can_cast, char, character, mat, matrix
from pkg_resources import PathMetadata 
import pymysql.cursors
import numpy as np
import openpyxl
import copy
#memo 
ides1 = []
ciclos1 = []
operaciones1 = []
niveles1 = []
ordenHD = []
opHD = []
ordenPD = []
opPD = []
ordenINY = []
opINY = []
ordenCH = []
opCH = []
ordenEXT =[]
opEXT = []
ordenTI =[]
opTI = []

ciclominero1 = ['regado_marina','extraccion_marina','acuñadura','limpieza_pata','escaner','mapeo_geomecanico',
'shotcrete_fibra','perforacion_pernos','lechado_pernos','instalacion_malla','hilteo_malla','proyeccion_shotcrete',
'marcacion_topografica','perforacion_avance','carguio_explosivos','tronadura']
# memoria ciclos

operaciones = [ 
        ['rm','regado_marina','jefe_turno',1,1,1,'marina',0,'si','-'],
        ['e','extraccion_marina','LHD',3,3,4,'marina',1,'si','*e'],
        ['ac','acunadura','acunador',1,1,1,'marina',1,'si','*ac'],
        ['lp','limpieza_pata','LHD',1,1,1,'marina',1,'si','*lp'],
        ['sc','escaner','topografo',1,1,1,'-',0,'si','-'],
        ['mg','mapeo_geomecanico','topografo',1,1,1,'-',0,'si','-'],
        ['shf','shotcrete_fibra','roboshot',1,1,1,'-',2,'no','*shf'],
        ['pp','perforacion_pernos','jumbo',3,4,5,'mineria',0,'si','-'],
        ['l','lechado_pernos','cuadrilla',3,4,5,'mineria',2,'si','*l'],
        ['m','instalacion_malla','cuadrilla',3,4,5,'mineria',0,'si','-'],
        ['h','hilteo_malla','cuadrilla',3,4,5,'mineria',0,'si','-'],
        ['sh','proyeccion_shotcrete','roboshot',2,2,2,'mineria',2,'no','*sh'],
        ['mt','marcacion_topografica','topografo',1,1,1,'mineria',0,'si','-'],
        ['pa','perforacion_avance','jumbo',3,4,5,'mineria',0,'si','-'],
        ['c','carguio_explosivos','cuadrilla',3,3,3,'mineria',0,'no','-'],
        ['q','tronadura','-',1,1,1,'mineria',0,'no','-'],
    ]
ciclos = [ 
        ['p-m-sh',1,['rm','e','ac','lp','sc','mg','pp','l','m','mt','h','sh','pa','c','q']],
        ['p-m-sh',2,['rm','e','ac','lp','sc','mg','pp','l','m','mt','h','pa','sh','c','q']],
        ['p-m-sh',3,['rm','e','ac','lp','sc','mg','pp','l','m','mt','pa','h','sh','c','q']],
        ['p-m-sh',4,['rm','e','ac','lp','sc','mg','pp','l','m','h','sh','mt','pa','c','q']],
        ['p-m-sh',5,['rm','e','ac','lp','sc','mg','pp','l','m','h','mt','sh','pa','c','q']],
        ['p-m-sh',6,['rm','e','ac','lp','sc','mg','pp','l','m','h','mt','pa','sh','c','q']],
        ['p-shf',1,['rm','e','ac','lp','sc','mg','shf','mt','pp','l','pa','c','q']],
        ['p-shf',2,['rm','e','ac','lp','sc','mg','shf','mt','pp','pa','l','c','q']],
        ['p-shf',3,['rm','e','ac','lp','sc','mg','shf','mt','pa','pp','l','c','q']],
        ['p-shf',4,['rm','e','ac','lp','sc','mg','shf','pp','l','mt','pa','c','q']],
        ['p-shf',5,['rm','e','ac','lp','sc','mg','shf','pp','mt','l','pa','c','q']],
        ['p-shf',6,['rm','e','ac','lp','sc','mg','shf','pp','mt','pa','l','c','q']],
        ['shf-p-m-sh',1,['rm','e','ac','lp','sc','mg','shf','pp','mt','pa','l','c','q']],
        ['shf-p-m-sh',2,['rm','e','ac','lp','sc','mg','shf','mt','pp','pa','l','c','q']],
        ['shf-p-m-sh',3,['rm','e','ac','lp','sc','mg','shf','mt','pa','pp','l','c','q']]
    ]

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
                             password='admin',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd2 = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd3 = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd4 = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd5 = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd6 = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd7 = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd8 = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd9 = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd10 = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd11 = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd12 = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd13 = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

bd14 = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

matricitaa =  []
matricitaa2 =  []

ciclosyfrentes = []
def ventanaalgoritmos():
    def run():
        inicio = entryi.get()
        termino = entryt.get()
        algoritmos(int(inicio),int(termino))
    
    def ventanamatriz():
        win4 = Tk()
        win4.geometry('1080x200')
        frame = Frame(win4)
        frame.pack()
        extra = ['id','tam','ope','est','for','cic','08:00','08:30','09:00','09:30','10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30','18:00','18:30','19:00','19:30']
        for uwu in range(0,30):
            j = Entry(frame,width=5)
            j.grid(row = 0, column = uwu)
            j.insert(END,extra[uwu])

        for f in range(0,len(matricitaa2)):
                    for j in range(0,len(matricitaa2[f])):
                            x = Entry(frame,width=5)
                            x.grid(row = f+1, column = j)
                            x.insert(END,matricitaa2[f][j])

        for f in range(0,len(matricitaa)):
                    for j in range(0,len(matricitaa[f])):
                            x = Entry(frame,width=5)
                            x.grid(row = f+1, column = j+6)
                            x.insert(END,matricitaa[f][j])
    


    raiz = Tk()
    raiz.title('LIMITES DEL HORARIO')
    framemain = Frame(raiz)
    framemain.pack()
    txt1 = Label(framemain,text='BLOQUE INICIO DE TURNO')
    txt1.grid(row='0',column='0')
    txt2 = Label(framemain,text='BLOQUE TERMINO DE TURNO')
    txt2.grid(row='1',column='0')
    entryi= ttk.Combobox(framemain)
    entryi.grid(row="0",column="1")
    entryi['values'] = ('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25')
    entryt= ttk.Combobox(framemain)
    entryt.grid(row="1",column="1")
    entryt['values'] = ('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25')
    correr = Button(framemain,text='GENERAR REPORTE',command=run, anchor=CENTER)
    correr.grid(row='3',column='0')
    vmatrix = Button(framemain,text='matriz ',command=ventanamatriz)
    vmatrix.grid(row='3',column='1')

    
    

    

def algoritmos(inicio,termino): 

    print(ciclosyfrentes)
    
    # Algoritmo 1

    print("ALGORTIMO 1")
    
    cursor=bd13.cursor()
    totalfrentes = cursor.execute("select * from frentes")
    print("TOTAL FRENTES")
    print(totalfrentes)

    ciclosyfrente = [
        ['F1',1],
        ['F2',2],
        ['F3',3],
        ['F4',4],
        ['F5',5],
        ['F6',6]
    ]
    for i in range(0,len(ciclosyfrentes)):
        if(len(ciclosyfrentes[i])==1):
            ciclosyfrentes[i].append(1)
    print(ciclosyfrentes)
    #ruta
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

    #urgencia
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
    fortiaux = []
    cicloaux = []
    dista = []
    distasi= []
    distano = []
    troprosia= []
    tropronoa = []
    ciclominero = []
    cicloaux = []
    naux = []
    operfnaux = []
    cursor.execute("select id_frente,operacion,fortificacion from estado_frentes")
    trop = cursor.fetchall()
    for t in trop:
        fren = t['id_frente']
        idaux.append(fren)
        oper = t['operacion']
        operaux.append(oper)
        fort = t['fortificacion']
        fortiaux.append(fort)

    for i in range(totalfrentes):
        if operaux[i] == 'regado_marina':
            operfnaux.append('rm')
        if operaux[i] == 'extraccion_marina':
            operfnaux.append('e')
        if operaux[i] == 'acuñadura':
            operfnaux.append('ac')
        if operaux[i] == 'limpieza_pata':
            operfnaux.append('lp')
        if operaux[i] == 'escaner':
            operfnaux.append('sc')
        if operaux[i] == 'mapeo_geomecanico':
            operfnaux.append('mg')
        if operaux[i] == 'shotcrete_fibra':
            operfnaux.append('shf')
        if operaux[i] == 'perforacion_pernos':
            operfnaux.append('pp')
        if operaux[i] == 'lechado_pernos':
            operfnaux.append('l')
        if operaux[i] == 'instalacion_malla':
            operfnaux.append('m')
        if operaux[i] == 'hilteo_malla':
            operfnaux.append('h')
        if operaux[i] == 'proyeccion_shotcrete':
            operfnaux.append('sh')
        if operaux[i] == 'marcacion_topografica':
            operfnaux.append('mt')
        if operaux[i] == 'perforacion_avance':
            operfnaux.append('pa')
        if operaux[i] == 'carguio_explosivos':
            operfnaux.append('c')
        if operaux[i] == 'tronadura':
            operfnaux.append('q')

    for r in range(totalfrentes):
        for c in range(len(ciclosyfrentes)):
            if(idaux[r] == ciclosyfrentes[c][0]):
                cicloaux.append(ciclosyfrentes[c][1])

    for r in range(totalfrentes):
        for c in range(15):
            if(fortiaux[r]==ciclos[c][0]) and (int(cicloaux[r])==ciclos[c][1]):
                ciclominero.append(ciclos[c][2])
                naux.append(len(ciclos[c][2]))

    for i in range(totalfrentes):
        fin = naux[i]
        for j in range(fin):
            if(operfnaux[i]==ciclominero[i][j]):
                aux = j+1
                dis = fin-aux
                dista.append(dis)
    print(dista)
    
    for i, num in enumerate(dista):
        menor= None
        posi = None
        if (num != 0):
            if (num not in distasi and num not in distano):
                if (num <= 4):
                    menor = num
                    posi = i
        if menor != None:
            troprosia.append(idaux[posi])
            distasi.append(menor)
    for p in p2:
        for r in range(len(troprosia)):
            if(p==troprosia[r]):
                troprosi.append(p)

    for i, num in enumerate(dista):
        menor= None
        posi = None
        if (num != 0):
                if (num > 4):
                    menor = num
                    posi = i
        if menor != None:
            tropronoa.append(idaux[posi])
            distano.append(menor)

    for p in p2:
        for r in range(len(tropronoa)):
            if(p==tropronoa[r]):
                troprono.append(p)
    
    for i, num in enumerate(dista):
        menor= None
        posi = None
        if (num == 0):
                menor = num
                posi = i
        if menor != None:
            tropronoa.append(idaux[posi])
            distano.append(menor)

    for p in p2:
        for r in range(len(tropronoa)):
            if(p==tropronoa[r]):
                if(tropronoa[r] not in troprono):
                    troprono.append(p)
       

# llenado tronadura prox

    tp = []

    for r in troprosi:
        tp.append(r)

    for r in troprono:
        tp.append(r)
    
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

    # Algoritmo 2

    cursor=bd14.cursor()
    totalfrentes = cursor.execute("select * from frentes")
    print("ALGORITMO 2")

    l1= []
    lr = []
    laux = []
    tamf = []
    opf = []
    fof = []
    ciclof = []
    eaf = []
    tamor = []
    opeor = []
    cior = []
    foor = []
    eaor = []

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

    cursor.execute("select id_frente, estado_avance from estado_frentes")
    eafn = cursor.fetchall()
    for x in eafn:
        eaf.append(x)

    for p in pf:
        for e in eaf:
            if(p == e['id_frente']):
                eaor.append(e['estado_avance'])

    cursor.execute("select id_frente, fortificacion from estado_frentes")
    fofn= cursor.fetchall()
    for x in fofn:
        fof.append(x)

    for p in pf:
        for f in fof:
            if(p==f['id_frente']):
                foor.append(f['fortificacion'])

     # rescato id ( prio ) , tam , est , estado_av, fort
    #id
    for i in range(totalfrentes):
        lr.append([])
        for j in range(1):
            lr[i].append(pf[i])
    #tam
    for i in range(totalfrentes):
        lr.append([])
        for j in range(1):
            lr[i].append(tamor[i])
    #estado       
    for i in range(totalfrentes):
        lr.append([])
        for j in range(1):
            if opeor[i] == 'regado_marina':
                lr[i].append('rm')
            if opeor[i] == 'extraccion_marina':
                lr[i].append('e')
            if opeor[i] == 'acuñadura':
                lr[i].append('ac')
            if opeor[i] == 'limpieza_pata':
                lr[i].append('lp')
            if opeor[i] == 'escaner':
                lr[i].append('sc')
            if opeor[i] == 'mapeo_geomecanico':
                lr[i].append('mg')
            if opeor[i] == 'shotcrete_fibra':
                lr[i].append('shf')
            if opeor[i] == 'perforacion_pernos':
                lr[i].append('pp')
            if opeor[i] == 'lechado_pernos':
                lr[i].append('l')
            if opeor[i] == 'instalacion_malla':
                lr[i].append('m')
            if opeor[i] == 'hilteo_malla':
                lr[i].append('h')
            if opeor[i] == 'proyeccion_shotcrete':
                lr[i].append('sh')
            if opeor[i] == 'marcacion_topografica':
                lr[i].append('mt')
            if opeor[i] == 'perforacion_avance':
                lr[i].append('pa')
            if opeor[i] == 'carguio_explosivos':
                lr[i].append('c')
            if opeor[i] == 'tronadura':
                lr[i].append('q')
    # estado_avance
    for i in range(totalfrentes):
        lr.append([])
        for j in range(1):
            lr[i].append(eaor[i])

    # fortificacion
    for i in range(totalfrentes):
        lr.append([])
        for j in range(1):
            lr[i].append(foor[i])

    # pregunta al usuario el bloque de inicio y termino

    print("[-08:00-08:30-09:00-09:30-10:00-10:30-11:00-11:30-12:00-12:30-13:00-13:30-14:00-14:30-15:00-15:30-16:00-16:30-17:00-17:30-18:00-18:30-19:00-19:30]")
    print("[- 1   - 2   - 3   - 4   - 5   - 6   - 7   - 8   - 9   - 10  - 11  - 12  - 13  - 14  - 15  - 16  - 17  - 18  - 19  - 20  - 21  - 22  - 23  - 24  ]")
    bloquei = inicio
    bloquei = bloquei - 1
    bloquet = termino
    reco = bloquet-bloquei

    # guarda espacios segun defina usuario

    for i in range(totalfrentes):
        l1.append([])
        for j in range(bloquei):
            l1[i].append('-')

    # llena primer frente y guarda almuerzo

    contador = 0
    recualmu = 0
    

    for i in range(1):

        limit = bloquei
        larg = 0

        # selecciona ciclo

        for c in range(len(ciclosyfrente)):
            if(lr[i][0] == ciclosyfrente[c][0]):
                ciclof.append(ciclosyfrente[c][1])

        # guarda largo del ciclo

        for c in range(15):
            if(lr[i][4]==ciclos[c][0]) and (ciclof[i]==ciclos[c][1]):
                fortycic=c
                larg = len(ciclos[fortycic][2])

        #busca donde retomar actividad
        for j in range(larg):
            if(lr[i][2]==ciclos[fortycic][2][j]): 
                                posi = j+1 #siguiente de lista act 
                                break
        
        for k in range(reco):

            # comienza el llenado

            if (k+posi<larg): #no es tronadura, ciclo sin terminar
                po = k+posi
                esav = int(lr[i][3]) # rescata estado avance operacion

                # rescata recurso, duracion segun tamaño y si es parcial o no 

                cicloclasic = 15 # longitud ciclo original para comparar

                for l in range(cicloclasic):
                    if (lr[i][1]=='C'):
                        if (ciclos[fortycic][2][po]==operaciones[l][0]):
                            duracion = int(operaciones[l][3])
                            pausa = int(operaciones[l][7])
                            parcial = operaciones[l][8]

                    if (lr[i][1]=='M'):
                        if (ciclos[fortycic][2][po]==operaciones[l][0]):
                            duracion = int(operaciones[l][4])
                            pausa = int(operaciones[l][7])
                            parcial = operaciones[l][8]

                    if (lr[i][1]=='G'):
                        if (ciclos[fortycic][2][po]==operaciones[l][0]):
                            duracion = int(operaciones[l][5])
                            pausa = int(operaciones[l][7])
                            parcial = operaciones[l][8]

                # repetidor para cantidad de bloques por actividad

                if (parcial=='si'): #parcial

                    auxdu = esav
                    contav = 0

                    f1 = ciclos[fortycic][2][po-contador]
                    
                    while(auxdu<duracion):

                        if(limit<bloquet): # restriccion fin del turno

                            if(limit==9):
                                l1[i].append('A')
                                l1[i].append('A')
                                limit = limit + 2
                                recualmu = f1
                            
                            else:
                                l1[i].append(f1)
                                limit = limit + 1
                                contav = contav + 1
                                auxdu = auxdu + 1

                                # guardar contav (nuevo estado_avance)

                        else:
                            auxdu = auxdu + 1

                    if(auxdu==duracion):

                        #estado_avance = 0  where id_frente = lr[i][0] 

                        if(pausa>0):
                            auxpa = 0
                            while (auxpa<pausa):

                                if(limit<bloquet): # restriccion fin del turno

                                    if(limit==9):
                                        l1[i].append('A')
                                        l1[i].append('A')
                                        limit = limit + 2
                                        recualmu = f1

                                    else:
                                        l1[i].append('-')
                                        limit = limit + 1
                                        auxpa = auxpa + 1

                                else:
                                    auxpa = auxpa + 1
                    
                    # guardar contav (nuevo estado_avance) where id_frente = lr[i][0] a la BD

                if (parcial=='no'): #no parcial

                    auxdu = esav
                    contav = 0

                    f1 = ciclos[fortycic][2][po-contador]

                    if(limit==9):
                        l1[i].append('A')
                        l1[i].append('A')
                        limit = limit + 2
                        recualmu = f1

                    else:

                        if(limit+duracion<bloquet):

                            f1 = ciclos[fortycic][2][po-contador]

                            if(f1!='q'): # no es q (restriccion q a la ultima posicion)
                                
                                while(auxdu<duracion):

                                    if(limit<bloquet): # restriccion fin del turno
                                                
                                        l1[i].append(f1)
                                        limit = limit + 1
                                        contav = contav + 1
                                        auxdu = auxdu + 1

                                    else:
                                        auxdu = auxdu + 1


                                if(auxdu==duracion):

                                    #estado_avance = 0  where id_frente = lr[i][0] 

                                    if(pausa>0):
                                        auxpa = 0
                                        while (auxpa<pausa):
                                            if(limit<bloquet): # restriccion fin del turno
                                                if(limit==9):
                                                    l1[i].append('A')
                                                    l1[i].append('A')
                                                    limit = limit + 2
                                                    recualmu = f1

                                                else:
                                                    l1[i].append('-')
                                                    limit = limit + 1
                                                    auxpa = auxpa + 1
                                            else:
                                                auxpa = auxpa + 1

                            # guardar contav (nuevo estado_avance) where id_frente = lr[i][0] a la BD

                            if(f1=='q'):
                                indite = len(l1[i])
                    
                        if(limit+duracion>=bloquet):

                            if(limit<bloquet): # restriccion fin del turno

                                if(limit==9):
                                    l1[i].append('A')
                                    l1[i].append('A')
                                    limit = limit + 2
                                    recualmu = f1

                                else:
                                    l1[i].append('-')
                                    limit = limit + 1
                                    contador = contador + 1
            
            if(k+posi>=larg):

                if(lr[i][2]!='q'):

                    # guarda q al final

                    num = bloquet - 1 - indite

                    while (num>0):

                        if(limit<bloquet):

                            if (num == 1):
                                l1[i].append('q')
                                limit = limit + 1

                            if (num !=1):
                                #guarda el almuerzo

                                f1 = ciclos[fortycic][2][po-contador]

                                if(limit==9):
                                    l1[i].append('A')
                                    l1[i].append('A')
                                    limit = limit + 2
                                    recualmu = f1

                                else:
                                    l1[i].append('-')
                                    limit = limit + 1

                        num = num - 1
                                
                    if (num == 0):
                        break    

                if(lr[i][2]=='q'):
                    
                    po=k

                    if(po<larg):

                        esav = int(lr[i][3]) # rescata estado avance operacion

                        # rescata recurso, duracion segun tamaño y si es parcial o no 

                        cicloclasic = 15 # longitud ciclo original para comparar

                        for l in range(cicloclasic):
                            if (lr[i][1]=='C'):
                                if (ciclos[fortycic][2][po]==operaciones[l][0]):
                                    duracion = int(operaciones[l][3])
                                    pausa = int(operaciones[l][7])
                                    parcial = operaciones[l][8]

                            if (lr[i][1]=='M'):
                                if (ciclos[fortycic][2][po]==operaciones[l][0]):
                                    duracion = int(operaciones[l][4])
                                    pausa = int(operaciones[l][7])
                                    parcial = operaciones[l][8]

                            if (lr[i][1]=='G'):
                                if (ciclos[fortycic][2][po]==operaciones[l][0]):
                                    duracion = int(operaciones[l][5])
                                    pausa = int(operaciones[l][7])
                                    parcial = operaciones[l][8]

                        # repetidor para cantidad de bloques por actividad

                        if (parcial=='si'): #parcial

                            auxdu = esav
                            contav = 0

                            f1 = ciclos[fortycic][2][po-contador]

                            cicloclasic = 15 # ciclo original operaciones

                            for y in range(cicloclasic): 
                                if(f1==operaciones[y][0]):
                                    rf1 = operaciones[y][2] # guarda recurso actividad
                                    ap = operaciones[y][9] # guarda pausa
                    
                            while(auxdu<duracion):

                                if(limit<bloquet): # restriccion fin del turno

                                    if(limit==9):
                                        l1[i].append('A')
                                        l1[i].append('A')
                                        limit = limit + 2
                                        recualmu = f1
                                    
                                    else:
                                        l1[i].append(f1)
                                        limit = limit + 1
                                        contav = contav + 1
                                        auxdu = auxdu + 1

                                        # guardar contav (nuevo estado_avance)

                                else:
                                    auxdu = auxdu + 1

                            if(auxdu==duracion):

                                #estado_avance = 0  where id_frente = lr[i][0] 

                                if(pausa>0):
                                    auxpa = 0
                                    while (auxpa<pausa):

                                        if(limit<bloquet): # restriccion fin del turno

                                            if(limit==9):
                                                l1[i].append('A')
                                                l1[i].append('A')
                                                limit = limit + 2
                                                recualmu = f1

                                            else:
                                                l1[i].append(ap)
                                                limit = limit + 1
                                                auxpa = auxpa + 1
                                        
                                        else:
                                            auxpa = auxpa + 1
                                        
                            # guardar contav (nuevo estado_avance) where id_frente = lr[i][0] a la BD

                        if (parcial=='no'): #no parcial

                            auxdu = esav
                            contav = 0

                            if(limit==9):
                                l1[i].append('A')
                                l1[i].append('A')
                                limit = limit + 2
                                recualmu = f1

                            else:

                                if(limit+duracion<bloquet):

                                    f1 = ciclos[fortycic][2][po-contador]

                                    if(f1!='q'): # no es q (restriccion q a la ultima posicion)
                                        
                                        while(auxdu<duracion):

                                            if(limit<bloquet): # restriccion fin del turno

                                                l1[i].append(f1)
                                                limit = limit + 1
                                                contav = contav + 1
                                                auxdu = auxdu + 1

                                            else:
                                                auxdu = auxdu + 1

                                        if(auxdu==duracion):

                                            #estado_avance = 0  where id_frente = lr[i][0] 

                                            if(pausa>0):
                                                auxpa = 0
                                                while (auxpa<pausa):
                                                    if(limit<bloquet): # restriccion fin del turno
                                                        if(limit==9):
                                                            l1[i].append('A')
                                                            l1[i].append('A')
                                                            limit = limit + 2
                                                            recualmu = f1

                                                        else:
                                                            l1[i].append('-')
                                                            limit = limit + 1
                                                            auxpa = auxpa + 1
                                                    else:
                                                        auxpa = auxpa + 1
                                                    
                                    # guardar contav (nuevo estado_avance) where id_frente = lr[i][0] a la BD

                                if(limit+duracion>=bloquet):

                                    if(limit<bloquet): # restriccion fin del turno
                                        l1[i].append('-')
                                        limit = limit + 1
                                        contador = contador + 1

    # guarda data almuerzo

    cuadrilla = ['rm','l','m','h','c']
    jumbos = ['pp','pa']
    otros = ['e','ac','lp','sc','mg','shf','sh','mt']
    almuerzo = 0

    if (recualmu in cuadrilla):
        almuerzo = 1

    if (recualmu in jumbos):
        almuerzo = 2

    if (recualmu in otros):
        almuerzo = 3


    # llena demas frentes
    
    rf0 = 0
    rf1 = 0

    for i in range(1,totalfrentes):

        if (lr[i][4]=='p-m-sh'):
            totalci=6

        if (lr[i][4]=='p-shf'):
            totalci=6

        if (lr[i][4]=='shf-p-m-sh'):
            totalci=3

        xci = 0


        for q in range(totalci):

            # guarda espacios segun defina usuario

            for v in range(bloquei):
                laux.append('-')

            print("esto pasa en i = ",i)

            limit = bloquei 
            contador = 0

            # guarda largo del ciclo

            for f in range(15):
                if(lr[i][4]==ciclos[f][0]):
                    if(q==ciclos[f][1]):
                        fortycic = f
                        larg=len(ciclos[f][2])

            #busca donde retomar actividad
            for j in range(larg):
                if(lr[i][2]==ciclos[fortycic][2][j]): 
                                    posi = j+1 #siguiente de lista act 
                                    break

            for k in range(reco):

                # comienza el llenado

                if (k+posi<larg): #no es tronadura, ciclo sin terminar
                    po = k+posi
                    esav = int(lr[i][3]) # rescata estado avance operacion

                    # rescata recurso, duracion segun tamaño y si es parcial o no 

                    cicloclasic = 15 # longitud ciclo original para comparar

                    for l in range(cicloclasic):
                        if (lr[i][1]=='C'):
                            if (ciclos[fortycic][2][po]==operaciones[l][0]):
                                duracion = int(operaciones[l][3])
                                pausa = int(operaciones[l][7])
                                parcial = operaciones[l][8]

                        if (lr[i][1]=='M'):
                            if (ciclos[fortycic][2][po]==operaciones[l][0]):
                                duracion = int(operaciones[l][4])
                                pausa = int(operaciones[l][7])
                                parcial = operaciones[l][8]

                        if (lr[i][1]=='G'):
                            if (ciclos[fortycic][2][po]==operaciones[l][0]):
                                duracion = int(operaciones[l][5])
                                pausa = int(operaciones[l][7])
                                parcial = operaciones[l][8]

                    qhecha = 'no'
                        
                    # repetidor para cantidad de bloques por actividad

                    if (parcial=='si'): #parcial

                        contav = 0

                        f1 = ciclos[fortycic][2][po-contador]

                        x = 0

                        while(x==0): # busqueda vertical total

                            #guarda almuerzo

                            auxalmu = f1

                            if (almuerzo==1): #tipo 1
                                if(limit==13):
                                    if (auxalmu in otros):
                                        laux.append('A')
                                        laux.append('A')
                                        limit = limit + 2
                                if(limit==11):
                                    if (auxalmu in jumbos):
                                        laux.append('A')
                                        laux.append('A')
                                        limit = limit + 2
                                if(limit==9):
                                    if (auxalmu in cuadrilla):
                                        laux.append('A')
                                        laux.append('A')
                                        limit = limit + 2

                            if (almuerzo==2): #tipo 2
                                if(limit==13):
                                    if (auxalmu in otros):
                                        laux.append('A')
                                        laux.append('A')
                                        limit = limit + 2
                                if(limit==11):
                                    if (auxalmu in cuadrilla):
                                        laux.append('A')
                                        laux.append('A')
                                        limit = limit + 2
                                if(limit==9):
                                    if (auxalmu in jumbos):
                                        laux.append('A')
                                        laux.append('A')
                                        limit = limit + 2

                            if (almuerzo==3): #tipo 3
                                if(limit==13):
                                    if (auxalmu in jumbos):
                                        laux.append('A')
                                        laux.append('A')
                                        limit = limit + 2
                                if(limit==11):
                                    if (auxalmu in cuadrilla):
                                        laux.append('A')
                                        laux.append('A')
                                        limit = limit + 2
                                if(limit==9):
                                    if (auxalmu in otros):
                                        laux.append('A')
                                        laux.append('A')
                                        limit = limit + 2

                            contadoraux = limit
                            auxdu = esav
                            bandera = 0

                            while(auxdu<duracion+pausa): # busqueda vertical total

                                # busqueda vertical fila

                                aux = i-1

                                while (aux>=0):
                                    
                                    if(limit<bloquet) and (contadoraux<bloquet): # restriccion fin del turno

                                        f0 = l1[aux][contadoraux]

                                        for y in range(cicloclasic): 
                                            if(f1==operaciones[y][0]):
                                                rf1 = operaciones[y][2] # guarda recurso actividad
                                                ap1 = operaciones[y][9] # guarda actividad pausa
                                        for y in range(larg):
                                            if(f0==operaciones[y][0]):
                                                rf0 = operaciones[y][2] # guarda recurso actividad a comparar
                                                ap0 = operaciones[y][9] # guarda actividad pausa

                                            if(f0==operaciones[y][9]) and (f0!='-'):
                                                rf0 = operaciones[y][2] # guarda recurso pausa a comparar
                                                ap0 = operaciones[y][9] # guarda pausa

                                        if(f1!=f0): # si no son iguales

                                            if(f0=='-'):
                                                bandera = bandera

                                            if(f0=='A'):
                                                bandera = bandera

                                            if (f0!='-') and (f0!='A'): # salvedad guion y A

                                                if(rf1==rf0): # si usan el mismo recurso
                                                        bandera = bandera + 1     

                                        if(f1!='-' and f1!='q'): # salvedad guion y q
                                            if f1==f0: # si son iguales
                                                bandera = bandera + 1

                                        aux = aux - 1

                                    else:

                                        aux = aux - 1
                                        break

                                contadoraux = contadoraux + 1
                                auxdu = auxdu + 1

                            if(limit>=bloquet): # restriccion fin del turno

                                x = 1
                                break

                            else: # guarda en la matriz

                                if (bandera==0):
                                    cont = 0
                                    while(cont<duracion):

                                        if(limit>=bloquet): # restriccion fin del turno

                                            x = 1
                                            break

                                        #guarda almuerzo

                                        auxalmu = f1
        
                                        if (almuerzo==1): #tipo 1
                                            if(limit==13):
                                                if (auxalmu in otros):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2
                                                    x=0
                                                    duracion = duracion - cont
                                                    break
                                            if(limit==11):
                                                if (auxalmu in jumbos):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2
                                                    x=0
                                                    duracion = duracion - cont
                                                    break
                                            if(limit==9):
                                                if (auxalmu in cuadrilla):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2
                                                    x=0
                                                    duracion = duracion - cont
                                                    break

                                        if (almuerzo==2): #tipo 2
                                            if(limit==13):
                                                if (auxalmu in otros):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2
                                                    x=0
                                                    duracion = duracion - cont
                                                    break
                                            if(limit==11):
                                                if (auxalmu in cuadrilla):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2
                                                    x=0
                                                    duracion = duracion - cont
                                                    break
                                            if(limit==9):
                                                if (auxalmu in jumbos):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2
                                                    x=0
                                                    duracion = duracion - cont
                                                    break

                                        if (almuerzo==3): #tipo 3
                                            if(limit==13):
                                                if (auxalmu in jumbos):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2
                                                    x=0
                                                    duracion = duracion - cont
                                                    break
                                            if(limit==11):
                                                if (auxalmu in cuadrilla):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2
                                                    x=0
                                                    duracion = duracion - cont
                                                    break
                                            if(limit==9):
                                                if (auxalmu in otros):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2
                                                    x=0
                                                    duracion = duracion - cont
                                                    break

                                            laux.append(f1)
                                            limit = limit + 1
                                            cont = cont + 1

                                    if(cont==duracion):
                                        x = 1

                                if (bandera>0):

                                    #guarda almuerzo

                                    auxalmu = f1

                                    if (almuerzo==1): #tipo 1
                                        if(limit==13):
                                            if (auxalmu in otros):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==11):
                                            if (auxalmu in jumbos):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==9):
                                            if (auxalmu in cuadrilla):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2

                                    if (almuerzo==2): #tipo 2
                                        if(limit==13):
                                            if (auxalmu in otros):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==11):
                                            if (auxalmu in cuadrilla):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==9):
                                            if (auxalmu in jumbos):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2

                                    if (almuerzo==3): #tipo 3
                                        if(limit==13):
                                            if (auxalmu in jumbos):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==11):
                                            if (auxalmu in cuadrilla):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==9):
                                            if (auxalmu in otros):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2

                                    laux.append('-')
                                    limit = limit + 1

                            if(auxdu==duracion+pausa) and (bandera == 0):
                                    
                                #estado_avance = 0  where id_frente = lr[i][0] 

                                if(pausa>0):
                                    auxpa = 0
                                    while (auxpa<pausa):
                                        if(limit<bloquet): # restriccion fin del turno

                                            #guarda almuerzo

                                            auxalmu = f1
            
                                            if (almuerzo==1): #tipo 1
                                                if(limit==13):
                                                    if (auxalmu in otros):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2
                                                if(limit==11):
                                                    if (auxalmu in jumbos):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2
                                                if(limit==9):
                                                    if (auxalmu in cuadrilla):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2

                                            if (almuerzo==2): #tipo 2
                                                if(limit==13):
                                                    if (auxalmu in otros):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2
                                                if(limit==11):
                                                    if (auxalmu in cuadrilla):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2
                                                if(limit==9):
                                                    if (auxalmu in jumbos):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2

                                            if (almuerzo==3): #tipo 3
                                                if(limit==13):
                                                    if (auxalmu in jumbos):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2
                                                if(limit==11):
                                                    if (auxalmu in cuadrilla):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2
                                                if(limit==9):
                                                    if (auxalmu in otros):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2

                                            laux.append(ap1)
                                            limit = limit + 1
                                            auxpa = auxpa + 1

                                        else:
                                            auxpa = auxpa + 1
                                        
                            # guardar contav (nuevo estado_avance) where id_frente = lr[i][0] a la BD            
                                

                    if (parcial=='no'): #no parcial

                        contav = 0

                        f1 = ciclos[fortycic][2][po-contador]

                        if(f1=='q'):
                            qhecha='si'
                            break

                        x=0

                        if(limit+duracion+pausa<bloquet): # restriccion final des turno no parciales

                            while(x==0): # busqueda vertical total

                                #guarda almuerzo

                                auxalmu = f1

                                if (almuerzo==1): #tipo 1
                                    if(limit==13):
                                        if (auxalmu in otros):
                                            laux.append('A')
                                            laux.append('A')
                                            limit = limit + 2
                                    if(limit==11):
                                        if (auxalmu in jumbos):
                                            laux.append('A')
                                            laux.append('A')
                                            limit = limit + 2
                                    if(limit==9):
                                        if (auxalmu in cuadrilla):
                                            laux.append('A')
                                            laux.append('A')
                                            limit = limit + 2

                                if (almuerzo==2): #tipo 2
                                    if(limit==13):
                                        if (auxalmu in otros):
                                            laux.append('A')
                                            laux.append('A')
                                            limit = limit + 2
                                    if(limit==11):
                                        if (auxalmu in cuadrilla):
                                            laux.append('A')
                                            laux.append('A')
                                            limit = limit + 2
                                    if(limit==9):
                                        if (auxalmu in jumbos):
                                            laux.append('A')
                                            laux.append('A')
                                            limit = limit + 2

                                if (almuerzo==3): #tipo 3
                                    if(limit==13):
                                        if (auxalmu in jumbos):
                                            laux.append('A')
                                            laux.append('A')
                                            limit = limit + 2
                                    if(limit==11):
                                        if (auxalmu in cuadrilla):
                                            laux.append('A')
                                            laux.append('A')
                                            limit = limit + 2
                                    if(limit==9):
                                        if (auxalmu in otros):
                                            laux.append('A')
                                            laux.append('A')
                                            limit = limit + 2

                                contadoraux = limit
                                auxdu = esav
                                bandera = 0

                                while(auxdu<duracion+pausa): # busqueda vertical total

                                    # busqueda vertical fila

                                    aux = i-1

                                    while (aux>=0):

                                        if(limit<bloquet) and (contadoraux<bloquet): # restriccion fin del turno

                                            f0 = l1[aux][contadoraux]

                                            for y in range(cicloclasic): 
                                                if(f1==operaciones[y][0]):
                                                    rf1 = operaciones[y][2] # guarda recurso actividad
                                                    ap1 = operaciones[y][9] # guarda actividad pausa
                                            for y in range(larg):
                                                if(f0==operaciones[y][0]):
                                                    rf0 = operaciones[y][2] # guarda recurso actividad a comparar
                                                    ap0 = operaciones[y][9] # guarda actividad pausa

                                                if(f0==operaciones[y][9]) and (f0!='-'):
                                                    rf0 = operaciones[y][2] # guarda recurso pausa a comparar
                                                    ap0 = operaciones[y][9] # guarda pausa

                                            if(f1!=f0): # si no son iguales

                                                if(f0=='-'):
                                                    bandera = bandera

                                                if(f0=='A'):
                                                    bandera = bandera

                                                if (f0!='-') and (f0!='A'): # salvedad guion y A

                                                    if(rf1==rf0): # si usan el mismo recurso
                                                            bandera = bandera + 1   

                                            if(f1!='-' and f1!='q'): # salvedad guion y q
                                                if f1==f0: # si son iguales
                                                    bandera = bandera + 1
                                            
                                            aux = aux - 1

                                        else :

                                            aux = aux - 1
                                            break

                                    contadoraux = contadoraux + 1
                                    auxdu = auxdu + 1

                                if(limit>=bloquet): # restriccion fin del turno

                                    x = 1
                                    break

                                else: # guarda en la matriz

                                    #guarda almuerzo

                                    auxalmu = f1

                                    if (almuerzo==1): #tipo 1
                                        if(limit==13):
                                            if (auxalmu in otros):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==11):
                                            if (auxalmu in jumbos):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==9):
                                            if (auxalmu in cuadrilla):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2

                                    if (almuerzo==2): #tipo 2
                                        if(limit==13):
                                            if (auxalmu in otros):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==11):
                                            if (auxalmu in cuadrilla):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==9):
                                            if (auxalmu in jumbos):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2

                                    if (almuerzo==3): #tipo 3
                                        if(limit==13):
                                            if (auxalmu in jumbos):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==11):
                                            if (auxalmu in cuadrilla):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==9):
                                            if (auxalmu in otros):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2

                                    if (bandera==0):
                                        cont = 0
                                        while(cont<duracion):

                                            if(limit>=bloquet): # restriccion fin del turno

                                                x = 1
                                                break
                                            
                                            laux.append(f1)
                                            limit = limit + 1
                                            cont = cont + 1
                                        
                                        if(cont==duracion):
                                            x = 1

                                    if (bandera>0):

                                        laux.append('-')
                                        limit = limit + 1

                                if(auxdu==duracion+pausa) and (bandera == 0):

                                    #estado_avance = 0  where id_frente = lr[i][0]

                                    if(pausa>0):
                                        auxpa = 0
                                        while (auxpa<pausa):
                                            if(limit<bloquet): # restriccion fin del turno

                                                laux.append(ap1)
                                                limit = limit + 1
                                                auxpa = auxpa + 1

                                            else:

                                                axupa = auxpa + 1

                                # guardar contav (nuevo estado_avance) where id_frente = lr[i][0] a la BD 

                        if(limit+duracion+pausa>=bloquet):
        
                            if(limit<bloquet): # restriccion fin del turno

                                #guarda almuerzo

                                auxalmu = f1

                                if (almuerzo==1): #tipo 1
                                    if(limit==13):
                                        if (auxalmu in otros):
                                            laux.append('A')
                                            laux.append('A')
                                            limit = limit + 2
                                    if(limit==11):
                                        if (auxalmu in jumbos):
                                            laux.append('A')
                                            laux.append('A')
                                            limit = limit + 2
                                    if(limit==9):
                                        if (auxalmu in cuadrilla):
                                            laux.append('A')
                                            laux.append('A')
                                            limit = limit + 2

                                if (almuerzo==2): #tipo 2
                                    if(limit==13):
                                        if (auxalmu in otros):
                                            laux.append('A')
                                            laux.append('A')
                                            limit = limit + 2
                                    if(limit==11):
                                        if (auxalmu in cuadrilla):
                                            laux.append('A')
                                            laux.append('A')
                                            limit = limit + 2
                                    if(limit==9):
                                        if (auxalmu in jumbos):
                                            laux.append('A')
                                            laux.append('A')
                                            limit = limit + 2

                                if (almuerzo==3): #tipo 3
                                    if(limit==13):
                                        if (auxalmu in jumbos):
                                            laux.append('A')
                                            laux.append('A')
                                            limit = limit + 2
                                    if(limit==11):
                                        if (auxalmu in cuadrilla):
                                            laux.append('A')
                                            laux.append('A')
                                            limit = limit + 2
                                    if(limit==9):
                                        if (auxalmu in otros):
                                            laux.append('A')
                                            laux.append('A')
                                            limit = limit + 2

                                laux.append('-')
                                limit = limit + 1

                if(k+posi>=larg):
        
                    if(lr[i][2]!='q') and (qhecha=='si'):

                        # guarda q al final

                        indite = len(laux[i])

                        num = bloquet - indite

                        while (num>0):

                            if(limit<bloquet):

                                if (num == 1):
                                    laux.append(f1)
                                    limit = limit + 1

                                if (num !=1):

                                    #guarda almuerzo

                                    auxalmu = f1

                                    if (almuerzo==1): #tipo 1
                                        if(limit==13):
                                            if (auxalmu in otros):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==11):
                                            if (auxalmu in jumbos):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==9):
                                            if (auxalmu in cuadrilla):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2

                                    if (almuerzo==2): #tipo 2
                                        if(limit==13):
                                            if (auxalmu in otros):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==11):
                                            if (auxalmu in cuadrilla):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==9):
                                            if (auxalmu in jumbos):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2

                                    if (almuerzo==3): #tipo 3
                                        if(limit==13):
                                            if (auxalmu in jumbos):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==11):
                                            if (auxalmu in cuadrilla):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==9):
                                            if (auxalmu in otros):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2

                                    laux[i].append('-')
                                    limit = limit + 1

                            num = num - 1
                                    
                        if (num == 0):
                            break

                    if(lr[i][2]=='q'):

                        po=k

                        if(po<larg):

                            esav = int(lr[i][3]) # rescata estado avance operacion

                            # rescata recurso, duracion segun tamaño y si es parcial o no 

                            cicloclasic = 15 # longitud ciclo original para comparar

                            for l in range(cicloclasic):
                                if (lr[i][1]=='C'):
                                    if (ciclos[fortycic][2][po]==operaciones[l][0]):
                                        duracion = int(operaciones[l][3])
                                        pausa = int(operaciones[l][7])
                                        parcial = operaciones[l][8]

                                if (lr[i][1]=='M'):
                                    if (ciclos[fortycic][2][po]==operaciones[l][0]):
                                        duracion = int(operaciones[l][4])
                                        pausa = int(operaciones[l][7])
                                        parcial = operaciones[l][8]

                                if (lr[i][1]=='G'):
                                    if (ciclos[fortycic][2][po]==operaciones[l][0]):
                                        duracion = int(operaciones[l][5])
                                        pausa = int(operaciones[l][7])
                                        parcial = operaciones[l][8]

                            # repetidor para cantidad de bloques por actividad

                            if (parcial=='si'): #parcial
                                
                                contav = 0
                                
                                f1 = ciclos[fortycic][2][po-contador]
                                
                                x = 0

                                while(x==0): # busqueda vertical total

                                    #guarda almuerzo

                                    auxalmu = f1

                                    if (almuerzo==1): #tipo 1
                                        if(limit==13):
                                            if (auxalmu in otros):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==11):
                                            if (auxalmu in jumbos):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==9):
                                            if (auxalmu in cuadrilla):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2

                                    if (almuerzo==2): #tipo 2
                                        if(limit==13):
                                            if (auxalmu in otros):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==11):
                                            if (auxalmu in cuadrilla):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==9):
                                            if (auxalmu in jumbos):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2

                                    if (almuerzo==3): #tipo 3
                                        if(limit==13):
                                            if (auxalmu in jumbos):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==11):
                                            if (auxalmu in cuadrilla):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2
                                        if(limit==9):
                                            if (auxalmu in otros):
                                                laux.append('A')
                                                laux.append('A')
                                                limit = limit + 2

                                    contadoraux = limit
                                    auxdu = esav
                                    bandera = 0


                                    while(auxdu<duracion+pausa): # busqueda vertical total

                                        # busqueda vertical fila

                                        aux = i-1

                                        while (aux>=0):

                                            if(limit<bloquet) and (contadoraux<bloquet): # restriccion fin del turno
                                                
                                                f0 = l1[aux][contadoraux]

                                                for y in range(cicloclasic): 
                                                    if(f1==operaciones[y][0]):
                                                        rf1 = operaciones[y][2] # guarda recurso actividad
                                                        ap1 = operaciones[y][9] # guarda actividad pausa
                                                for y in range(larg):
                                                    if(f0==operaciones[y][0]):
                                                        rf0 = operaciones[y][2] # guarda recurso actividad a comparar
                                                        ap0 = operaciones[y][9] # guarda actividad pausa

                                                    if(f0==operaciones[y][9]) and (f0!='-'):
                                                        rf0 = operaciones[y][2] # guarda recurso pausa a comparar
                                                        ap0 = operaciones[y][9] # guarda pausa

                                                if(f1!=f0): # si no son iguales

                                                    if(f0=='-'):
                                                        bandera = bandera

                                                    if(f0=='A'):
                                                        bandera = bandera

                                                    if (f0!='-') and (f0!='A'): # salvedad guion y A

                                                        if(rf1==rf0): # si usan el mismo recurso
                                                                bandera = bandera + 1     

                                                if(f1!='-' and f1!='q'): # salvedad guion y q
                                                    if f1==f0: # si son iguales
                                                        bandera = bandera + 1
                                                
                                                aux = aux - 1

                                            else:

                                                aux = aux - 1
                                                break

                                        contadoraux = contadoraux + 1
                                        auxdu = auxdu + 1

                                    if(limit>=bloquet): # restriccion fin del turno

                                        x = 1
                                        break

                                    else: # guarda en la matriz

                                        if (bandera==0):
                                            cont = 0
                                            while(cont<duracion):

                                                if(limit>=bloquet): # restriccion fin del turno

                                                    x = 1
                                                    break

                                                #guarda almuerzo

                                                auxalmu = f1
                
                                                if (almuerzo==1): #tipo 1
                                                    if(limit==13):
                                                        if (auxalmu in otros):
                                                            laux.append('A')
                                                            laux.append('A')
                                                            limit = limit + 2
                                                            x=0
                                                            duracion = duracion - cont
                                                            break
                                                    if(limit==11):
                                                        if (auxalmu in jumbos):
                                                            laux.append('A')
                                                            laux.append('A')
                                                            limit = limit + 2
                                                            x=0
                                                            duracion = duracion - cont
                                                            break
                                                    if(limit==9):
                                                        if (auxalmu in cuadrilla):
                                                            laux.append('A')
                                                            laux.append('A')
                                                            limit = limit + 2
                                                            x=0
                                                            duracion = duracion - cont
                                                            break

                                                if (almuerzo==2): #tipo 2
                                                    if(limit==13):
                                                        if (auxalmu in otros):
                                                            laux.append('A')
                                                            laux.append('A')
                                                            limit = limit + 2
                                                            x=0
                                                            duracion = duracion - cont
                                                            break
                                                    if(limit==11):
                                                        if (auxalmu in cuadrilla):
                                                            laux.append('A')
                                                            laux.append('A')
                                                            limit = limit + 2
                                                            x=0
                                                            duracion = duracion - cont
                                                            break
                                                    if(limit==9):
                                                        if (auxalmu in jumbos):
                                                            laux.append('A')
                                                            laux.append('A')
                                                            limit = limit + 2
                                                            x=0
                                                            duracion = duracion - cont
                                                            break

                                                if (almuerzo==3): #tipo 3
                                                    if(limit==13):
                                                        if (auxalmu in jumbos):
                                                            laux.append('A')
                                                            laux.append('A')
                                                            limit = limit + 2
                                                            x=0
                                                            duracion = duracion - cont
                                                            break
                                                    if(limit==11):
                                                        if (auxalmu in cuadrilla):
                                                            laux.append('A')
                                                            laux.append('A')
                                                            limit = limit + 2
                                                            x=0
                                                            duracion = duracion - cont
                                                            break
                                                    if(limit==9):
                                                        if (auxalmu in otros):
                                                            laux.append('A')
                                                            laux.append('A')
                                                            limit = limit + 2
                                                            x=0
                                                            duracion = duracion - cont
                                                            break

                                                laux.append(f1)
                                                limit = limit + 1
                                                cont = cont + 1

                                            if(cont==duracion):
                                                x = 1

                                        if (bandera>0):

                                            #guarda almuerzo

                                            auxalmu = f1
            
                                            if (almuerzo==1): #tipo 1
                                                if(limit==13):
                                                    if (auxalmu in otros):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2
                                                if(limit==11):
                                                    if (auxalmu in jumbos):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2
                                                if(limit==9):
                                                    if (auxalmu in cuadrilla):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2

                                            if (almuerzo==2): #tipo 2
                                                if(limit==13):
                                                    if (auxalmu in otros):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2
                                                if(limit==11):
                                                    if (auxalmu in cuadrilla):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2
                                                if(limit==9):
                                                    if (auxalmu in jumbos):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2

                                            if (almuerzo==3): #tipo 3
                                                if(limit==13):
                                                    if (auxalmu in jumbos):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2
                                                if(limit==11):
                                                    if (auxalmu in cuadrilla):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2
                                                if(limit==9):
                                                    if (auxalmu in otros):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2

                                            laux.append('-')
                                            limit = limit + 1

                                    if(auxdu==duracion+pausa) and (bandera == 0):
                                            
                                        #estado_avance = 0  where id_frente = lr[i][0] 

                                        if(pausa>0):
                                            auxpa = 0
                                            while (auxpa<pausa):
                                                if(limit<bloquet): # restriccion fin del turno

                                                    #guarda almuerzo

                                                    auxalmu = f1
                    
                                                    if (almuerzo==1): #tipo 1
                                                        if(limit==13):
                                                            if (auxalmu in otros):
                                                                laux.append('A')
                                                                laux.append('A')
                                                                limit = limit + 2
                                                        if(limit==11):
                                                            if (auxalmu in jumbos):
                                                                laux.append('A')
                                                                laux.append('A')
                                                                limit = limit + 2
                                                        if(limit==9):
                                                            if (auxalmu in cuadrilla):
                                                                laux.append('A')
                                                                laux.append('A')
                                                                limit = limit + 2

                                                    if (almuerzo==2): #tipo 2
                                                        if(limit==13):
                                                            if (auxalmu in otros):
                                                                laux.append('A')
                                                                laux.append('A')
                                                                limit = limit + 2
                                                        if(limit==11):
                                                            if (auxalmu in cuadrilla):
                                                                laux.append('A')
                                                                laux.append('A')
                                                                limit = limit + 2
                                                        if(limit==9):
                                                            if (auxalmu in jumbos):
                                                                laux.append('A')
                                                                laux.append('A')
                                                                limit = limit + 2

                                                    if (almuerzo==3): #tipo 3
                                                        if(limit==13):
                                                            if (auxalmu in jumbos):
                                                                laux.append('A')
                                                                laux.append('A')
                                                                limit = limit + 2
                                                        if(limit==11):
                                                            if (auxalmu in cuadrilla):
                                                                laux.append('A')
                                                                laux.append('A')
                                                                limit = limit + 2
                                                        if(limit==9):
                                                            if (auxalmu in otros):
                                                                laux.append('A')
                                                                laux.append('A')
                                                                limit = limit + 2

                                                    laux.append(ap1)
                                                    limit = limit + 1
                                                    auxpa = auxpa + 1

                                                else:
                                                    auxpa = auxpa + 1
                                                
                                    # guardar contav (nuevo estado_avance) where id_frente = lr[i][0] a la BD 
                                            

                            if (parcial=='no'): #no parcial

                                contav = 0

                                f1 = ciclos[fortycic][2][po-contador]

                                x=0

                                if(limit+duracion+pausa<bloquet): # restriccion final des turno no parciales

                                    while(x==0): # busqueda vertical total

                                        #guarda almuerzo

                                        auxalmu = f1

                                        if (almuerzo==1): #tipo 1
                                            if(limit==13):
                                                if (auxalmu in otros):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2
                                            if(limit==11):
                                                if (auxalmu in jumbos):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2
                                            if(limit==9):
                                                if (auxalmu in cuadrilla):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2

                                        if (almuerzo==2): #tipo 2
                                            if(limit==13):
                                                if (auxalmu in otros):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2
                                            if(limit==11):
                                                if (auxalmu in cuadrilla):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2
                                            if(limit==9):
                                                if (auxalmu in jumbos):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2

                                        if (almuerzo==3): #tipo 3
                                            if(limit==13):
                                                if (auxalmu in jumbos):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2
                                            if(limit==11):
                                                if (auxalmu in cuadrilla):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2
                                            if(limit==9):
                                                if (auxalmu in otros):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2

                                        contadoraux = limit
                                        auxdu = esav
                                        bandera = 0 

                                        while(auxdu<duracion+pausa): # busqueda vertical total

                                            # busqueda vertical fila

                                            aux = i-1

                                            while (aux>=0):

                                                if(limit<bloquet) and (contadoraux<bloquet): # restriccion fin del turno

                                                    f0 = l1[aux][contadoraux]

                                                    for y in range(cicloclasic): 
                                                        if(f1==operaciones[y][0]):
                                                            rf1 = operaciones[y][2] # guarda recurso actividad
                                                            ap1 = operaciones[y][9] # guarda actividad pausa
                                                    for y in range(larg):
                                                        if(f0==operaciones[y][0]):
                                                            rf0 = operaciones[y][2] # guarda recurso actividad a comparar
                                                            ap0 = operaciones[y][9] # guarda actividad pausa

                                                        if(f0==operaciones[y][9]) and (f0!='-'):
                                                            rf0 = operaciones[y][2] # guarda recurso pausa a comparar
                                                            ap0 = operaciones[y][9] # guarda pausa

                                                    if(f1!=f0): # si no son iguales

                                                        if(f0=='-'):
                                                            bandera = bandera

                                                        if(f0=='A'):
                                                            bandera = bandera

                                                        if (f0!='-') and (f0!='A'): # salvedad guion y A

                                                            if(rf1==rf0): # si usan el mismo recurso
                                                                    bandera = bandera + 1       

                                                    if(f1!='-' and f1!='q'): # salvedad guion y q
                                                        if f1==f0: # si son iguales
                                                            bandera = bandera + 1
                                                    
                                                    aux = aux - 1

                                                else :

                                                    aux = aux - 1
                                                    break

                                            contadoraux = contadoraux + 1
                                            auxdu = auxdu + 1

                                        if(limit>=bloquet): # restriccion fin del turno

                                            x = 1
                                            break

                                        else: # guarda en la matriz
                                            
                                            #guarda almuerzo

                                            auxalmu = f1

                                            if (almuerzo==1): #tipo 1
                                                if(limit==13):
                                                    if (auxalmu in otros):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2
                                                if(limit==11):
                                                    if (auxalmu in jumbos):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2
                                                if(limit==9):
                                                    if (auxalmu in cuadrilla):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2

                                            if (almuerzo==2): #tipo 2
                                                if(limit==13):
                                                    if (auxalmu in otros):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2
                                                if(limit==11):
                                                    if (auxalmu in cuadrilla):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2
                                                if(limit==9):
                                                    if (auxalmu in jumbos):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2

                                            if (almuerzo==3): #tipo 3
                                                if(limit==13):
                                                    if (auxalmu in jumbos):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2
                                                if(limit==11):
                                                    if (auxalmu in cuadrilla):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2
                                                if(limit==9):
                                                    if (auxalmu in otros):
                                                        laux.append('A')
                                                        laux.append('A')
                                                        limit = limit + 2

                                            if (bandera==0):
                                                cont = 0
                                                while(cont<duracion):

                                                    if(limit>=bloquet): # restriccion fin del turno

                                                        x = 1
                                                        break
                                                    
                                                    laux.append(f1)
                                                    limit = limit + 1
                                                    cont = cont + 1
                                                
                                                if(cont==duracion):
                                                    x = 1

                                            if (bandera>0):

                                                laux.append('-')
                                                limit = limit + 1

                                        if(auxdu==duracion+pausa) and (bandera == 0):

                                            #estado_avance = 0  where id_frente = lr[i][0]

                                            if(pausa>0):
                                                auxpa = 0
                                                while (auxpa<pausa):
                                                    if(limit<bloquet): # restriccion fin del turno

                                                        laux.append(ap1)
                                                        limit = limit + 1
                                                        auxpa = auxpa + 1

                                                    else:

                                                        axupa = auxpa + 1

                                        # guardar contav (nuevo estado_avance) where id_frente = lr[i][0] a la BD 

                                if(limit+duracion+pausa>=bloquet):
                
                                    if(limit<bloquet): # restriccion fin del turno

                                        #guarda almuerzo

                                        auxalmu = f1

                                        if (almuerzo==1): #tipo 1
                                            if(limit==13):
                                                if (auxalmu in otros):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2
                                            if(limit==11):
                                                if (auxalmu in jumbos):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2
                                            if(limit==9):
                                                if (auxalmu in cuadrilla):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2

                                        if (almuerzo==2): #tipo 2
                                            if(limit==13):
                                                if (auxalmu in otros):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2
                                            if(limit==11):
                                                if (auxalmu in cuadrilla):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2
                                            if(limit==9):
                                                if (auxalmu in jumbos):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2

                                        if (almuerzo==3): #tipo 3
                                            if(limit==13):
                                                if (auxalmu in jumbos):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2
                                            if(limit==11):
                                                if (auxalmu in cuadrilla):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2
                                            if(limit==9):
                                                if (auxalmu in otros):
                                                    laux.append('A')
                                                    laux.append('A')
                                                    limit = limit + 2

                                        laux.append('-')
                                        limit = limit + 1

            contaciclo = 0
            contaguion = 0

            print ("laux", laux)
            print ("ciclo", q)

            for c in range(len(laux)):
                if(laux[c]!='-'):
                    contaciclo = contaciclo + 1
                if(laux[c]=='-'):
                    contaguion = contaguion + 1

            if(contaciclo>xci):
                xci=contaciclo
                l1[i].clear()
                l1[i] = copy.deepcopy(laux)
                print ("FORTIFICACION = ", lr[i][4],"MEJOR CICLO = ", q)


            laux.clear()

            # imprimir matriz 1 (ordenamiento)

            print("[ ID - TAM - OPE - EST - FOR -08:00-08:30-09:00-09:30-10:00-10:30-11:00-11:30-12:00-12:30-13:00-13:30-14:00-14:30-15:00-15:30-16:00-16:30-17:00-17:30-18:00-18:30-19:00-19:30]")
            
            for n in range(totalfrentes):
                print(lr[n],l1[n],len(l1[n]))
        

                
                
                

                
                                                

    # imprimir matriz 1 (ordenamiento)

    print("[ ID - TAM - OPE - EST - FOR -08:00-08:30-09:00-09:30-10:00-10:30-11:00-11:30-12:00-12:30-13:00-13:30-14:00-14:30-15:00-15:30-16:00-16:30-17:00-17:30-18:00-18:30-19:00-19:30]")
    
    for i in range(totalfrentes):
        print(lr[i],l1[i],len(l1[i]))

    print ("ALMUERZO 1 RECURSO: ", recualmu)
    
    
    excel = openpyxl.load_workbook('base.xlsx')
    hoja = excel.active
    for i in range(totalfrentes):
        for j in range(termino):
            hoja.cell(row=i+9,column=j+3).value = l1[i][j]

    for i in range(totalfrentes):
        hoja.cell(row=i+9,column=2).value = lr[i][0]
    

    excel.save("turno prototipo .xls") 
    
    for i in range(termino):
        matricitaa2.append(lr[i])
    for i in range (totalfrentes):
        matricitaa.append(l1[i])
        
    print('matricitaa')
    print(matricitaa)
    
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
    def verfrentesmenu():
        print('entro vf')
    def addfrentesmenu():
        win5 = Tk()
        win5.title('AÑADIR FRENTE')
        frame = Frame(win5)
        frame.pack()
        txtid= Label(frame,text='Id frente',width='23')
        txtid.grid(column='0',row='0')
        txttipo = Label(frame,text='Tipo',width='23')
        txttipo.grid(column='0',row='1')
        txtsigla = Label(frame,text='Sigla',width='23')
        txtsigla.grid(column='0',row='2')
        txtnumero = Label(frame,text='Numero',width='23')
        txtnumero.grid(column='0',row='3')
        txtnumeroref = Label(frame,text='Numero referencia',width='23')
        txtnumeroref.grid(column='0',row='4')
        txtdir = Label(frame,text='Direccion',width='23')
        txtdir.grid(column='0',row='5')
        txtdirref = Label(frame,text='Direccion referencia',width='23')
        txtdirref.grid(column='0',row='6')
        txtestado = Label(frame,text='Estado',width='23')
        txtestado.grid(column='0',row='7')
        txttam = Label(frame,text='Tamaño',width='23')
        txttam.grid(column='0',row='8')
        txtruta = Label(frame,text='Ruta critica',width='23')
        txtruta.grid(column='0',row='9')
        txtdmarina = Label(frame,text='Distancia marina',width='23')
        txtdmarina.grid(column='0',row='10')
        txtnivel = Label(frame,text='Tipo',width='23')
        txtnivel.grid(column='0',row='11')
        txtmacrob = Label(frame,text='Macrobloque',width='23')
        txtmacrob.grid(column='0',row='12')
        txtsector = Label(frame,text='Sector',width='23')
        txtsector.grid(column='0',row='13')
        txtcodigo = Label(frame,text='Codigo',width='23')
        txtcodigo.grid(column='0',row='14')
        txtfortificacion = Label(frame,text='Fortificacion',width='23')
        txtfortificacion.grid(column='0',row='15')
        txtciclo = Label(frame,text='Ciclo',width='23')
        txtciclo.grid(column='0',row='16')
        txtcriticidad = Label(frame,text='Criticidad',width='23')
        txtcriticidad.grid(column='0',row='17')
        

        entryid = Entry(frame,width='23')
        entryid.grid(column='1',row='0')
    
    #codigo de la ventana principal
    rutt=rut
    win3 = Tk()
    win3.title('PROGRAMACION MINERA CAVES IA')
    win3.config(bg="cornflowerblue")
    win3.geometry('500x300')
    framemain = Frame(win3)
    framemain.pack(expand=1)
    framemain.config(bg="royalblue", width="500", height="300", relief="sunken")
    menubar = Menu(win3)
    win3.config(menu=menubar)
    menufrentes=Menu(menubar)
    menuequipos=Menu(menubar)
    menubar.add_cascade(label='frentes',menu=menufrentes)
    menubar.add_cascade(label='equipos',menu=menuequipos)
    menufrentes.add_command(label='añadir nueva frente',command=addfrentesmenu)
    menufrentes.add_command(label='ver frentes',command=verfrentesmenu)
    menuequipos.add_command(label='añadir equipo')
    menuequipos.add_command(label='ver equipo')
    def addestadofrentes(frente,operacion):
        bd15 = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='cavesbd',
                             cursorclass=pymysql.cursors.DictCursor)

        print(frente,operacion)
        fecha = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        print(fecha)
        cursor = bd15.cursor()
        sql = "insert into estado_frentes(id_frente,operacion,fecha) value('%s','%s','%s')" % (frente, operacion, fecha)
        try:
            
            cursor.execute(sql)
            bd15.commit()
            cursor.close()
            
        
        except Exception as e:
            print(e)
        bd15.close()
       
        
        
    def verfrentes():
        numfilas = 0
        numcolumnas = 2
        win4 = Tk()
        win4.title('Estados de frente')
        datos=Frame(win4)
        datos.pack()
        nid = Label(datos,text='  id Frente           ')
        nid.grid(row='0',column='0')
        nop = Label(datos,text='operacion anterior')
        nop.grid(row='0',column='1')
        tabla=Frame(win4)
        tabla.pack()
        def creartablafrentes():
            
            

            

            
            for f in range(numfilas):
                for j in range(numcolumnas):
                        x = Entry(tabla)
                        x.grid(row = f, column = j)
                        if (j==0):
                                x.insert(END,ides1[f])
                        if (j==1):
                                x.insert(END,operaciones1[f])
                        x.config(state='readonly')     
        cursor = bd3.cursor()
        cursor2 =  bd3.cursor()
        sql2 = 'SELECT * from estado_frentes'
        sql = 'SELECT * from frentes'
        try:
            cursor.execute(sql)
            cursor2.execute(sql2)
            data = cursor.fetchall()
            dataprint = cursor2.fetchall()
            for p in data:
                codigo=p['codigo_empresa']
                if (codigo==rutt):
                    numfilas = numfilas + 1

            for i in data:
                id = i['id_frente']
                codigo=i['codigo_empresa']
                nivel=i['nivel']
                if(codigo==rutt):
                    ides1.append(id)
                    niveles1.append(nivel)
            for i in dataprint:
                operacion = i['operacion']
                idfren = i['id_frente']
                ciclo = i ['ciclo']
                for j in ides1:
                    if(idfren==j):
                        ciclos1.append(ciclo)
                        operaciones1.append(operacion)
            cursor.close()
            bd3.commit()
            bd3.close
        except Exception as e:
            print(e)
        
        creartablafrentes()
       
        
    def ordenarsegunnivel(ides1,operaciones1,niveles):
        tamaño = len(ides1)
        
        print(tamaño)
        for i in range(tamaño):
            busqueda = niveles1[i]
            if(busqueda=='HD'):
                ordenHD.append(ides1[i])
                opHD.append(operaciones1[i])
            if(busqueda=='CH'):
                ordenCH.append(ides1[i])
                opCH.append(operaciones1[i])
            if(busqueda=='EXT'):
                ordenEXT.append(ides1[i])
                opEXT.append(operaciones1[i])
            if(busqueda=='INY'):
                ordenINY.append(ides1[i])
                opINY.append(operaciones1[i])
            if(busqueda=='PD'):
                ordenPD.append(ides1[i])
                opPD.append(operaciones1[i])
            if(busqueda=='TI'):
                ordenTI.append(ides1[i])
                opTI.append(operaciones1[i])
    

   #añadir atributo tipofort en tabla frentes
    def inputdata():
        def pushfrente(frente,ciclo):
            print('push',frente,ciclo)
            tam = len(ciclosyfrentes)
            for i in range(0,tam):
                if (ciclosyfrentes[i][0]==frente):
                    ciclosyfrentes[i].append(ciclo)
            print(ciclosyfrentes)
        def quefortes(frente):
            for i in tipopmsh:
                if(frente==i):
                    return 'p-m-sh' 
            for i in tipopshf:
                if(frente==i):
                    return 'p-shf'
            for i in tiposhfpmsh:
                if(frente==i):
                    return 'shf-p-m-sh'
        def quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa):
            fort = quefortes(frente)
            lista = list()
            lista.append(pp)
            lista.append(l)
            lista.append(m)
            lista.append(mt)
            lista.append(h)
            lista.append(psh)
            lista.append(pa)
            
            
            for i in range(len(lista)):
                aux = lista[i]
                if(aux=='si'): 
                    lista[i]='1'
                if(aux=='no'):
                    lista[i]='0'
            
            if(operacion=='perforacion_pernos'):
                match fort:
                    case 'p-m-sh':
                        ciclo = 1
                        pushfrente(frente,ciclo)
                    case 'p-shf':
                        unos = 0
                        for i in lista:
                            if(i=='1'):
                                unos = unos + 1
                        print(unos)
                        if(unos==1):
                            print('ciclo 4,5,6')
                            ciclo = 4
                            pushfrente(frente,ciclo)

                            
                        if(unos==2):
                            print('ciclo 1,2')
                            ciclo = 1
                            pushfrente(frente,ciclo)
                            
                        if(unos==3):
                            print('ciclo 3')
                            ciclo = 3
                            pushfrente(frente,ciclo)
                           
                    case 'shf-p-m-sh':
                        unos = 0
                        for i in lista:
                            if(i=='1'):
                                unos = unos + 1
                        print(unos)
                        if(unos==1):
                            print('ciclo 1')
                            ciclo= 1
                            pushfrente(frente,ciclo)
                        if(unos==2):
                            print('ciclo 2')
                            ciclo = 2
                            pushfrente(frente,ciclo)
                        if(unos==3):
                            print('ciclo 3')
                            ciclo = 3
                            pushfrente(frente,ciclo)
            if(operacion=='lechado_pernos'):
                match fort:
                    case 'p-m-sh':
                        print('pueden ser todos')
                        ciclo = 1
                        pushfrente(frente,ciclo)
                    case 'p-shf':
                        unos = 0
                        for i in lista:
                            if(i=='1'):
                                unos = unos + 1
                        if(unos==1):
                            print('ciclo 4')
                            ciclo = 4
                            pushfrente(frente,ciclo)
                            
                        if(unos==2):
                            print('ciclo 1,5')
                            ciclo = 1
                            pushfrente(frente,ciclo)
                            
                        if(unos==3):
                            print('ciclo 2,3,6')
                            ciclo = 2
                            pushfrente(frente,ciclo)
                            
                    case 'shf-p-m-sh':
                        print('pueden ser todos')
                        ciclo = 1
                        pushfrente(frente,ciclo)
                        
            if(operacion=='mapeo_geomecanico'):
                match fort:
                    case 'p-m-sh':
                        print('pueden ser todos')
                        ciclo = 1
                        pushfrente(frente,ciclo)
                        
                    case 'p-shf':
                        print('no hay')
                        ciclo = 0
                        pushfrente(frente,ciclo)
                    case 'shf-p-m-sh':
                        print('no hay')
                        ciclo = 0
                        pushfrente(frente,ciclo)
            if(operacion=='marcacion_topografica'):
                match fort:
                    case 'p-m-sh':
                        unos = 0
                        for i in lista:
                            if(i=='1'):
                                unos = unos + 1
                        if(unos==3):
                            print('ciclo 1,2,3')
                            ciclo = 1
                            pushfrente(frente,ciclo)
                        if(unos==4):
                            print('ciclo 5,6')
                            ciclo = 5
                            pushfrente(frente,ciclo)
                            
                        if(unos==5):
                            print('ciclo 4')
                            ciclo = 4
                            pushfrente(frente,ciclo)
                            
                        
                    case 'p-shf':
                        unos = 0
                        for i in lista:
                            if(i=='1'):
                                unos = unos + 1
                        if(unos==0):
                            print('ciclo 1,2,3')
                            ciclo = 1
                            pushfrente(frente,ciclo)
                        if(unos==1):
                            print('ciclo 5,6')
                            ciclo = 5
                            pushfrente(frente,ciclo)
                        if(unos==2):
                            print('ciclo 2,3,6')
                            ciclo = 2
                            pushfrente(frente,ciclo)
                    case 'shf-p-m-sh':
                        unos = 0
                        for i in lista:
                            if(i=='1'):
                                unos = unos + 1
                        if(unos==0):
                            print('ciclo 2,3')
                            ciclo = 2
                            pushfrente(frente,ciclo)
                        if(unos==1):
                            print('ciclo 1')
                            ciclo = 1
                            pushfrente(frente,ciclo)                        
            if(operacion=='hilteo_malla'):
                match fort:
                    case 'p-m-sh':
                        unos = 0
                        for i in lista:
                            if(i=='1'):
                                unos = unos + 1
                        if(unos==3):
                            print('ciclo 5,6,7')
                            ciclo = 5
                            pushfrente(frente,ciclo)
                        
                        if(unos==4):
                            print('ciclo 1,2')
                            ciclo = 1
                            pushfrente(frente,ciclo)
                        if(unos==5):
                            print('ciclo 4')
                            ciclo = 4
                            pushfrente(frente,ciclo)
                    case 'p-shf':
                        print('no hay')
                    case 'shf-p-m-sh':
                        print('no hay ')
            if(operacion=='proyeccion_shotchete'):
                match fort:
                    case 'p-m-sh':
                        unos = 0
                        for i in lista:
                            if(i=='1'):
                                unos = unos + 1
                        if(unos==4):
                            print('ciclo 4')
                            ciclo = 4
                            pushfrente(frente,ciclo)
                            
                        if(unos==5):
                            print('ciclo 1,5')
                            ciclo = 1
                            pushfrente(frente,ciclo)
                            
                        if(unos==6):
                            print('ciclo 2,3,6')
                            ciclo = 2
                            pushfrente(frente,ciclo)
                            
                    case 'p-shf':
                        print('no hay')
                    case 'shf-p-m-sh':
                        print('no hay ')
            if(operacion=='perforacion_avance'):
                match fort:
                    case 'p-m-sh':
                        unos = 0
                        for i in lista:
                            if(i=='1'):
                                unos = unos + 1
                        if(unos==4):
                            print('ciclo 3')
                            ciclo = 3
                            pushfrente(frente,ciclo)
                            
                        if(unos==5):
                            print('ciclo 6,2')
                            ciclo = 2
                            pushfrente(frente,ciclo)
                        if(unos==6):
                            print('ciclo 1,4,5')
                            ciclo = 1
                            pushfrente(frente,ciclo)
                    case 'p-shf':
                        unos = 0
                        for i in lista:
                            if(i=='1'):
                                unos = unos + 1
                        if(unos==1):
                            print('ciclo 3')
                            ciclo = 3
                            pushfrente(frente,ciclo)
                            
                        if(unos==2):
                            print('ciclo 2,6')
                            ciclo = 2
                            pushfrente(frente,ciclo)
                            
                        if(unos==3):
                            print('ciclo 1,4,5')
                            ciclo = 1
                            pushfrente(frente,ciclo)
                            
                        
                    case 'shf-p-m-sh':
                        unos = 0
                        for i in lista:
                            if(i=='1'):
                                unos = unos + 1
                        if(unos==1):
                            print('ciclo 3')
                            ciclo = 3
                            pushfrente(frente,ciclo)
                            
                        if(unos==2):
                            print('ciclo 1,2')
                            ciclo = 1
                            pushfrente(frente,ciclo)
                            
                      
            
        #DIVIDIR FRENTES POR NIVEL 
        cursor = bd14.cursor()
        sql = 'select * from frentes'
        cursor.execute(sql)
        data = cursor.fetchall()
        #memparaorden 
        nivelti = []
        nivelext = []
        nivelhd = []
        nivelpd = []
        nivelch = []
        niveliny = []
        tipopmsh = []
        tiposhfpmsh = []
        tipopshf = []
        #ordena id segun nivel 
        for i in data :
            cod = i['codigo_empresa']
            idfren = i['id_frente']
            e = list()
            e.append(idfren)
            ciclosyfrentes.append(e)
            nivel = i['nivel']
            tipofort =i['tipofort']
            if(cod==rut):
                match nivel:
                    case 'TI':
                        print(nivel,idfren)
                        nivelti.append(idfren)
                    case 'EXT':
                        print(nivel,idfren)
                        nivelext.append(idfren)
                    case 'HD':
                        print(nivel,idfren)
                        nivelhd.append(idfren)
                    case 'PD':
                        print(nivel,idfren)
                        nivelpd.append(idfren)
                    case 'CH':
                        print(nivel,idfren)
                        nivelch.append(idfren)
                    case 'INY':
                        print(nivel,idfren)
                        niveliny.append(idfren)
            if(cod==rut):
                match tipofort:
                    case 'p-m-sh':
                        tipopmsh.append(idfren)
                    case 'p-shf':
                        tipopshf.append(idfren)
                    case 'shf-p-m-sh':
                        tiposhfpmsh.append(idfren)


        #codigo ventana botones de nivel 
       
        def inhd():
            print('entro')
            winhd = Tk()
            winhd.title('FRENTES NIVEL HD')
            frame = Frame(winhd)
            frame.pack()
            marcadores = Frame(winhd)
            txtfrente = Label(frame,text='ID FRENTE:')
            txtfrente.grid(row='0',column='0')
            listfrente = ttk.Combobox(frame)
            listfrente.grid(row='0',column='1')
            listfrente['values']=nivelhd
            txtoperacion = Label(frame,text='Operacion:')
            txtoperacion.grid(row='1',column='0')
            listoperacion = ttk.Combobox(frame)
            listoperacion.grid(row='1',column='1')
            listoperacion['values'] = ciclominero1
            
            def chequear():
                frente = listfrente.get()
                operacion = listoperacion.get()
                addestadofrentes(frente,operacion)
                # 'pp','l','m','mt','h','sh','pa',
                if(operacion=='perforacion_pernos'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')

                if (operacion=='lechado_pernos'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                  
                if(operacion=='instalacion_malla'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                    
                if(operacion=='marcacion_topografica'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                    
                if(operacion=='hilteo_malla'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                   
                if(operacion=='proyeccion_shotcrete'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                    
                if(operacion=='perforacion_avance'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)

                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')

                else:
                    ciclo = '1'
                    
            verificar = Button(frame,text='Verificar',command=chequear)
            verificar.grid(row='2',column='0')
        def inpd():
            print('entro')
            winhd = Tk()
            winhd.title('FRENTES NIVEL HD')
            frame = Frame(winhd)
            frame.pack()
            marcadores = Frame(winhd)
            txtfrente = Label(frame,text='ID FRENTE:')
            txtfrente.grid(row='0',column='0')
            listfrente = ttk.Combobox(frame)
            listfrente.grid(row='0',column='1')
            listfrente['values']=nivelpd
            txtoperacion = Label(frame,text='Operacion:')
            txtoperacion.grid(row='1',column='0')
            listoperacion = ttk.Combobox(frame)
            listoperacion.grid(row='1',column='1')
            listoperacion['values'] = ciclominero1
            
            def chequear():
                frente = listfrente.get()
                operacion = listoperacion.get()
                addestadofrentes(frente,operacion)
                # 'pp','l','m','mt','h','sh','pa',
                if(operacion=='perforacion_pernos'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')

                if (operacion=='lechado_pernos'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                  
                if(operacion=='instalacion_malla'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                    
                if(operacion=='marcacion_topografica'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                    
                if(operacion=='hilteo_malla'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                   
                if(operacion=='proyeccion_shotcrete'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                    
                if(operacion=='perforacion_avance'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)

                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')

                else:
                    ciclo = '1'
                    
            verificar = Button(frame,text='Verificar',command=chequear)
            verificar.grid(row='2',column='0')
        def inch():
            print('entro')
            winhd = Tk()
            winhd.title('FRENTES NIVEL HD')
            frame = Frame(winhd)
            frame.pack()
            marcadores = Frame(winhd)
            txtfrente = Label(frame,text='ID FRENTE:')
            txtfrente.grid(row='0',column='0')
            listfrente = ttk.Combobox(frame)
            listfrente.grid(row='0',column='1')
            listfrente['values']=nivelch
            txtoperacion = Label(frame,text='Operacion:')
            txtoperacion.grid(row='1',column='0')
            listoperacion = ttk.Combobox(frame)
            listoperacion.grid(row='1',column='1')
            listoperacion['values'] = ciclominero1
            
            def chequear():
                frente = listfrente.get()
                operacion = listoperacion.get()
                addestadofrentes(frente,operacion)
                # 'pp','l','m','mt','h','sh','pa',
                if(operacion=='perforacion_pernos'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')

                if (operacion=='lechado_pernos'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                  
                if(operacion=='instalacion_malla'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                    
                if(operacion=='marcacion_topografica'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                    
                if(operacion=='hilteo_malla'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                   
                if(operacion=='proyeccion_shotcrete'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                    
                if(operacion=='perforacion_avance'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)

                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')

                else:
                    ciclo = '1'
                    
            verificar = Button(frame,text='Verificar',command=chequear)
            verificar.grid(row='2',column='0')
        def ininy():
            print('entro')
            winhd = Tk()
            winhd.title('FRENTES NIVEL HD')
            frame = Frame(winhd)
            frame.pack()
            marcadores = Frame(winhd)
            txtfrente = Label(frame,text='ID FRENTE:')
            txtfrente.grid(row='0',column='0')
            listfrente = ttk.Combobox(frame)
            listfrente.grid(row='0',column='1')
            listfrente['values']=niveliny
            txtoperacion = Label(frame,text='Operacion:')
            txtoperacion.grid(row='1',column='0')
            listoperacion = ttk.Combobox(frame)
            listoperacion.grid(row='1',column='1')
            listoperacion['values'] = ciclominero1
            
            def chequear():
                frente = listfrente.get()
                operacion = listoperacion.get()
                addestadofrentes(frente,operacion)
                # 'pp','l','m','mt','h','sh','pa',
                if(operacion=='perforacion_pernos'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')

                if (operacion=='lechado_pernos'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                  
                if(operacion=='instalacion_malla'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                    
                if(operacion=='marcacion_topografica'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                    
                if(operacion=='hilteo_malla'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                   
                if(operacion=='proyeccion_shotcrete'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                    
                if(operacion=='perforacion_avance'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)

                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')

                else:
                    ciclo = '1'
                    
            verificar = Button(frame,text='Verificar',command=chequear)
            verificar.grid(row='2',column='0')
        def inext():
            print('entro')
            winhd = Tk()
            winhd.title('FRENTES NIVEL HD')
            frame = Frame(winhd)
            frame.pack()
            marcadores = Frame(winhd)
            txtfrente = Label(frame,text='ID FRENTE:')
            txtfrente.grid(row='0',column='0')
            listfrente = ttk.Combobox(frame)
            listfrente.grid(row='0',column='1')
            listfrente['values']=nivelext
            txtoperacion = Label(frame,text='Operacion:')
            txtoperacion.grid(row='1',column='0')
            listoperacion = ttk.Combobox(frame)
            listoperacion.grid(row='1',column='1')
            listoperacion['values'] = ciclominero1
            
            def chequear():
                frente = listfrente.get()
                operacion = listoperacion.get()
                addestadofrentes(frente,operacion)
                # 'pp','l','m','mt','h','sh','pa',
                if(operacion=='perforacion_pernos'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')

                if (operacion=='lechado_pernos'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                  
                if(operacion=='instalacion_malla'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                    
                if(operacion=='marcacion_topografica'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                    
                if(operacion=='hilteo_malla'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                   
                if(operacion=='proyeccion_shotcrete'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                    
                if(operacion=='perforacion_avance'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)

                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')

                else:
                    ciclo = '1'
                    
            verificar = Button(frame,text='Verificar',command=chequear)
            verificar.grid(row='2',column='0')
        def inti():
            print('entro')
            winhd = Tk()
            winhd.title('FRENTES NIVEL HD')
            frame = Frame(winhd)
            frame.pack()
            marcadores = Frame(winhd)
            txtfrente = Label(frame,text='ID FRENTE:')
            txtfrente.grid(row='0',column='0')
            listfrente = ttk.Combobox(frame)
            listfrente.grid(row='0',column='1')
            listfrente['values']=nivelti
            txtoperacion = Label(frame,text='Operacion:')
            txtoperacion.grid(row='1',column='0')
            listoperacion = ttk.Combobox(frame)
            listoperacion.grid(row='1',column='1')
            listoperacion['values'] = ciclominero1
            
            def chequear():
                frente = listfrente.get()
                operacion = listoperacion.get()
                addestadofrentes(frente,operacion)
                # 'pp','l','m','mt','h','sh','pa',
                if(operacion=='perforacion_pernos'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')

                if (operacion=='lechado_pernos'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                  
                if(operacion=='instalacion_malla'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                    
                if(operacion=='marcacion_topografica'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                    
                if(operacion=='hilteo_malla'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                   
                if(operacion=='proyeccion_shotcrete'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)
                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')
                    
                if(operacion=='perforacion_avance'):
                    def getchek():
                        pp=pplist.get()
                        l=llist.get()
                        m=mlist.get()
                        mt=mtlist.get()
                        h=hlist.get()
                        psh=pshlist.get()
                        pa=palist.get()
                        quecicloes(frente,operacion,pp,l,m,mt,h,psh,pa)

                    print(frente,operacion)
                    marcadores.pack()
                    pp = Label(marcadores,text='Perforacion pernos')
                    pp.grid(row='1',column='0')
                    pplist = ttk.Combobox(marcadores)
                    pplist.grid(row='1',column='1')
                    pplist['values']=['si','no']
                    pplist.current(1)
                    l = Label(marcadores,text='Lechado pernos')
                    l.grid(row='2',column='0')
                    llist = ttk.Combobox(marcadores)
                    llist.grid(row='2',column='1')
                    llist['values']=['si','no']
                    llist.current(1)
                    m = Label(marcadores,text='Instalacion malla')
                    m.grid(row='3',column='0')
                    mlist = ttk.Combobox(marcadores)
                    mlist.grid(row='3',column='1')
                    mlist['values']=['si','no']
                    mlist.current(1)
                    mt = Label(marcadores,text='Marcacion topografica')
                    mt.grid(row='4',column='0')
                    mtlist = ttk.Combobox(marcadores)
                    mtlist.grid(row='4',column='1')
                    mtlist['values']=['si','no']
                    mtlist.current(1)
                    h = Label(marcadores,text='Hilteo malla')
                    h.grid(row='5',column='0')
                    hlist = ttk.Combobox(marcadores)
                    hlist.grid(row='5',column='1')
                    hlist['values']=['si','no']
                    hlist.current(1)
                    psh = Label(marcadores,text='Proyeccion shotcrete')
                    psh.grid(row='6',column='0')
                    pshlist = ttk.Combobox(marcadores)
                    pshlist.grid(row='6',column='1')
                    pshlist['values']=['si','no']
                    pshlist.current(1)
                    pa = Label(marcadores,text='Perforacion avance')
                    pa.grid(row='7',column='0')
                    palist = ttk.Combobox(marcadores)
                    palist.grid(row='7',column='1')
                    palist['values']=['si','no']
                    palist.current(1)
                    cualciclo = Button(marcadores,text='Ciclo',command=getchek)
                    cualciclo.grid(row='8',column='0')

                else:
                    ciclo = '1'
                    
            verificar = Button(frame,text='Verificar',command=chequear)
            verificar.grid(row='2',column='0')
        
            
        raiz = Tk()
        raiz.title('ORDEN SEGUN NIVEL')
        frame = Frame(raiz)
        frame.pack()
        text = Label(frame,text='ESCOJA EL NIVEL DEL FRENTE:')
        text.grid(row='0',column='0')
        bhd = Button(frame,text='HD',width='10',command=inhd)
        bhd.grid(row='1',column='1')
        bpd = Button(frame,text='PD',width='10',command=inpd)
        bpd.grid(row='1',column='2')
        bch = Button(frame,text='CH',width='10',command=inch)
        bch.grid(row='1',column='3')
        biny = Button(frame,text='INY',width='10',command=ininy)
        biny.grid(row='2',column='1')
        bext = Button(frame,text='EXT',width='10',command=inext)
        bext.grid(row='2',column='2')
        bti= Button(frame,text='TI',width='10',command=inti)
        bti.grid(row='2',column='3')
        




    
    verestadofrentes = Button(framemain,text='VER ESTADO FRENTES',command=verfrentes,width='28')
    verestadofrentes.grid(row='0',column="0")
    ingresarfrentes = Button(framemain,text='CAMBIAR ESTADO FRENTES',command=inputdata,width='28')
    ingresarfrentes.grid(row='1',column='0')
    algoritmoboton = Button(framemain,text='CORRER ALGORITMO',command=ventanaalgoritmos,width='28')
    algoritmoboton.grid(row='2',column='0')
    


#old 
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