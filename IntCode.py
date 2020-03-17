
global matrix
global opcodeDic


def suma(param1,param2,res):
	matrix[res]=param1+param2

def producto(param1,param2,res):
	matrix[res]=param1*param2

def leer(param1,param2,res):
	matrix[param1]=input()

def escribir(param1,param2,res):
	print matrix[param1]

def leerarchivo():
	f = open ('input2.txt','r')
	mensaje = f.read()
	matrix = []
	num=""
	for i in mensaje:
		if(i!=','):
			num+=i
		else:
			matrix.append(int(num))
			num=""
	matrix.append(0)
	f.close()
	return(matrix)

matrix=leerarchivo()
opcodeDic={1:suma, 2:producto, 3:leer, 4:escribir}
i=0
while(True):
	opcode=matrix[i]%10
	if opcode<3:
		if matrix[i]/1000%10==0:
			param2=matrix[matrix[i+2]]
		else:
			param2=matrix[i+2]
		if matrix[i]/100%10==0:
			param1=matrix[matrix[i+1]]
		else:
			param1=matrix[i+1]
		res=matrix[i+3]
		i+=4
	elif opcode==3 or opcode==4:
		param1=matrix[i+1]
		param2=0
		res=0
		i+=2
	elif opcode==99:
		break
	opcodeDic.pop(opcode)(param1,param2,res)




	
