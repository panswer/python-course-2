'''
Ejercicio 4
Crear un programa que pida 2 numeros y obtenga como resultado cual es ellos es par o si ambos lo son
'''

num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Numero 1 y 2 son par")
elif num1 % 2 == 0:
    print("Numero 1 es par")
elif num2 % 2 == 0:
    print("Numero 2 es par")
else:
    print("Ninguno de los 2 numeros es par")