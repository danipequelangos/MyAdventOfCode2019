import math
import itertools
#################PARTE1####################
def suma(param1,param2,res):
	matrix[res]=param1+param2

def producto(param1,param2,res):
	matrix[res]=param1*param2

def leer(param1,sigInput,j):
	if j == -1:
		matrix[param1]=sigInput
	else:
		matrix[param1]=j
	return sigInput

def escribir(param1,sigInput,j):
	sigInput = param1
	return sigInput

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
	f = open ('input7.txt','r')
	mensaje = f.read()
	matrix = mensaje.split(',')
	for i in range(0,len(matrix)):
		matrix[i]=int(matrix[i])
	f.close()
	return(matrix)

#################################################
def amplificador(setSeq,sigInput):
	for j in setSeq:
		i=0
		while(True):
			opcode=matrix[i]%100
			if opcode==3 or opcode==4:
				if matrix[i]/100%10==0 and opcode!=3:
					param1=matrix[matrix[i+1]]
				else:
					param1=matrix[i+1]
				sigInput=opcodeDic.get(opcode)(param1,sigInput,j)#para el 3 y 4
				j=-1
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
	return sigInput

matrix=leerarchivo()
opcodeDic={ 1:suma, 2:producto, 3:leer, 4:escribir, 5:saltoV, 6:saltoF, 7:menor, 8:igual}
outputs=[]
setSeq1=[0,1,2,3,4]
for i in range(5):
	setSeq2=setSeq1[:i]+setSeq1[i+1:]
	for j in range(4):
		setSeq3=setSeq2[:j]+setSeq2[j+1:]
		for y in range(3):
			setSeq4=setSeq3[:y]+setSeq3[y+1:]
			for x in range(2):
				setSeq5=setSeq4[:x]+setSeq4[x+1:]
				outputs.append(amplificador([setSeq1[i],setSeq2[j],setSeq3[y],setSeq4[x],setSeq5[0]],0))

print max(outputs)
##############PARTE2################