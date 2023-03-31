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

if total>=500 and total<100:
    descuento=((total*0.05)+total)
    print(f"El total de las compras es: {descuento} con el 5% de descuento aplicado")

elif total>=1000:
    descuento=((total*0.1)+total)
    print(f"El total de las compras es: {descuento} con el 10% de descuento aplicado")

else:print(f"El total de las compras es: {total} sin descuento")

# Imprimir el total de las compras del cliente


print('                                           FIN                                                              ')
print('**********************************************************************************************************\n')
