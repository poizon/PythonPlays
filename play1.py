import simple1
"""
  Играемся с импортом своего модуля, обработкой исключений
  Все коряво - но пока так и надо :))
"""
exit = 'r'
while(exit != 'q'):
    print('first num')
    
    try: 
        x = float(input())
    except Exception:
        print('Whats the fuck?')
        x = 0
   
    print('operation')

    try:
        op = str(input())
    except Exception:
        print('Whats the fuck?')        
        op = '+'

    print('second num')
    try:
        y = float(input())
    except Exception:
        print('Whats the fuck?')        
        y = 1

    if op == '+':
        result = simple1.my_sum(x,y)
    elif op == '*':
        result = simple1.my_multi(x,y)
    elif op == '/':
        result = simple1.my_div(x,y)
    else:
        result = 'Not allowed'
    """ печатаем результат """
    print (result)
    
    print('Enter q for exit, or anykey for continue')
    exit = str(input())

    if exit == 'q':
        break
    else:
        continue