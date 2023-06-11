# Realice un programa que pida un número del 1 al 12 y diga el nombre
# del mes correspondiente

numero = int(input("Ingrese un número del 1 al 12 que representará un mes: "))

# Determinar el nombre del mes correspondiente
if numero == 1:
    nombre_mes = "Enero"
elif numero == 2:
    nombre_mes = "Febrero"
elif numero == 3:
    nombre_mes = "Marzo"
elif numero == 4:
    nombre_mes = "Abril"
elif numero == 5:
    nombre_mes = "Mayo"
elif numero == 6:
    nombre_mes = "Junio"
elif numero == 7:
    nombre_mes = "Julio"
elif numero == 8:
    nombre_mes = "Agosto"
elif numero == 9:
    nombre_mes = "Septiembre"
elif numero == 10:
    nombre_mes = "Octubre"
elif numero == 11:
    nombre_mes = "Noviembre"
elif numero == 12:
    nombre_mes = "Diciembre"
else:
    nombre_mes = "Número no válido"

# Mostrar el mes
print("El número", numero, "corresponde al mes de:", nombre_mes)
