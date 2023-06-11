# Confeccione un programa que pida un número del 1 al 7 y diga el día de
# la semana correspondiente.

numero = int(input("Ingrese un número del 1 al 7 que representará un día de la semana: "))

# Días de la semana 
if numero == 1:
    dia_semana = "Lunes"
elif numero == 2:
    dia_semana = "Martes"
elif numero == 3:
    dia_semana = "Miércoles"
elif numero == 4:
    dia_semana = "Jueves"
elif numero == 5:
    dia_semana = "Viernes"
elif numero == 6:
    dia_semana = "Sábado"
elif numero == 7:
    dia_semana = "Domingo"
else:
    dia_semana = "Número no válido"

# Mostrar el día de la semana
print("El número", numero, "corresponde al día de la semana: ", dia_semana)