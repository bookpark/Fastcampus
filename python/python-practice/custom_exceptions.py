import re

class NotMatchedException(Exception):
    def __init__(self, pattern, source):
        self.pattern = pattern
        self.source = source

    def __str__(self):
        return f'Pattern "{self.pattern}" is not matched in source "{self.source}"'

def search_from_source(p, s):
    m = re.search(p, s)
    if not m:
        raise NotMatchedException(p, s)
    return m

source_string = 'Lux, the Lady of Luminosity'
pattern_string = r'L\w{5}\b'

result = None
try:
    result = search_from_source(pattern_string, source_string)
    print(result)
except NotMatchedException as e:
    print(e)

print('Search result: ', result)
