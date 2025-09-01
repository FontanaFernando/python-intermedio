a = {1,2,3,4,5}
b = {4,5,6,7,8}

# Union
print(a)
print(b)
print(a | b)

# Interseccion
print(a & b)

# Diferencia y Diferencia Simetrica
print(a - b)
print(b - a)
print(a.symmetric_difference(b))

# Subconjunto
a = {1,2,3,4,5}
b = {4,5}
print(b.issubset(a))

# Numero de elementos
print(len(a))
print(len(b))