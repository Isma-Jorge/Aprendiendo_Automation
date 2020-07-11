
precio = 0

#Funciones para calcular precio según marca, puerta y color 
def calc_marca(marca):
    global precio
    if marca == "Ford":
        precio += 100000
    elif marca == "Chevrolet":
        precio += 120000 
    elif marca == "Fiat":
        precio += 80000
        
def calc_puertas(puertas):
    global precio
    if puertas == "2":
        precio += 50000
    elif puertas == "4":
        precio += 65000
    elif puertas == "5":
        precio += 78000
    
def calc_color(color):
    global precio
    if color == "blanco":
        precio += 10000
    elif color == "azul":
        precio += 20000
    elif color == "negro":
        precio += 30000

nro_clientes = 1
marcas = ['ford','chevrolet','fiat']
puertas = [2,4,5]
colores = ['blanco','azul','negro']
ventas = []
#Bucle principal
while True:    
    precio = 0
    print("Buenos días. Se le pide su nombre y apellido.")
    Nombre = input("Nombre: ")
    Apellido = input("Apellido: ")
    print("Ahora cuentenos las características del auto deseado.")
    marca = ''
    puerta = 0
    color = ''
    #Validación de los inputs
    while marca not in marcas: 
        marca = input("Marca: ")
        marca = marca.lower()
    while puerta not in puertas:
        puerta = int(input("N° de puertas: "))
    while color not in colores:
        color = input("Color: ")
        color = color.lower()
    #Llamadas a funciones de calcular los precios
    calc_marca(marca)
    calc_puertas(puerta)
    calc_color(color)
    #Cálculo de Descuentos
    if nro_clientes > 5 and nro_clientes < 11:
        precio *= 0.10
    elif nro_clientes > 10 and nro_clientes < 51:
        precio *= 0.15
    elif nro_clientes > 50:
        precio *= 0.18
    ventas.append({'nombre':Nombre,'apellido':Apellido,'marca':marca,'puerta':puerta,'color':color,'precio':precio})    
    #Pregunta final
    opt = input("¿Nueva compra de cliente?: ")
    opt = opt.lower()
    while opt != "no" and opt != "si":
        opt = input("¿Nueva compra de cliente? si/no: ")
    if opt == "no":
        break
    nro_clientes += 1
    print("Clientes: "+str(nro_clientes)) #DLC para ver nro_clientes (:
    
#Print final
for venta in ventas:
    print("El cliente "+venta['nombre']+" "+venta['apellido']+" "+"compró el siguiente auto: ")
    print("Marca: " + venta['marca'])
    print("Puertas: " + str(venta['puerta']))
    print("Color: " + venta['color'])
    print("-------")
    print("Precio: " + str(venta['precio']))
    print("-------")

# PD: Ya ví el video de resolución y me di cuenta de todas las lineas que gaste en esas 3 funciones (:
#Saludos y gracias!