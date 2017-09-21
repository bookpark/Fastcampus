
def mymax(*args):
    try:
        max_num = args[0]
        for i in args:
            if max_num < i:
                max_num = i
        print(max_num)
    except TypeError:
        print('Invalid arguments')

mymax(1,2,3,4,5,6,7,8)
