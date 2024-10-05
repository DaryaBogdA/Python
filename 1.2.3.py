
x = int(input("Введите число: "))
last = x % 10
while x >= 10:
    x //= 10
first = x

sum = first + last
print("Сумма первой и последней цифры:", sum)