# Leer 10 números y obtener la cantidad de mayores y la cantidad de
# menores a 100, cuál es el número máximo y cuál es el número mínimo.

cantMayoresA100 = 0
cantMenoresA100 = 0
maximo = float(0)
minimo = float(0)
contador = 0
# Leer 10 números
while contador < 10:
    print("Ingresado número", contador, "de 10:")
    numero = int(input("Número: "))
    
    if numero > 0:
        if numero > 100:
            cantMayoresA100 += 1
        elif numero < 100:
            cantMenoresA100 += 1
            
        # Calcular máximo y mínimo
        maximo = max(maximo, numero)
        minimo = min(minimo, numero)

        contador += 1
    else:
        print("Debe ingresar números mayores a 0")

# Resultados
print("Cantidad de números mayores a 100:", int(cantMayoresA100))
print("Cantidad de números menores a 100:", int(cantMenoresA100))
print("Número máximo:", int(maximo))
print("Número mínimo:", int(minimo))
