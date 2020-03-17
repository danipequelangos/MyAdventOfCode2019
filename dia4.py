cont=0
for i in range(367479,893699):
	contar=False
	hayPar=False
	digitos=[i/100000,(i/10000)%10,(i/1000)%10,(i/100)%10,(i/10)%10,i%10]
	oldDigit=-1
	for j in range(0,5):
		if digitos[j]==digitos[j+1]:
			if j!=4 and digitos[j]!=digitos[j+2] and oldDigit!=digitos[j]:
				oldDigit=-1
				contar=True
				break
			if j!=4 and digitos[j]==digitos[j+2]:
				oldDigit=digitos[j+2]
			if j==4 and oldDigit!=digitos[j]:
				oldDigit=-1
				contar=True
				break
	for j in range(1,6):
		if digitos[j]<digitos[j-1]:
			contar=False
	if contar:
		print i
		cont+=1
print cont
