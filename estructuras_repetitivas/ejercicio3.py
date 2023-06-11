# Ingresar las edades y el sexo de 15 personas y determinar cuántas son
# mujeres, cuántos varones, cuántos mayores de edad y cuántos
# menores de edad.
# Inicializar variables

cantMujeres = 0
cantVarones = 0
cantMayoresEdad = 0
cantMenoresEdad = 0

print("Bienvenido. Deberá ingresar los datos de 15 personas...")
for i in range(15):
    print("Ingresado datos de la persona:", i+1)
    edad = int(input("Ingrese la edad: "))
    sexo = input("Ingrese el sexo (M/F): ")

    # Validar sexo de la persona
    if sexo.upper() == "M":
        cantVarones += 1
    elif sexo.upper() == "F":
        cantMujeres += 1

    # Validar si la persona es mayor o menor de edad
    if edad >= 18:
        cantMayoresEdad += 1
    else:
        cantMenoresEdad += 1

# Resultados
print("Cantidad de mujeres:", int(cantMujeres))
print("Cantidad de varones:", int(cantVarones))
print("Cantidad de personas mayores de edad:", int(cantMayoresEdad))
print("Cantidad de personas menores de edad:", int(cantMenoresEdad))
