#listas

autos = ['Ford','Chevrolet','Fiat']

print(autos)
print(autos[2])

autos.append('Ferrari')
autos.insert(2,'BYD')

print(autos)

del autos[0]

print(autos)

#tuplas

lenguajes = ('php','c++','c')
print(lenguajes)

#diccionarios

user = {'id':1,'name':'Ismael','Male':True}
user['id'] *= 4
print(user['name'])
print(user.values())
