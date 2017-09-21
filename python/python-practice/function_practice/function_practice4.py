def rtn_tuple(x, y):
    if y > x:
        return x + y, y - x
    else:
        return x + y, x - y

print(rtn_tuple(1, 2))
