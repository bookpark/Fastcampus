l = list('abcd')
d = dict(name='Lux', champion_type='Magician')

print('program start')
try:
    print('before l[5]')
    print('check dict key')
    d['Sona']
    l[5]
    print('after l[5]')
except IndexError as e:
    print('l[5] exception!')
    print(e)
except KeyError as e:
    print("d['Sona'] exception!")
    print(e)
print('program terminate')

"""
while문내에 try 구문에서 input을 이용해 숫자값을 입력 받음
입력받은 숫자값에 해당하는 l[index]를 참조하고, IndexError가 날 경우 다시 숫자값을 입력받음
IndexError가 나지 않으면 while문 종료
"""

while True:
    try:
        value = int(input('숫자 입력:'))
        l[value]
        print(l[value])
    except IndexError:
        print('IndexError!')
    except ValueError:
        print('숫자만 입력해주세요')
    else:
        print('제대로 출력되었습니다.')
        break
    finally:
        print('한 번의 실행이 완료되었습니다.')
