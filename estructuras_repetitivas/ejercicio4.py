# Leer 10 números y mostrar solamente los números positivos, y su
# sumatoria

sumaDePositivos = 0

print("Ingrese 10 números:")   
for i in range(10):
    print("Ingresado número:", i+1)
    numero = float(input("Número: "))

    # Sumo si el nro. es mayor a cero
    if numero > 0:
        sumaDePositivos += numero

# Resultados
print("Sumatoria de números positivos:", sumaDePositivos)
