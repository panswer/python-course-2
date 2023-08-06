'''
Ejercicio 4
Obtener el precio final que se tiene que pagar si se aplica el 36% de descuento
'''

precio_str = input("Precio: ")

if precio_str.isdecimal():
    precion_num = float(precio_str)

    percentage = 36

    descount = (precion_num * percentage) / 100

    total = precion_num - descount

    print(f"Total: {total:.2f}")
else:
    print("Precio invalido")