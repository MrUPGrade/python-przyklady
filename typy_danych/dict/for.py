slownik = {
    'imie': 'Jakub',
    'nazwisko': 'Czaplinski',
    'wiek': 31
}
print('slownik: ', slownik)
print('# domyslnie po kluczach')
for x in slownik:
    print(x)

print('# po wartosciach')
for x in slownik.values():
    print(x)

print('# po parach klucz wartosc')
for klucz, wartosc in slownik.items():
    print('klucz: ', klucz, 'wartosc', wartosc)
