import math
# rows value
n0 = int(input('enter the value of number of rows '))

for rows in range(n0):
    print(' '*(n0-rows-1),end='')
    n = 1
    for column in range(rows+1):
        print(' '+str(n), end='')
        n = math.ceil(n*(rows-column)/(column+1))

    print()
