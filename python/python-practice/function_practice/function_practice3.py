def mul(*args):
    if len(args) == 1:
        return args[0] ** 2
    elif len(args) == 2:
        return args[0] * args[1]
    else:
        raise Exception('require arguments')

result1 = mul(3)
result2 = mul(3, 10)

print(result1)
print(result2)
