# Realice un programa que lea 4 números y diga cuántos son pares y
# cuantos impares y devuelva la sumatoria de los pares.

cantidadpares = 0
cantidadimpares = 0
sumadepares = 0

for i in range(4):
    print("Ingresado número", i+1, "de 4:")
    numero = int(input("Número: "))

    if numero % 2 == 0:
        cantidadpares += 1
        sumadepares += numero
    else:
        cantidadimpares += 1

print("Cantidad de números pares:", int(cantidadpares))
print("Cantidad de números impares:", int(cantidadimpares))
print("Suma de los números pares:", sumadepares)
