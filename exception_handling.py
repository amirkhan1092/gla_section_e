e='''
Exception handling 

Type of error

1. Syntax error : Parser error 
2. Runtime error (Exceptions ) 
 


'''


while 1:
    try:
        a = int(input('enter the number only '))
        print('succesfully got the value ')
        break
    except (EOFError, KeyboardInterrupt) :
        print('try Again !')
