h = '''
Exception handling 

Type of error

1. Syntax error : Parser error 
2. Runtime error (Exceptions ) 


'''


a = 10
b = 90
c = 0
try:
    c = a/int(input('enter the value '))
except ValueError:
    print('Value error handled ')

print(c)