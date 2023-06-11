#  Leer 15 números negativos y convertirlos a positivos e imprimir dichos
# números.

# Leer 15 números negativos y convertirlos a positivos
print("Ingrese 15 números negativos:")
for i in range(15):
    print("Ingresado número:", i+1)
    numero = float(input("Número negativo: "))

    # Si el nro es menor que 0, es negativo
    if numero < 0:
        #abs función para convertir de negativo a positivo
        numero = abs(numero)

    # Imprimir
    print("Nro. convertido a positivo:", int(numero))
