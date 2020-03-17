from collections import defaultdict
def leerarchivo():
	f = open ('input3.txt','r')
	texto = f.read()
	wire1 = []
	wire2 = []
	num=""
	w2 = False
	for i in texto:
		if(i=='\n'):
			wire1.append(num)
			num=''
			w2=True
			continue
		if(i!=','):
			num+=i
			continue
		else:
			if(w2==False):
				wire1.append(num)
			else:
				wire2.append(num)
			num=""
	f.close()
	return(wire1,wire2)

def recorrido(W1,W2):
	movimientos=[W1,W2]
	puntos = defaultdict(list)
	x=0
	y=0
	for m in range(0,2):
		x=0
		y=0
		for i in range(0,len(movimientos[m])):
			movs=movimientos[m]
			if(movs[i][0]=="L"):
				for j in range(1,int(movs[i][1:len(movs[i])])+1):
					x+=1
					puntos[m].append((x,y))
			if(movs[i][0]=="R"):
				for j in range(1,int(movs[i][1:len(movs[i])])+1):
					x-=1
					puntos[m].append((x,y))
			if(movs[i][0]=="U"):
				for j in range(1,int(movs[i][1:len(movs[i])])+1):
					y+=1
					puntos[m].append((x,y))
			if(movs[i][0]=="D"):
				for j in range(1,int(movs[i][1:len(movs[i])])+1):
					y-=1
					puntos[m].append((x,y))
	return(puntos)


W1,W2=leerarchivo()
puntos=recorrido(W1,W2)
res = set(puntos[0]) & set(puntos[1])
print min(abs(punto[0]) + abs(punto[1]) for punto in res)
print [puntos[0].index(punto) + puntos[1].index(punto) + 2 for punto in res]
