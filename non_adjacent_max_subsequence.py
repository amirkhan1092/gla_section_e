# comma separated number input
# a = eval(input()) # this method can use directly (unpack directly propose to tuple type )
num = list(map(int, input('enter the comma separated number string in single line ').split(','))) # list
# inclusive
inc = 0
# exclusive
exc = 0

for k in num:
    inc, exc = exc + k, inc if inc > exc else exc

result = inc if inc > exc else exc
print('The maximum sub sequence non adjacent sum ', result)
