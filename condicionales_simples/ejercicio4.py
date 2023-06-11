# Realiza un programa que lea dos números y diga cuál es el mayor

# float para evitar decimales
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Comparar los números y determinar el mayor
if numero1 > numero2:
    print("El primer número es mayor.")
elif numero2 > numero1:
    print("El segundo número es mayor.")
else:
    print("Los números son iguales.")
