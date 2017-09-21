# 7의 배수이거나 9의 배수인 정수를 담을 list
result = []

# 1부터 99까지를 순회, 각 순회 아이템은 x변수에 할당
for x in range(1, 100):
    # x가 7로 나누어지거나 9로 나누어질 경우에는
    if x % 7 == 0 or x % 9 == 0:
        # 결과 list의 마지막에 해당 x변수를 삽입
        result.append(x)
print(result)

# List comprehension

result = [x for x in range(1, 100) if x % 7 == 0 or x % 9 == 0]
print(result)
