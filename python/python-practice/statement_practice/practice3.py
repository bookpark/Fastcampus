for x in range(7):
    for y in range(4):
        if x % 2 == 0:
            print((x, y))


l = [(x, y) for x in range(7) for y in range(4) if x % 2 == 0]
print(l)

