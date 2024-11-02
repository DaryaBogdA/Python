dct = {
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4
}
summa = 0
for key in dct:
    dct[key] = dct[key]**2
    print(dct[key])
    summa += dct[key]
print(summa)