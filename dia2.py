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
noun=0
verb=-1
while(matrix[0]!=19690720):
	matrix=leerarchivo()
	verb+=1
	if(verb==99):
		noun+=1
		verb=0
	matrix[1]=noun
	matrix[2]=verb
	for i in range(0,len(matrix)-1,4):
		if(matrix[i]==1 and i+3<len(matrix)-1):
			matrix[matrix[i+3]]=matrix[matrix[i+1]]+matrix[matrix[i+2]]
			continue
		if(matrix[i]==2 and i+3<len(matrix)-1):
			matrix[matrix[i+3]]=matrix[matrix[i+1]]*matrix[matrix[i+2]]
			continue
		if(matrix[i]==99):
			break
print(100*23+47)