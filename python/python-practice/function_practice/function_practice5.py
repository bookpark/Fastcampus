def count_args(*args):
    print('%d개' % len(args))

count_args(1, 2, 3, 4)


def args_count(*args):
    c = len(args)
    print(c)
    return c

result = args_count(3, 5, 2, 10, 'ABC')
print(result)
