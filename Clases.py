class objeto:
    """ Una clase en Python"""
    numero_1 = 5
    numero_2 = 4
    def suma(self,num1,num2):
        print(num1 + num2)

c = objeto()    
print(c.__doc__)
print(objeto.numero_1) 
print(objeto.numero_2)
c.suma(c.numero_1,c.numero_2)
