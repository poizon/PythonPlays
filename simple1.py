def my_sum(x,y):
    return x+y

def my_multi(x,y):
    return x*y

def my_div(x,y):
    result = 0
    try:
        result = x/y
        return result
    except ZeroDivisionError:
        print('Division by zero!')
        return result

    