print('**********************************************************************************************************\n')
print('                                          tiendita\n                                                        ')
print('**********************************************************************************************************\n')

# Definir una lista vacía para almacenar los montos de las compras
compras = []

# Ingresar los montos de las compras del cliente
while True:
    compra = input("Ingrese el monto de la compra (o 'fin' para terminar): ")
    if compra == "fin":
        break
    try:
        compra = float(compra)
        compras.append(compra)
    except ValueError:
        print("Error: el valor ingresado no es un número válido.")

# Calcular el total de las compras del cliente
total = sum(compras)

# Imprimir el total de las compras del cliente
print("El total de las compras del cliente es:", total)

print('                                           FIN                                                              ')
print('**********************************************************************************************************\n')