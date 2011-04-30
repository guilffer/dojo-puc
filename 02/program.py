import math

def caixaEletronico(valor):
    notas = [2, 5, 10, 20, 50, 100]
    moedas = [0.01, 0.05, 0.10, 0.25, 0.50, 1]
    moedas.reverse()
    dic = {"notas": {}, "moedas": {}}
    
    valor = math.modf(valor)    
    valor = [round(valor[0], 2), valor[1]]
    
    valor = valor[::-1]
    
    if valor[0] == 1:
        dic["moedas"][int(valor[0])] = 1
    
    
    
    if valor[0] in notas:
        dic["notas"][int(valor[0])] = 1

    while valor[1] > 0:
        for i in moedas:
            if(i <= valor[1]):
                valor[1] = valor[1] - i 
                 
                dic["moedas"][i] = dic["moedas"].get(i,0) + 1
            
        
            
    return dic
