def upper_if_gt_i(char):
    if char > 'i':
        return char.upper()
    else:
        return char

import string
for char in string.ascii_lowercase:
    print(upper_if_gt_i(char))


for char in string.ascii_lowercase:
    print((lambda x: x.upper() if x > 'i' else x)(char))
