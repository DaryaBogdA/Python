import datetime
import random
import string

def exercise6_1_1():
    today = datetime.date.today()
    day = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    print(day[today.weekday()])


def exercise6_1_3(num):
  print(num // 86400)


def exercise6_1_4(num, str):
  str = str[:num]
  print(str)

     

# exercise6_1_1()
# exercise6_1_3(432000)
# exercise6_1_4(4, "asdsaddsad")




def exercise6_3_1(arr):
    arr = set(arr)
    print(arr) 



def exercise6_3_3(arr):
    new_arr = []
    for num in arr:
        if new_arr and num == new_arr[-1]:
            continue
        new_arr.append(num)
    print(new_arr)

# exercise6_3_1([1, 4, 5, -6, 1, 2, 7, 8, 3, 2, 5, 6, 5, -4, 1, 0])
# exercise6_3_3([1, 3, 4, 4, 6, 4, 7, 7, 8, 3, 3, 0])



def exercise6_5_1(str):
    str = str.isalpha()
    print(str)

def exercise6_5_3(arr):
    digit = 0
    digit2 = 0
    new_arr = []
    for num in arr:
        if num > digit:
            digit = num
    for num in arr:
        if num < digit:
            new_arr.append(num)
    for num in new_arr:
        if num > digit2:
            digit2 = num
    print(digit2)
  

def exercise6_5_5(lenght):
    arr = []
    for i in range(lenght):
        arr.append(random.choice(string.ascii_letters))

    print(arr)
  
# exercise6_5_1("asdfasdf")
# exercise6_5_3([6, -5, 45, 65, 11, 54, 5])
# exercise6_5_5(8)




def exercise7_2_1():
    with open('7_2_1.txt') as file:
        text = file.read()
    count = 0
    for char in text:
        if char.isalpha():
            count += 1
    print(count)


def exercise7_2_3():
    with open('7_2_3.txt') as file:
        max_number = 0
        for i in file:
            for number in i.split(","):
                number = int(number)
                if number > max_number:
                    max_number = number
    print(max_number)


def exercise7_2_5(char, num):
    arr = []
    for i in range(num):
        arr.append([char] * i)
    print(arr)

     

# exercise7_2_1()
# exercise7_2_3()
# exercise7_2_5('g', 6)
