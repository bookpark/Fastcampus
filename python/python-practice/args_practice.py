def multiply_args(*args):
    if len(args) == 1:
        return args[0] ** 2
    elif len(args) == 2:
        return args[0] * args[1]

print(multiply_args(3))
print(multiply_args(5, 7))
