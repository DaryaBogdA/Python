import datetime


def exercise4_1_1(num):
    num = str(num)
    for i in range(1, len(num)):
        if num[i] < num[i-1]:
            return False
    return True


def exercise4_1_3():
    l = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
  ]
    for i in l:
        for j in i:
            print(j)

     

# print(exercise4_1_1(131579))
# exercise4_1_3()


    
def exercise4_3_1(l):
  l2 = []
  for i in range(0, len(l)):
      if (i + 1) % 5 != 0:
          l2.append(l[i])
  print(l2)



def exercise4_3_3():
    txt1 = 12345
    txt2 = 45678
    res = tuple(set(str(txt1)) & set(str(txt2)))
    result = [int(i) for i in res]
    print(result)

# exercise4_3_1([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
# exercise4_3_3()




def exercise4_5_1():
    for i in range(10, 1001):
       if (i // 10 % 10) % 2 == 0:
          print(i) 
    

    
def exercise4_5_3():
    dct = {
    1: {
        1: {
        1: 111,
        2: 112,
        3: 113,
        },
        2: {
        1: 121,
        2: 122,
        3: 123,
        },
    },
    2: {
        1: {
        1: 211,
        2: 212,
        3: 213,
        },
        2: {
        1: 221,
        2: 222,
        3: 223,
        },
    },
    3: {
        1: {
        1: 311,
        2: 312,
        3: 313,
        },
        2: {
        1: 321,
        2: 322,
        3: 323,
        },
    },
    }
    sum = 0
    for key1, value1 in dct.items():
        for key2, value2 in value1.items():
            for key3, value3 in value2.items():
                sum += value3
    print(sum)
  
# exercise4_5_1()
# exercise4_5_3()




def exercise5_2_1():
    year = int(input("Введите год "))
    month = int(input("Введите месяц "))
    day = int(input("Введите день "))
    try:
        datetime.date(year, month, day)
    except ValueError:
        print("Введена дата некорректна")
    else:
        print("Введена дата корректна")
    

    
def exercise5_2_3():
    result = ' '
    for i in range(1,6):
        result += str(i)
    print(result)
  
# exercise5_2_1()
exercise5_2_3()