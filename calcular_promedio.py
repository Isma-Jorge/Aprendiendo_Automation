def calcular_promedio(matematicas, literatura, física):
    notas = matematicas + literatura + física
    prom = notas / 3
    print("Su promedio: " + str(prom))
    if prom >= 6:
        print("Usted Aprobó")
        if prom >= 9:
            print("Alumno destacado")
    elif prom <= 4:
        print("Insuficiente")
    elif prom > 4 and prom <= 5.99999:
        print("A recuperatorio")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
mat = int(input("Ahora ingrese su nota en matemáticas: "))
lit = int(input("Ingrese su nota en literatura: "))
fis = int(input("Ingrese su nota en Física: "))
print(nombre + " " + apellido)
calcular_promedio(mat,lit,fis)