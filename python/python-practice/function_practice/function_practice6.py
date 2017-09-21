print([(lambda a, b : '%d x %d = %d' % (a, b, a * b))(x, y) for x in range(2, 10) for y in range(1, 10)])
