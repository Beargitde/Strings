import re

s = str(input('Введите строку:'))
s2 = re.sub(r'\d', '', s)
print(s2)
