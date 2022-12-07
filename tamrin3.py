
'''Tamrin-3'''


i = 1
a = 1
b = 1

while i <= 10 :
    x = float(input('enter X ? '))

    if x >=5:
        while b <=x :
            a = a*b
            b +=1
        print( x , '==>', a)
    elif x>= 0 and x < 5 :
        y = 3*x**4
        print(x , ' ==>', y)
    else:
        y = (3*x)**6
        print(x , ' ==>', y)
    
    i +=1
    b = 1
    a = 1
    
        


