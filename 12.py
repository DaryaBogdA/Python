import datetime

def exercise5_1_1():
    today = datetime.date.today()
    print(today.year, "-", today.month, "-", today.day)


def exercise5_1_3(l):
  print(l * 5)


     

# exercise5_1_1()
# exercise5_1_3("x")


# x = int(input("Enter first number "))
# y = int(input("Enter second number "))
def exercise5_3_1(num1, num2):
  for i in range(num1, num2 + 1):
     print(i) 



# year = int(input("Enter year "))
def exercise5_3_3(year):
    if year % 4 == 0:
        print("Год високосный")
    else:
        print("Год не високосный")

def exercise5_5_3(arr):
    for i in range(0, len(arr), 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    print(arr)


# exercise5_3_1(x, y)
# exercise5_3_3(year)
# exercise5_5_3([1, 2, 3, 4, 5, 6])



def exercise5_5_1():
    year = int(input("Введите год "))
    month = int(input("Введите месяц "))
    day = int(input("Введите день "))
    today = datetime.date.today()
    if (today.month - month >= 0 and today.day - day >= 0):
        print(today.year - year, "лет")
    else:
        print(today.year - year - 1, "лет")


def exercise3_5_3(num):
    arr = []

    while num > 0:
        digit = num % 10
        arr.append(digit)
        num //= 10

    arr.sort()

    sort_number = ''
    for digit in arr:
        sort_number += str(digit)

    print(sort_number)
  
# exercise5_5_1()
# exercise3_5_3(35142)