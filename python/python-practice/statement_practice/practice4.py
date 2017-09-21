# 3000 * 500 / 2
result = 0
for x in range(1000, 2000):
    if x % 2 == 1:
        result += x

print(result)

# List comprehension과 내장함수 sum이용
result = sum([x for x in range(1000, 2000) if x % 2 == 1])
print(result)

# 더 효율적으로 step을 사용
result = sum([x for x in range(1001, 2000, 2)])
print(result)

