import re
def exercise8_8_2():
    events = [
    {
        'date':  '2019-12',
        'event': 'name1'
    },
    {
        'date':  '2019-12',
        'event': 'name2'
    },
    {
        'date':  '2019-11',
        'event': 'name3'
    },
    {
        'date':  '2019-11',
        'event': 'name4'
    },
    {
        'date':  '2020-10',
        'event': 'name5'
    },
    {
        'date':  '2020-10',
        'event': 'name6'
    },
    {
        'date':  '2020-11',
        'event': 'name5'
    },
    {
        'date':  '2020-11',
        'event': 'name6'
    },
    {
        'date':  '2020-12',
        'event': 'name7'
    },
    {
        'date':  '2020-12',
        'event': 'name8'
    },
    {
        'date':  '2020-12',
        'event': 'name9'
    },
    ]

    result = {}

    for event in events:
        year, month = map(int, event['date'].split('-'))
        if year not in result:
            result[year] = {}
        if month not in result[year]:
            result[year][month] = []
        result[year][month].append(event['event'])

    print(result)

# exercise8_8_2()


def exercise8_9_1():
    affairs = {
    '2019-12-31': ['список дел'],
    '2018-11-29': ['список дел'],
    '2018-11-30': ['список дел'],
    '2018-12-27': ['список дел'],
    '2019-12-29': ['список дел'],
    '2019-12-30': ['список дел'],
    '2018-12-30': ['список дел'],
    '2018-12-31': ['список дел'],
    }

    for date, events in affairs.items():
        if date.startswith('2018'):
            print(f"Дата: {date}, Дела: {events}")

# exercise8_9_1()



def exercise9_1_1(text):
    result = re.split(r'(?<=[.!?]) +', text)
    for i in result:
        print(i)


# exercise9_1_1("Првие! как дела? че ты ка. двылаоф. авофыдлао.афдлвоыадловы.фадлв.одалыфов.")


def exercise9_1_3():
    matrix = [
        [11, 12, 13, 14, 15],
        [21, 22, 23, 24, 25],
        [31, 32, 33, 34, 35],
        [41, 42, 43, 44, 45],
        [51, 52, 53, 54, 55],
    ]

    diagonal = []
    for i in range(len(matrix)):
        diagonal.append(matrix[i][i])
    print(diagonal) 

# exercise9_1_3()



def exercise9_2_1(num):
    i = 2
    factors = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    print(factors) 

# num = int(input("Введите целое число: "))
# exercise9_2_1(num)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def exercise9_2_3(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    print(primes) 
    


# start = int(input("Введите первое целое число: "))
# end = int(input("Введите второе целое число: "))
# exercise9_2_3(start, end)
