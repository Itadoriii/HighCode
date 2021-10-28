#clase frente 


class Frente:
    def __init__(self,nombre,sigla,numero,direccion,estado,tamaño,ruta,distancia,id,nivel,mb):
        self.nombre = nombre
        self.sigla = sigla
        self.numero= numero
        self.direccion = direccion
        self.estado = estado
        self.tamaño = tamaño
        self.ruta = ruta
        self.distancia = distancia
        self.id = id
        self.nivel =  nivel
        self.mb =  mb

    def getnombre (self): 
        return self.nombre
    def setnombre(self,nombre):
        self.nombre=nombre

    def getsigla (self):
        return self.sigla
    def setsigla(self,sigla):
        self.sigla=sigla
        
    def getnumero (self):
        return self.numero
    def setnumero(self,numero):
        self.numero=numero

    def getdireccion (self):
        return self.direccion
    def setdireccion (self,direccion):
        self.direccion=direccion
    
    def getestado (self):
        return self.estado
    def setestado(self,estado):
        self.estado=estado

    def gettamaño (self):
        return self.tamaño
    def settamaño(self,tamaño):
        self.tamaño=tamaño

    def getruta (self):
        return self.ruta
    def setruta(self,ruta):
        self.ruta=ruta

    def getdistancia (self):
        return self.distancia
    def setdistancia(self,distancia):
        self.distancia=distancia

    def getid (self):
        return self.id
    def setid(self,id):
        self.id=id
    
    def getnivel (self):
        return self.nivel
    def setnivel(self,nivel):
        self.nivel=nivel

    def getmb (self):
        return self.mb
    def setmb(self,mb):
        self.mb=mb
    





    
        



    

