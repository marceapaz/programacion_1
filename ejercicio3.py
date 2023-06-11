# Realice un programa que lea tres números, muestre cuál es el mayor y
# determine si es par o impar.

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Determinar el número mayor
mayor = max(numero1, numero2, numero3)

# Mostrar el número mayor
print("El número mayor es:", mayor)

# Determinar si el número mayor es par o impar
if mayor % 2 == 0:
    print("El número mayor es par.")
else:
    print("El número mayor es impar.")
