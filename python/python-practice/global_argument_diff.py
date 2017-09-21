global_level = 100

def level_add(value):
    value += 30

level_add(global_level)
print(global_level)

def level_add():
    global global_level
    global_level += 30
    print(global_level)

level_add()

global_list = [100]

def level_add(l):
    l[0] += 30

print(global_list)
level_add(global_list)
print(global_list)
