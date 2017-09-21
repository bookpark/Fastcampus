import re

result = re.match('Hello', 'Hello, can you hear me?')

import re
source = 'Lux, the lady of Luminosity'
m = re.match('Lux', source)
if m:
    print(m.group())