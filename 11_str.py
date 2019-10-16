strin = input('Введите строку:')
strin1 = strin.split()
big_word = 0
for x in range (1, len(strin1)):
    if (len(strin1[big_word])) < len(strin1 [x]):
        big_word = x
print(strin1[big_word])

