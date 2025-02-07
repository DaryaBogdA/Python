import re

def exercise1(sample):
    pattern = r'^[0-9]{6}$'
    if re.match(pattern, str(sample)):
        print('yes')
    else:
        print('no')
     

# exercise1(24567)
# exercise1(123456)
# exercise1(1234567)

def exercise2(sample):
    pattern = r'^#[0-9a-z]{6}$'
    if re.match(pattern, str(sample), flags=re.IGNORECASE):
        print('yes')
    else:
        print('no')
     
# exercise2("#FFFFFF")
# exercise2("#FF3421")
# exercise2("#00ff00")
# exercise2("232323")
# exercise2("f#fddee")
# exercise2("#fd2")


def exercise3(sample):
    pattern = r'^[0-9]+([.,]?[0-9]+)?$'
    if re.match(pattern, str(sample)):
        print('yes')
    else:
        print('no')
     

# exercise3('1.22')
# exercise3('5')
# exercise3('324545,123231')
# exercise3('324.')
# exercise3(',1587')
# exercise3('02.qwe')


def exercise4(sample):
    pattern = r'^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$'
    if re.match(pattern, str(sample)):
        print('yes')
    else:
        print('no')



# exercise4('127.0.0.1')
# exercise4('255.255.255.0')
# exercise4('192.168.0.1')
# exercise4('1300.6.7.8')
# exercise4('254.hzf.bar.10')


def exercise5(sample):
    pattern = r'^\{?[0-9a-z]{8}(-[0-9a-z]{4}){3}-[0-9a-z]{12}\}?$'
    if re.match(pattern, str(sample), flags=re.IGNORECASE):
        print('yes')
    else:
        print('no')


# exercise5('{e02fa0e4-01ad-090A-c130-0d05a0008ba0}')
# exercise5('ep3fd0e4-00fd-090A-ca30-0d00a0038ba0')
# exercise5('02fa0e4-01ad-090A-c130-0d05a0008ba0}')
# exercise5('e02fd0e400fd090Aca300d00a0038ba0')
# exercise5('strrev')
# exercise5('replace')
