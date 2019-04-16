with open('lines.txt','r') as a:

# data1 = a.readline()
# data2 = a.readline()

    data = next(a)
    print(data)
    # print(data2)
print(a.closed)

