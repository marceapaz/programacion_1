# Realice un programa que le permita al usuario simular el pago
# ingresando el importe y la forma de pago:
# • Contado (1): se aplica un descuento del 10% al importe
# • Tarjeta (2): se aplica un interés de 10%
# • Débito (3): se aplica un descuento del 5%

importe = float(input("Ingrese el importe: "))
importetotal = float(0)
formadepago = int(input("Ingrese la forma de pago (1: Contado, 2: Tarjeta, 3: Débito): "))

# Calcular el importe
if formadepago == 1: #Contado
    importetotal = importe - ((importe * 10) / 100)  
elif formadepago == 2: #Tarjeta
    importetotal = importe + ((importe * 10) / 100)
elif formadepago == 3: #Débito
    importetotal = importe - ((importe * 5) / 100) 
else:
    print("Forma de pago incorrecta.")

# Mostrar el importe total:
print("Importe final:", importetotal)
