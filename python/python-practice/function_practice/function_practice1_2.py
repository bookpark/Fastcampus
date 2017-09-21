def print_string(s):
    'this is an explaination on this function'
    if s == 'red':
        return 'apple'
    elif s == 'yellow':
        return 'banana'
    elif s == 'green':
        return 'melon'
    else:
        return "I don't know"

result = print_string('red')
print(result)
#help(print_string)

def fruit_dict(color):
    fruit_color_dict = {
        'red': 'apple',
        'yellow': 'banana',
        'green': 'melon'
    }
    return fruit_color_dict.get(color, 'I don\'t know')

result = fruit_dict('red')
print(result)
