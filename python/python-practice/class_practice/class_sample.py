class Shop:
    description = 'Python Shop class'

    def __init__(self, name, shop_type, address):
        self.name = name
        self._shop_type = shop_type
        self.address = address

    def show_info(self):
        print(f'상점정보: ({self.name})')
        print(f'    유형: {self._shop_type}')
        print(f'    주소: {self.address}')

    @classmethod
    def make_dummy(cls):
        return cls('untitled', 'undefined', 'unknown')

    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, new_shop_type):
        if new_shop_type not in['Fastfood', 'PC']:
            print('Cannot change the type')
        else:
            self._shop_type = new_shop_type

    def show_object_log(self, obj):
        print(obj.log)

class Restaurant(Shop):
    def __init__(self, name, shop_type, address, rating=5.0):
        super().__init__(name, shop_type, address)
        self.rating = rating

    def show_info(self):
        print(f'식당: ({self.name})')
        print(f'유형: ({self.shop_type})')
        print(f'주소: ({self.address})')
        print(f'평점: ({self.rating})')
