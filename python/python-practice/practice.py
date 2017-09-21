for x in range(7):
    for y in range(4):
        print('(%d, %d)' % (x, y))

l = [('(%d, %d)' % (x, y)) for x in range(7) for y in range(4)]
print(l)


l = [('(%d, %d)' % (x, y)) for x in range(7) for y in range(4) if x % 2 == 0]
print(l)


l = [('(%d, %d)' % (x, y)) for x in range(7) for y in range(4) if y % 2 == 0]
print(l)

sum = 0
for i in range(1000, 2001):
    if i % 2 != 0:
        sum += i
print(sum)

l = [i for i in range(1, 100) if  i % 7 == 0 if i % 9 == 0]
print(l)

gugu = [('(%d x %d = %d)' % (x, y, x * y)) for x in range(2, 10) for y in range(2, 10)]
print(gugu)