
x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))

while x >= 10:
    x //= 10

first_x = x

while y >= 10:
    y //= 10

first_y = y
if first_y == first_x:
 print("Цифры равны")
else:
   print("Цифры не равны")