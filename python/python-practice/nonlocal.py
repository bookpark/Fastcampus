champion = 'Lux'

def local1():
    champion = 'Ahri'

    def local2():
        nonlocal champion
        champion = 'Ezreal'
        print('local2:', champion)

    print('before local1:', champion)
    local2()
    print('after local1:', champion)
    

print('global:', champion)
local1()
print('global:', champion)

