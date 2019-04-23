# a = {'car': ['alto', 'nano'], 'speed': 110, 'model': 2019}
# a['speed'] = 210
# print(a)






# change key of any dict
a = {'car': ['alto', 'nano'], 'speed': 110, 'model': 2019}

for i in a:
    a[i.upper()] = a.pop(i)

print(a)







# Addition (append or merging dictionary )
a = {1: 'one', 2: 'two'}
b = {3: 'three', 4: 'four', 2:'43'}

a.update(b)

print(a)




a = [('b','i'),('c','i')]

d = a.pop()

print(d)




# sorting of dictionary
a = {'CAR': ['alto', 'nano'], 'SPEED': 110, 'MODEL': 2019}


s = sorted(a.items())

a = dict(s)

print(a)



# for i in b:
#     print(a[i],end = ' ')
# {'CAR': ['alto', 'nano'], 'MODEL': 2019, 'SPEED': 110}




# clear all data from dictionary
d = {'CAR': ['alto', 'nano'], 'SPEED': 110, 'MODEL': 2019}

d.clear()

print(d) # {}



# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = {3: 'three', 4: 'four',2:'22'}

k = b.popitem()

print(k)
# (2,'22')

'''
Python Dictionary Comprehension
Dictionary comprehension consists of an expression pair (key: value) 
followed by for statement inside curly braces {}.
'''

# k = [i for i in range(10)]

sq1 = {x:x*x for x in range(10)}
sq2 = {x: None for x in range(10)}

# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print(sq1)






print()
