# 1부터 20까지 정수를 갖는 result 리스트
# 슬라이스 연산으로 '홀수'만 가지며 '역순

result = list(range(1, 21))
result1 = result[-2::-2]
print(result1)

# today = '우울한 하루'가 주어졌을 때 '활기찬 하루'로 만드시오
today = '우울한 하루'

today = today.split()
print(today)
today[0] = '활기찬'
today = " ".join(today)
print(today)

# 숫자를 받아 곱을 계산하여 반환하는 myfunc 함수를 만드시오
# 인자가 한개면 제곱, 두개면 두 수의 곱, 그 외에는 Invalid arguments를 출력

def myfunc(*args):
    length = len(args)
    if length == 1:
        return args[0] ** 2
    elif length == 2:
        return args[0] * args[1]
    else:
        print("Invalid arguments")


result3 = myfunc(3)
result3_1 = myfunc(3, 5)
print(result3)
print(result3_1)

# n개의 숫자를 입력받아 제일 큰 숫자를 반환하는 함수 작성
# 오류가 날 경우 오류 메시지를 출력하는

def mymax(*args):
    result = args[0]
    for i in args:
        if result < i:
            result = i
    return result


result4 = mymax(1, 3, 7, 2, 41, 19, 34, 61, 51, 12, 32)
print(result4)

def mymax(*args):
    result = args[0]
    try:
        for i in args:
            if result < i:
                result = i
        return result
    except TypeError:
        return "Invalid arguments"


result4_1 = mymax(1, 3, 7, 2, 41, 19, 34, 61, 51, 12, 32, 'abc')
print(result4_1)

# mymax 함수에 입력된 인자의 개수를 출력하는 mydecorator 함수를 작성

@mydecorator
def mymax(*args):
    result = args[0]
    try:
        for i in args:
            if result < i:
                result = i
        return result
    except TypeError:
        return "Invalid arguments"


def mydecorator(f):
    def rtn_func(*args):
        print(len(args), "개")
        return f(*args)
    return rtn_func


result4_2 = mymax(1, 3, 7, 2, 41, 19, 34, 61, 51, 12, 32)
print(result4_2)