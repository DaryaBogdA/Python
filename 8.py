def exercise2_6_1(l):
  mas = []
  for i in range(len(l)):
    if l[i] >= '0' and l[i] <= '9':
      mas.append(i)
  print (mas)


def exercise2_6_3():
  num = [1, 2, 3, 4, 5, 6]
  mas = []
  for i in range(0, len(num), 2):
      mas.append(num[i]*10 + num[i + 1])
  print(mas) 


     

# exercise2_6_1('023m0df0dfg0')
# exercise2_6_3()



def exercise2_7_1(l):
  if l.isupper():
     print(f"{l}:\nВ верхнем регистре")
  else:
     print(f"{l}:\nВ нижнем регистре")

def z2_2_3():
    l = 'abcdeabc' 
    l = l[:-2] + l[-1]
    print (l)



def exercise2_7_3():
  l = ('2025', '12', '31')
  dict = {
    'year': l[0],
    'month': l[1],
    'day': l[2],
  }
  print(dict)



# exercise2_7_1("д")
# exercise2_7_3()



    
def exercise2_8_1():
  mas = []
  for i in range(1, 11):
      mas.append(i)
  print(mas) 
    

def exercise2_8_3():
   l = ['1', '2', '3', '4', '5']
   mas = []
   for i in range(len(l)):
    mas.append(int(l[i]))
   print (mas) 


# exercise2_8_1()
# exercise2_8_3()



def exercise2_9_1():
  mas = []
  for i in range(1, 101):
      if i % 2 == 0:
        mas.append(i)
  print(mas) 
    

def exercise2_9_3(txt1, txt2):
  dct = {}
  for i in range(len(txt1)):
    dct[txt1[i]] = int(txt2[i]) 
  print(dct)



# exercise2_9_1()
# exercise2_9_3('abcde', '12345')


def exercise2_10_1(l):
  count = 0
  for char in l:
    if char.isalpha():
      count += 1
  if count >=3:
       print("Больше трех букв")
  else:
       print("Меньше трех букв")

    
def exercise2_10_3(l):
  result = ''
  for i in l.split():
    result += '!' + i[1:] + ' '
  print(result)

  
# exercise2_10_1('023m0df0dfg0')
# exercise2_10_3('abcde abcde abcde')
