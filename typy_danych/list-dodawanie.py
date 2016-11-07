a = [0, 1, 2]
print(a)

a.append(3)
print(a)

a = a + [4, 5]
print(a)

a = a + ['6', 'cos innego', {'wiek': 31}]
print(a)

ilosc_elementow = len(a)
print('Ilosc elementow: ', ilosc_elementow)

# Nie da sie tak dodawac do listy
# a[ilosc_elementow] = 'ostatni'
