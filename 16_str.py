strin1 = input('Введите строку 1:')
strin2 = input('Введите строку 2:')
a = len(strin1)
b = len(strin2)
c = a - b
c = abs(c)
if a>b:
    for x in range(1,c+1):
        print(strin1)
elif b>a:
    for x in range(1, c+1):
        print(strin2)






