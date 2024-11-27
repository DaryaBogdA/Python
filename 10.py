import random
def game_random_number():
    computer_number = random.randint(1, 100)
    print(computer_number)

    count = 0
    while(True):
        you_number = int(input("Введите число "))
        if you_number == computer_number:
            print("Вы выиграли")
            break
        elif you_number > computer_number:
            print("Введите число поменьше")
            count+=1
        else:
            print("Введите число побольше")
            count+=1
    print(f"Вам понадобилось {count} попыток")

# game_random_number()

def exercise3_6_1(l):
    l2 = ""
    for x in l:
       l2 += str(x)
    l2 = l2.split(" ")
    l3 = []
    for world in l:
       if len(str(world)) < 3:
          l3.append(world)
    print(l3)



def exercise3_6_3(num):
    l = str(num)
    rez = True
    for i in l:
        if int(i) > 0:
          rez = True
        else:
          rez = False
    if rez:
       print("все цифры больше 0")
    else:
       print("не все цифры больше 0")
       


     

# exercise3_6_1([1, 22, 3333, 4444, 55, 61])
# exercise3_6_3(12345)


def exercise3_7_1(l):
    l = l.split(" ")
    rez = ""
    for world in l:
        rez += world[:-1] + world[-1].upper() + " "
    print(rez)




def exercise3_7_3():
    txt1 = '12345'
    txt2 = '45678'
    rez = "".join(set(txt1) & set(txt2))
    print(rez)



# exercise3_7_1("как я люблю астрахань апельсиныб а не мандарины и арбуз антошка пошел копать картошку аливидэрчи")
# exercise3_7_3()



    
def exercise3_8_1(arr):
  rez = False
  for i in arr:
    if "3" in str(i):
         rez = True
    else:
       rez = False
  if rez:
     print("все числа из этого списка содержат в себе цифру 3") 
  else:
    print("не все числа из этого списка содержат в себе цифру 3") 



def exercise3_8_3():
    p = 7
    # я хз че тут дедать с кебабом

def exercise3_8_5():
    p = 7
    # я хз че тут дедать с кебабом

# exercise3_8_1([13, 22, 3333, 4444, 55, 61])
# exercise3_8_3()
# exercise3_8_5()



def exercise3_9_1(l):
  l = [130, 2002, 303303, 44440, 55, 61]
  l2 = []
  for i in l: 
    count = 0
    for k in str(i):
          if k == "0":
             count += 1
    if count < 2:
        l2.append(i)
  print(l2) 
    

def exercise3_9_3(l):
    l2 = []
    for i in l:
        l2 += [i] * 2
    print(l2)


# exercise3_9_1([130, 2002, 303303, 44440, 55, 61])
# exercise3_9_3([1, 2, 3])



def exercise3_10_1(l, k):
    l2 = []
    for i in l:
       if i % k == 0:
          l2.append(i)
    print(l2) 


def exercise3_10_3(num1, num2):
    num1 = 12345
    num2 = 34567
    rez = set(str(num1)) | set(str(num2))
    rez2  = [int(i) for i in rez]
    print(rez2)



def exercise3_10_5(l):
    rez = []
    for num in l:
        num = str(num)
        digits = set(num)
        if len(digits) == len(num):
            rez.append(int(num))
    print(rez)




def exercise3_10_7(l):
    l = [123, 456, 789]
    l2 = []
    for i in l:
       l2.append(int(str(i)[::-1]))
    print(l2)


# exercise3_10_1([1, 10, 3, 25, 5], 5)
# exercise3_10_3(12345, 34567)
# exercise3_10_5([1, 10, 77, 3, 25, 5])
# exercise3_10_7([123, 456, 789])

            #игра кубики


def randomNumber():
    num = random.randint(1, 6)
    return num


def cube(number):
    for i in range(2):
        print("*" * 5)
        print("*   *")
        print("*" + " " + str(number[i])+ " " + "*")
        print("*   *")
        print("*" * 5)



def gameBlock():
    countYou = 0
    countComputer = 0
    while True:
        step = int(input("Кто ходит первыый? 1 - ты, 2 - компьютер "))
        if step == 1:
            for i in range(5):
                number = [randomNumber(), randomNumber()]
                cube(number)
                countYou += number[0] + number[1]
                print("Сyмма ваших очков: ", countYou)

                number2 = [randomNumber(), randomNumber()]
                cube(number2)
                countComputer += number2[0] + number2[1]
                print("Сyмма очков компутера: ", countComputer)

            print(f"Среднее количество ваших очков: {countYou / 5}")
            print(f"Среднее количество очков компутера: {countComputer / 5}")

            if countYou > countComputer:
                print("Вы выйграли")
            elif countYou < countComputer:
                print("Компутер выиграл")
            else:
                print("У вас ничья")
            break
        elif step == 2:
            for i in range(5):
                number2 = [randomNumber(), randomNumber()]
                cube(number2)
                countComputer += number2[0] + number2[1]
                print("Сyмма очков компутера: ", countComputer)

                number = [randomNumber(), randomNumber()]
                cube(number)
                countYou += number[0] + number[1]
                print("Сyмма ваших очков: ", countYou)

            print(f"Среднее количество очков компутера: {countComputer / 5}")
            print(f"Среднее количество ваших очков: {countYou / 5}")

            if countYou > countComputer:
                print("Вы выйграли")
            elif countYou < countComputer:
                print("Компутер выиграл")
            else:
                print("У вас ничья")
            break
        print("Ты тупой?")


   
gameBlock()
