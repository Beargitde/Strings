strin = input('Введите строку:')
x = strin.find('x')
w = strin.find('w')
if x < w:
    print('x встречается раньше!')
elif x > w:
    print('w встречается раньше!')
else:
    print('символы не найдены!')
    


