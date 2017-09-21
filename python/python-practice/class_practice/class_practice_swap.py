class BaskinRobbins:
    ''' Represent Baskin-Robbins'''
    def __init__(self, location):
        ''' Construct location of a Baskin-Robbins shop'''
        self.__location = location
        self.__menu = []
        #self.profit = 0

    def make_menu(self, flavor, price):
        ''' Take two args flavor and the price of the new menu to add a menu'''
        self.__menu.append({'flavor' :flavor, 'price' : price})

    def show_menu(self):
        ''' Show menu'''
        if len(self.__menu) == 0:
            print('preparing for the opening')
        else:
            for menu in __self.menu:
                print("flavor: {} price: {}won".format(__menu['flavor'], __menu['price']))

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, new_location):
        self.__location = new_location
        print('Set new location ({}'.format(self.__location))
