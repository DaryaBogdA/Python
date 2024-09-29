
x = input("Введите слово: ")
w = x[-1]

if (w == "ь"):
    print(x[-2])
else:
    print(w)
