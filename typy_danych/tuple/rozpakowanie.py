k1 = (1, 2, 'a')

print('rozpakowanie:')
x, y, napis = k1

print(x)
print(y)
print(napis)

# Ilosc zmiennych po lewej stronie musi rownac sie ilosci elementow w krotce.
# a, b = k1

print('pakowanie:')
k2 = 'a', 'b', 'c'
print(k2)

# no i zamiana!
print('zamiana: ')
a = 1
b = 2
print('a: ', a, 'b: ', b)
a, b = b, a
print('a: ', a, 'b: ', b)
