dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

def roman2Arabic(romano):
	valor = 0
	acumulado = 0
	
	for i in romano:
		
		if( dic[i] > acumulado and acumulado != 0):
			valor += dic[i]-(acumulado*2)
		else:
			valor += dic[i]
			acumulado = dic[i]	
		
	return valor
	