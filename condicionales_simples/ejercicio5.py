# Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo el cambio de dólares a pesos y que sea el usuario 
# quien decida qué tipo de cambio quiere, si de dólares a pesos o viceversa.

# DÓLAR OFICIAL $258
tipodeconversion = input("Ingrese la opción de conversión (1 de dólares a pesos, 2 de pesos a dólares): ")
cotizaciondolar = 258

# Verificar la opción
if tipodeconversion == "1":
    dolares = float(input("Ingrese la cantidad en dólares: "))
    pesos = dolares * cotizaciondolar  
    print(dolares, " dólares equivalen a ", pesos, " pesos")   
elif tipodeconversion == "2":
    pesos = float(input("Ingrese la cantidad en pesos: "))
    dolares = pesos / cotizaciondolar   
    print(pesos, " pesos equivalen a ", dolares, "dólares")
else:
    print("Opción incorrecta. Ingrese 1 o 2.")



