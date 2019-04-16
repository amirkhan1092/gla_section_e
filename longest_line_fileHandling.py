'''
write the function largest() which accept the a filename as a parameter
and reports the longest line along with number of char
'''

def largest(f):
    a = open(f,'r')
    lines = a.readlines()
    a.close()
    lm = [len(i) for i in lines]
    mx = max(lm)
    return mx , lm.index(mx)+1


file = 'tabledata.txt'
char, postion = largest(file)
print('largest line at postion ',postion)
print('number of char ',char)


# a = open('tabledata.txt','r')
#
# data = a.readlines()
# ln = []
# for i in data:
#     ln.append(len(i))
# print(ln)
# mx = max(ln)
# print('maximum char ',mx)
# print('longest line at position  ',ln.index(mx)+1)
#
# a.close()
