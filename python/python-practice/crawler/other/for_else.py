import sys

l = list(range(5))

# greater_than_5 = False

for item in l:
    print(item)
    if item > 5:
        # greater_than_5 = True
        break
else:
    print('5보다 큰 값이 없음')
    sys.exit(0)
print('5보다 큰 값이 있음')


# print('l이라는 리스트 변수 내에 5보다 큰 값이 있었는지: ', greater_than_5)