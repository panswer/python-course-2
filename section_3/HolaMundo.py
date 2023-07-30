# Operadores logicos

a = 30
b = 40
c = 50

# r = (a < b) and (b < c)
# r = (a > b) and (b < c)
# r = (a > b) or (b < c)
r = not((a > b) or (b < c))
print(r)