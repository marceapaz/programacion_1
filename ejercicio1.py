#Introducir los lados de un triángulo y visualizar por pantalla si dicho
# triángulo es equilátero, isósceles o escaleno.

#Clasificación de triángulos según lados:
#Triángulo equilátero: tiene sus tres lados iguales, todos miden lo mismo.
#El triángulo isósceles: tiene dos lados iguales y uno distinto.
#El escaleno: tiene los tres lados diferentes, es decir, de distinta longitud.

lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

if lado1 == lado2 == lado3:
    print("El triángulo es equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")
