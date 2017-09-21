def print_arg_type(f):
    def rtn_function(*args):
        for arg in args:
            print('%s type: %s' % (arg, type(arg)))
        return f(*args)
    return rtn_function

@print_arg_type
def print_string(s):
    print(s)

@print_arg_type
def print_int(i):
    print(i)

print_string('abc')
print_int(123)       
