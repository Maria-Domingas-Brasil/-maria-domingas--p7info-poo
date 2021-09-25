print("Escreva um número:")
a = int(input())

	
def primo (p):
    contador = 0
    for i in range (1, p+1):
        if p%i==0:
	        contador = contador+1
    if contador == 2:
        return True
    else:
        return False
		   
def somaPrimos (a):	
    soma = 0
    num = 0
    cont = 0 
    while cont < a:	 
        if primo(num):
            cont = cont + 1
            soma = soma + num
        num = num + 1    	
    return soma
    
print("Soma:", somaPrimos(a))
