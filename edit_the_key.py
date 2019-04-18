# change key of any dict
a = {'car': ['alto', 'nano'], 'speed': 110, 'model': 2019}

for i in a:
    a[i.upper()] = a.pop(i)
# del a['car']

# {'CAR': ['alto', 'nano'], 'SPEED': 110, 'MODEL': 2019}
print(a)


# Addition (append or merging dictionary )
a = {1: 'one', 2: 'two'}
b = {3: 'three', 4: 'four', 2: 'ab'}

a.update(b)
# {1: 'one', 2: '22', 3: 'three', 4: 'four'}
print(a)



# sorting of dictionary
a = {'CAR': ['alto', 'nano'], 'SPEED': 110, 'MODEL': 2019}


b = sorted(a.items())

a = dict(b)

# for i in b:
#     print(a[i],end = ' ')

print(a)