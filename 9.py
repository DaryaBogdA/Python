def exercise3_1_1():
    num = [x for x in range(1, 7)]
    print(num) 



def exercise3_1_3(l):
  summa = 0
  l2 = len(l) // 2
  for i in range(l2):
      summa += l[i]
  print(summa) 


     

# exercise3_1_1()
# exercise3_1_3([1, 2, 3, 4, 5, 6])


def exercise3_2_1():
    num = [x for x in range(1, 10, 2)]
    print(num) 





def exercise3_2_3():
    dct1 = {
	'a': 1,
	'b': 2,
    }
    dct2 = {
	'c': 3, 
	'd': 4,
    }
    dct3 = dct1.copy()
    dct3.update(dct2)
    print(dct3) 

# exercise3_2_1()
# exercise3_2_3()



    
def exercise3_3_1(num):
  odd = True
  for i in str(num):
      if int(i) % 2==0:
         odd = False
  if odd:
     print("все нечетные") 
  else:
    print(" не все нечетные") 



def exercise3_3_3():
    st1 = {1, 2, 3}
    st2 = {4, 5, 6}
    st3 = st1 | st2
    print(st3) 


# exercise3_3_1(1357)
# exercise3_3_3()



def exercise3_4_1(l):
  vowels = "уеыаоёэяиюУЕЫАОЁЭЯЮИ"
  rez =  ""
  for i in l:
      if i not in vowels:
        rez +=i
  print(rez) 
    

def exercise3_4_3():
    st1 = {1, 2, 3, 4, 5}
    st2 = {4, 5, 6, 7, 8}
    st3 = st1 ^ st2 
    print(st3) 


# exercise3_4_1("фываолдж")
# exercise3_4_3()



def exercise3_5_1(l):
    l = l.split()
    mas = []
    for i in l:
       if i.lower().startswith("а"):
          mas.append(i)
    print(mas) 

    
def exercise3_5_3():
    lst1 = [1, 2, 3, 4, 5]
    lst2 = [4, 5, 6, 7, 8]
    lst3 = list(set(lst1) & set(lst2))
    print(lst3)
  
# exercise3_5_1("как я люблю Астрахань апельсиныб а не мандарины и арбуз антошка пошел копать картошку аливидэрчи")
# exercise3_5_3()