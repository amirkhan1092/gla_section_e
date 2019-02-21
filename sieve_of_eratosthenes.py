n = int(input('enter the value for prime number list '))

# list initialized with all data True
prime = [True for i in range(n+1)]
# prime number starting init
p = 2
# iteration until the value reach to given limit
while p < n:
    if prime[p]:
        for k in range(p+p,n+1,p):
            prime[k] = False
    p += 1

for i in range(2, n+1):
    if prime[i]:
        print(i)  # output print (only prime number )

