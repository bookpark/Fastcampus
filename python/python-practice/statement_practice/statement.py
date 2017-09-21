is_holiday = True

if is_holiday:
    print('Good')
else:
    print('Bad')

# 조건표현식
print('Good') if is_holiday else print('Bad')


# 중첩 if문
vacation = 3

if vacation >= 7:
    print('Good')
elif vacation >= 5:
    print('Normal')
else:
    print('Bad')

# 중첩 조건표현식
print('Good') if vacation >= 7 else print('Normal') if vacation >= 5 else print('Bad')

