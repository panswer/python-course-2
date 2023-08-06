'''
Ejercicio 3
Obtener el radio y longitud de un circulo
'''

import math

area_str = input("Area de circulo: ")

if area_str.isdecimal():
    area_num = float(area_str)

    r = math.sqrt(area_num / math.pi)
    l = 2 * math.pi * r

    print(f"Radio: {r:.1f}, Longitud: {l:.1f}")
else:
    print("Area no valida")