import re, string
# source = 'Lux, the Lady of Luminosity'
# m = re.match('Lux', source)
# if m:
#     print(m.group())
#
# m = re.split(' of ', source)
# print(m)
# m = re.findall('y.?.?', source)
# print(m)
# m = re.sub('L', 'B', source)
# print(m)
#
# printable = string.printable
# # re.findall('\w', printable)
# re.findall('\d', printable)
#
# print(printable)

story = '''Born to the prestigious Crownguards, the paragon family of Demacian service, Luxanna was destined for greatness. She grew up as the family's only daughter, and she immediately took to the advanced education and lavish parties required of families as high profile as the Crownguards. As Lux matured, it became clear that she was extraordinarily gifted. She could play tricks that made people believe they had seen things that did not actually exist. She could also hide in plain sight. Somehow, she was able to reverse engineer arcane magical spells after seeing them cast only once. She was hailed as a prodigy, drawing the affections of the Demacian government, military, and citizens alike.

As one of the youngest women to be tested by the College of Magic, she was discovered to possess a unique command over the powers of light. The young Lux viewed this as a great gift, something for her to embrace and use in the name of good. Realizing her unique skills, the Demacian military recruited and trained her in covert operations. She quickly became renowned for her daring achievements; the most dangerous of which found her deep in the chambers of the Noxian High Command. She extracted valuable inside information about the Noxus-Ionian conflict, earning her great favor with Demacians and Ionians alike. However, reconnaissance and surveillance was not for her. A light of her people, Lux's true calling was the League of Legends, where she could follow in her brother's footsteps and unleash her gifts as an inspiration for all of Demacia.'''


pr1 = re.findall(r'\ba\w{3}\b', story)
print(pr1)

pr2 = re.findall(r'\b\w*r\b', story)
print(pr2)

pr3 = re.findall(r'\w*[abcde]{3}\w*', story)
print(pr3)

pr4 = re.findall(r'(?P<before>\w+)\s*,\s*(?P<after>\w+)', story)
p = re.compile(r'(?P<before>\w+)\s*,\s*(?P<after>\w+)')

# def upper(m):
#     return m.group().upper()
# pr4_1 = re.sub(p, upper, story)

def upper_first(m):
    return '{}, [{}]'.format(m.group(1).upper(), m.group(2))
pr4 = re.sub(p, upper_first, story)
print(pr4)