
# take a string including with parenthesis
st = input('enter the string with parenthesis')
# counter initialize with zero
c = 0
for i in st:
    if i == '(' :
        c += 1
    elif i == ')' :
        c -= 1
        if c < 0:
            break
if c == 0:
    print('valid arrangment of parenthesis ')
else:
    print(' in-valid arrangement of parentheis ')
