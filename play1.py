import simple1

exit = 'r'
while(exit != 'q'):
    print('first num')
    x = float(input())
    print('operation')
    op = str(input())
    print('second num')
    y = float(input())

    if op == '+':
        result = simple1.my_sum(x,y)
    elif op == '*':
        result = simple1.my_multi(x,y)
    elif op == '/':
        result = simple1.my_div(x,y)
    else:
        result = 'Not allowed'

    print (result)
    
    print('Enter q for exit, or anykey for continue')
    exit = str(input())

    if exit == 'q':
        break
    else:
        continue