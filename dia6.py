#Primera parte
class arbolDeHijos:
	def __init__(self,elemento):
		self.__elemento = elemento
		self.__hijos = []
	
	def getElemento(self):
		return self.__elemento
	
	def getHijos(self):
		return self.__hijos

	def agregarHijo(self,hijo):
		self.__hijos.append(hijo)

def leerArchivo():
	f = open ('input6.txt','r')
	mensaje = f.read()
	lista = mensaje.split('\n')
	return lista

lista = leerArchivo()
orbitas = []
planetas = []
for i in lista:
	orbit = i.split(')')
	if (orbit[0] in planetas) == False:
		planetas.append(orbit[0])
		orbitas.append(arbolDeHijos(orbit[0]))
	if (orbit[1] in planetas) == False:
		planetas.append(orbit[1])
		orbitas.append(arbolDeHijos(orbit[1]))
	indice0 = planetas.index(orbit[0])
	indice1 = planetas.index(orbit[1])
	orbitas[indice0].agregarHijo(orbitas[indice1])

def recursiva(cont,i,iterador):
	iterador+=1
	cont += iterador
	for j in i.getHijos():
		cont = recursiva(cont,j,iterador)
	return cont



COM = planetas.index("COM")
i=orbitas[COM]
cont=recursiva(0,i,-1)
print cont


#Segunda parte
from collections import defaultdict
class arbolDePadres:
	def __init__(self,elemento):
		self.__elemento = elemento
		self.__padre = None
	def getElemento(self):
		return self.__elemento
	
	def getPadre(self):
		return self.__padre

	def setPadre(self,padre):
		self.__padre=padre

lista = leerArchivo()
orbitas = []
planetas = []

for i in lista:
	orbit = i.split(')')
	if (orbit[0] in planetas) == False:
		planetas.append(orbit[0])
		orbitas.append(arbolDePadres(orbit[0]))
	if (orbit[1] in planetas) == False:
		planetas.append(orbit[1])
		orbitas.append(arbolDePadres(orbit[1]))
	indice0 = planetas.index(orbit[0])
	indice1 = planetas.index(orbit[1])
	orbitas[indice1].setPadre(orbitas[indice0])

def listaPadres(hijos):
	padres=defaultdict(list)
	distancias=[[],[]]
	for n in range(0,2):
		cont=-1
		i=orbitas[hijos[n]]
		while(True):
			padres[n].append(i.getElemento())
			distancias[n].append(cont)
			cont+=1
			if i.getPadre()==None:
				break;
			else:
				i=i.getPadre()
	return padres,distancias


YOU = planetas.index("YOU")
SAN = planetas.index("SAN")
padres,distancias=listaPadres([YOU,SAN])
comunes0 = [padres[0].index(i) for i in list(set(padres[0]) & set(padres[1]))]
comunes1 = [padres[1].index(i) for i in list(set(padres[0]) & set(padres[1]))]
distComunes=[]
for i in range(0,len(comunes0)):
	distComunes.append(distancias[0][comunes0[i]]+distancias[1][comunes1[i]])
print min(distComunes)