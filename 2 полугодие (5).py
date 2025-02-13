import re

def exercise1(sample):
    pattern = r'^(?!.*\.\.)(?!.*\.\-)(?!.*\-\-)(?!.*\-\.)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    if re.match(pattern, sample):
        print('yes')
    else:
        print('no')
     

# exercise1("vasya-pupkin@mail.com")
# exercise1("v.v.pupkin@firma.mail.com")
# exercise1("v.v.pupkin-director@firma.mail.com")
# exercise1("-vasya--pupkin@mail.com")
# exercise1("vasya.-pupkin@mail.com")
# exercise1("vasya_pupkin@mail..com")
# exercise1("vasya.-pupkin@mail.com")
# exercise1("v.v.pup kin@firma.mail.com")

def exercise2(text):
    pattern = r'<!--.*-->'
    print(re.sub(pattern, '', text))


html_text = '''
<div>
  <!-- HTML-комментарий -->
  <p>gfdsgf</p>
  <!--[if IE]>
  <link href="/css/invstroyIEfix.css" rel="stylesheet" type="text/css" />
  <![endif]-->
  <!--ddd HTML-комментарий -->
</div>
'''

# exercise2(html_text)



def exercise3():
    with open('папа/32.html', 'r', encoding='utf-8') as file:
        text = file.read()
    pattern = r'<.*?>'
    cleaned_text = re.sub(pattern, '', text)
    with open('папа/32_cleaned.txt', 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

    print(cleaned_text)


# exercise3()


def exercise4():
    with open('папа/exer4.html', 'r', encoding='utf-8') as file:
        text = file.read()
    pattern = r'\b[A-ZА-Я]{5,}\b'
    def replacer(match):
        return f'<div style="color: red; font-weight: bold;">{match.group(0)}</div>'
    
    cleaned_text = re.sub(pattern, replacer, text)
    
    with open('папа/32_replace.html', 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

    print(cleaned_text)


# exercise4()

def exercise5():
    with open('папа/yandex.html', 'r', encoding='utf-8') as file:
        text1 = file.read()
    with open('папа/mail.ru.html', 'r', encoding='utf-8') as file:
        text2 = file.read()

    pattern = r'<a href.*?>'

    cleaned_text_1 = re.finditer(pattern, text1)
    cleaned_text_2 = re.finditer(pattern, text2)
    
    with open('папа/5_replace.txt', 'w', encoding='utf-8') as file:
        file.write("https://360.yandex.ru/mail/\n")
        for match in cleaned_text_1:
            file.write(match.group(0) + "\n" + "\n")
        
        file.write("\nhttp://www.mail.ru/\n")
        for match in cleaned_text_2:
            file.write(match.group(0) + "\n"+ "\n")



exercise5()