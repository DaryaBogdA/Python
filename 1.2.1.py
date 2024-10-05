
x = int(input("Введите число: "))
if x == 0:
  first = 0
else:
  while x >= 10:
    x //= 10
  first = x
print("Первая цифра:", first)