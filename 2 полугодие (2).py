import datetime

def exercise4_6_1(arr):
    new_arr = []
    for i in arr:
        if "0" in str(i):
            new_arr.append(i)
    print(new_arr)



# exercise4_6_1([123, 950, 403, 23, 30, 54, 403, -39, -409])


def exercise5_6_1():
    email = input("Введите email ")
    if "@gmail.com" in email:
        print("yes")
    else:
        print("no")




def exercise5_6_3(arr):
    new_arr = []
    for i in arr:
        for j in str(i):
            new_arr.append(int(j))
    print(new_arr)

# exercise5_6_1()
# exercise5_6_3([123, 456, 789])



def exercise6_6_1():
    year = int(input("Введите год "))
    month = int(input("Введите месяц "))
    day = int(input("Введите день "))
    today = datetime.date.today()
    if (today.month - month < 0 and today.day - day < 0 and today.year - year < 0):
        print("false")
    else:
        print("true")


def exercise6_6_3(str):
    str = str.split()
    new_str = []
    for i in str:
        new_str.append(i[0].upper())
    new_str = ''.join(new_str)
    print(new_str)


def exercise6_6_5(seconds):
    day = seconds // 86400
    hour = seconds // 3600
    minute = seconds // 60
    result = dict(d = day, h = hour, m = minute, s = seconds)
    print(result)
# exercise6_6_1()
# exercise6_6_3("Привет мой милый лютик")
# exercise6_6_5(35142)


def exercise7_1_1():
    with open('7_2_1.txt') as file:
        text = file.read()
    count = 0
    for char in text:
        count += 1
    print(count)


def exercise7_1_3():
    with open('7_2_1.txt') as file:
        text = file.read()
    text = text.split()
    new_text = ''
    for i in text: 
        new_text += f'({i})'
    with open('new.txt', 'w') as new_file:
        new_file.write(new_text)
    print("все")


def exercise7_1_5():
    arr = []
    for i in range(3):
        arr2 = []
        for j in range(3):
            arr2.append([1, 2, 3])
        arr.append(arr2)
    print(arr)


# exercise7_1_1()
# exercise7_1_3()
# exercise7_1_5()


def exercise7_3_1():
    with open('7_3_1.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    text = text.split()
    result = []
    for i in text:
        try:
            number = int(i)
            result.append(str(number**2))
        except ValueError:
            result.append(i)

    text2 = ' '.join(result)
    with open('7_3_1.txt', 'w', encoding='utf-8') as file:
        file.write(text2)
    print("да")


def exercise7_3_3(arr):
    with open('7_3_3.txt', 'w', encoding='utf-8') as file:
        for i in arr:
            file.write(str(i) + '\n')
    print("да")

# exercise7_3_1()
# exercise7_3_3([1, 5, 'asdf', 4, 56, 7676, "asdfgrtht"])


