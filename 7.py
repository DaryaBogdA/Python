def z2_1_1():
  l = ["http://dkdkdk", "Hello world", "apple", "http://boyfreind"] 
  mas = []
  for i in l:
    if "http://" in i:
      mas.append(i)
  print (mas)



def z2_1_3():
  l = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
  print (l)
  mas = []
  x = int(input("Введите, что хотите удалить из списка: "))  
  for i in l:
     if i != x:
         mas.append(i)
  print (mas)         
      



def z2_1_5():
  l = 'abcdeabc' 
  l2 = ""
  for i in l:
     if i not in l2:
         l2 += i
  print (l2)         

# z2_1_1()
# z2_1_3()
# z2_1_5()



def z2_2_1():
  l = [1, 2, -3, 4, 5, -6, -7, 8, 9] 
  count = 0
  for i in l:
     if i < 0:
        count += 1
  print (count)


def z2_2_3():
    l = 'abcdeabc' 
    l = l[:-2] + l[-1]
    print (l)



def z2_2_5():
  l = [1.456, 2.125, 3.32, 4.1, 5.34]
  mas = []
  for i in l:
     i = round(i, 1)
     mas.append(i)
  print (mas)

# z2_2_1()
# z2_2_3()
# z2_2_5()


    
def z2_3_1():
  x = input("Введите  первое слово: ")
  y = input("Введите второе слово: ")
  if x[-1] == y[0]:
      print ("последняя буква первого слова совпадает с первой буквой второго слова")
  else:
      print ("no")
    
def z2_3_3():
   l = '12,34,56'
   l = l.split(",")
   summa = 0
   for i in l:
    summa += int (i)
   print (summa) 

def z2_3_5():
  dct = {
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}
  dct2 = set()
  for key in dct:
     dct2.add(dct[key])
  print (dct2)

# z2_3_1()
# z2_3_3()
# z2_3_5()



def z2_4_1():
  x = input("Введите слово: ")
  count = -1
  for i in x:
    count +=1
    if i >= '0' and i <= '9':
       print (count)
       break

def z2_4_3():
  dct = {
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}
  dct2 = set()
  for key in dct:
      dct2.add(key)
  print (dct2)



    
def z2_4_5():
  l = 'aaa bbb ccc'
  l = l.split()
  print (l)
  l2 = ''
  for i in l:
     i = i.capitalize()
     l2 += i + ' '
  print (l2)

# z2_4_1()
# z2_4_3()
# z2_4_5()


def z2_5_1():
  l = '023m0df0dfg0'
  mas = []
  for i in range(len(l)):
   if l[i] == '0':
    mas.append(i)
  print (mas)

    
def z2_5_3():
  l = [1, 2, 3, 4, 5, 6]
  sumCH = 0
  sumneCH = 0
  for i in range(len(l)):
    if i % 2 == 0:  
        sumCH += l[i]
    else:
        sumneCH += l[i]
  print (sumCH/sumneCH)
  
# z2_5_1()
# z2_5_3()