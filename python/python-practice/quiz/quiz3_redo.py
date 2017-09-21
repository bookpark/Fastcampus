class Monster:
    type_damage_dict = {'electricity': {'water': 2.0, 'fire': 0.8},
                        'water': {'electricity': 0.5, 'fire': 2.0},
                        'fire': {'electricity': 1.2, 'water': 0.5}
                        }

    def __init__(self, name, hp, damage, type):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.type = type

    def attack(self, target):
        self.damage = self.damage * self.type_damage_dict[self.type][target.type]
        if type(self) == type(target):
            print('{}가 {}를 공격하여 {}의 피해를 입혔습니다'.format(self.name, target.name, self.damage))
            target.hp -= self.damage
            if target.hp <= 0:
                print("{}가 {}의 공격으로 인해 사망하였습니다".format(target.name, self.name))
            else:
                print("{}의 피해를 받았습니다 현재 남은 체력: {}".format(self.damage, target.hp))
        else:
            print("몬스터끼리만 싸울 수 있습니다")


class Item:
    def __init__(self, name):
        self.name = name


pikachu = Monster('Pikachu', 1200, 250, 'electricity')
squirtle = Monster('Squirtle', 1400, 250, 'water')
charmander = Monster('Charmander', 1100, 250, 'fire')

squirtle.attack(pikachu)
squirtle.attack(pikachu)
squirtle.attack(pikachu)
squirtle.attack(pikachu)
pikachu.attack(squirtle)
pikachu.attack(squirtle)


