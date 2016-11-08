lista1 = [1, 2, 'a', False]

print('foreach')
# standradowo for dziala jak foreach!
for x in lista1:
    print('Element: ', x)

print()
print('enumerate')
# jesli potrzebujemy indeksow - uzyjmy enumerate
for indeks, wartosc in enumerate(lista1):
    print('indeks: ', indeks, ' wartosc: ', wartosc)
