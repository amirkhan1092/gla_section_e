import time
a = open('calcihistory.txt','a')

a1 = int(input('enter the 1st number  '))
a2 = int(input('enter the 2nd number' ))
print(
'''
choices 
1>Add
2>Sub
3>Div
4>Mul

'''
)
ti = time.asctime()
c = input('enter the choices  ')
if c == '1':
    re = a1+a2
    op = 'Addition '
elif c == '2':
    re = abs(a1-a2)
    op = 'Sub '
elif c == '3':
    re = a1*a2
    op = 'mul '


f = '{}\t{}\t{}\t{}\t{}\n'. format(a1,a2,op,re,ti)

a.write(f)

a.close()
