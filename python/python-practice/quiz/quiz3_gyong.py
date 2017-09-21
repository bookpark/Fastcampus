class Monster():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, target):
        if type(self) == type(target):
            print('{}가 {}를 공격해 {}의 피해를 입혔다.'.format(self.name, target.name, self.damage))
            target.hp -= self.damage
            if target.hp <= 0:
                print('{}가 죽었다.'.format(target.name))
            else:
                print('{}의 남은 체력: {}'.format(target.name, target.hp))
        else:
            print('몬스터끼리만 싸울 수 있습니다.')

    def __str__(self):
        return '{}: 공격력 {}'.format(self.name, self.damage)


class Item():
    def __init__(self, name):
        self.name = name

pikachu = Monster('피카츄', 300, 130)
ggobugi = Monster('꼬부기', 250, 100)
monsterball = Item('몬스터볼')

pikachu.attack(monsterball)
pikachu.attack(ggobugi)
ggobugi.attack(pikachu)
pikachu.attack(ggobugi)
ggobugi.attack(pikachu)
pikachu.attack(ggobugi)