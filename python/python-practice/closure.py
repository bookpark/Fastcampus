level = 0

def outer():
    level = 50

    def inner():
        nonlocal level
        level += 3
        print(level)

    return inner

f1 = outer()
f2 = outer()

print(f1)
print(f2)

f1()
f1()
f2()
