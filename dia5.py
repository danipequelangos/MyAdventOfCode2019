
def suma(param1,param2,res):
	matrix[res]=param1+param2

def producto(param1,param2,res):
	matrix[res]=param1*param2

def leer(param1):
	matrix[param1]=int(input())

def escribir(param1):
	print param1

def saltoV(param1,param2,i):
	if param1!=0:
		return param2
	else:
		return i+3

def saltoF(param1,param2,i):
	if param1==0:
		return param2
	else:
		return i+3

def menor(param1,param2,res):
	if param1<param2:
		matrix[res]=1
	else:
		matrix[res]=0

def igual(param1,param2,res):
	if param1==param2:
		matrix[res]=1
	else:
		matrix[res]=0

def leerarchivo():
	f = open ('input5.txt','r')
	mensaje = f.read()
	matrix = mensaje.split(',')
	for i in range(0,len(matrix)):
		matrix[i]=int(matrix[i])
	f.close()
	return(matrix)

#################################################

matrix=leerarchivo()
opcodeDic={ 1:suma, 2:producto, 3:leer, 4:escribir, 5:saltoV, 6:saltoF, 7:menor, 8:igual}
i=0
while(True):
	opcode=matrix[i]%100
	if opcode==3 or opcode==4:
		if matrix[i]/100%10==0 and opcode!=3:
			param1=matrix[matrix[i+1]]
		else:
			param1=matrix[i+1]
		opcodeDic.get(opcode)(param1)#para el 3 y 4
		i+=2
		continue
	elif opcode==99:
		break
	else:
		if matrix[i]/1000%10==0:
			param2=matrix[matrix[i+2]]
		if matrix[i]/1000%10==1:
			param2=matrix[i+2]
		if matrix[i]/100%10==0:
			param1=matrix[matrix[i+1]]
		if matrix[i]/100%10==1:
			param1=matrix[i+1]
		if opcode==5 or opcode==6:
			i=opcodeDic.get(opcode)(param1,param2,i)#para el 5 y 6
		else:
			res=matrix[i+3]
			opcodeDic.get(opcode)(param1,param2,res)#para el 1, 2, 7 y 8
			i+=4
			continue



	
