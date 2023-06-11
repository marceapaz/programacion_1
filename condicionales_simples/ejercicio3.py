# Realizar un programa que permita ingresar "f" o "m" y determinar si vota en mesa femenina o mesa masculina
genero = input("Ingrese su género: ")

# lower: pasa a minúscula lo que se ingresa como parámetro:
if genero.lower() == "f":
    print("Vota en mesa femenina.")
elif genero.lower() == "m":
    print("Vota en mesa masculina.")
else:
    print("Género no válido. Ingrese 'f' (femenino) o 'm' (masculino)")
