from fractions import gcd

def gcdlcm(a, b):
    return int(gcd(a, b)), int(a * b / gcd(a, b))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))