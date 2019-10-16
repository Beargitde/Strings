import copy


strin = input('Введите строку:')
strin = list(strin)
a1 = strin.index(',')
a1 = a1 + 1
print(a1)
strin1 = copy.copy(strin)
strin1[0:a1] = []
print(strin1)
a2 = strin1.index(',')
a2 = a2 + a1
print(a2)
print(strin[a1:a2])






