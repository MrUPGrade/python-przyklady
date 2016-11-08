ciag_znakow = 'to jest ciag znakow'
print(ciag_znakow)

print('str jest sewkencja:')
for znak in ciag_znakow:
    print('znak: ', znak)


print('enumerate tez dziala:')
for indeks, znak in enumerate(ciag_znakow):
    print('indeks: ', indeks, 'znak: ', znak)