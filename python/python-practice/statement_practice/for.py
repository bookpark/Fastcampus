fruits = ['apple', 'banana', 'melon']
colors = ['red', 'yellow', 'green', 'purple']

index = 0
for fruit in fruits:
    print('Fruit(%s), Color(%s)' % (fruit, colors[index]))
    index += 1

print(zip(fruits, colors))
