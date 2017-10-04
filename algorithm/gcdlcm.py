# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환해주는 gcdlcm 함수를 완성해 보세요.
# 배열의 맨 앞에 최대공약수, 그 다음 최소공배수를 넣어 반환하면 됩니다.
# 예를 들어 gcdlcm(3,12) 가 입력되면, [3, 12]를 반환해주면 됩니다.


def gcdlcm(a, b):
    answer = []
    x = min(a, b)
    y = min(a, b)
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            answer.append(i)
            break
        pass
    answer.append(int(a * b / answer[0]))
    # i = 1
    # while True:
    #     j = y * i
    #     if j % x == 0:
    #         answer.append(j)
    #         break
    #     else:
    #         i += 1
    return answer


print(gcdlcm(3, 12))
