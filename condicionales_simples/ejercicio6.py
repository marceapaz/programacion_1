# Realice un programa donde el usuario ingrese su edad. Si es mayor de 16 años, 
# muestre un mensaje diciendo “puede votar”, sino “no vota”.

edad = int(input("Ingrese una edad: "))

if edad > 16:
    print("Puede votar...")
else:
    print("No puede votar...")
