""" module with class Flower """


class Flower:
    """ Flower class"""
    def __init__(self, color: str, petals: int, price: int):
        self.color = self.check_color(color)
        self.petals = self.check_number(petals)
        self.price = self.check_number(price)

    def __hash__(self):
        """ return hash(self) """
        return hash((self.color, self.petals, self.price))

    @staticmethod
    def check_number(num: int):
        """ check if num of petals is valid and set it as attribute """
        if isinstance(num, int):
            if num < 0:
                raise ValueError('not correct val of num, it should be a int'
                                 'not less then 0!')
        else:
            raise ValueError('not correct val of num, it should be a int not '
                             'less then 0!')
        return num

    @staticmethod
    def check_color(color: str):
        """ check if color is valid and set it as attribute """
        if not isinstance(color, str):
            raise ValueError('not correct val of color, it should be a str!')
        return color


class Tulip(Flower):
    """ Tulip class"""
    def __init__(self, petals: int, price: int):
        super().__init__(color='pink', price=price, petals=petals)


class Rose(Flower):
    """ Rose class"""
    def __init__(self, petals: int, price: int):
        super().__init__(color='red', price=price, petals=petals)


class Chamomile(Flower):
    """ Chamomile class"""
    def __init__(self, petals: int, price: int):
        super().__init__(color='white', price=price, petals=petals)


class FlowerSet:
    """ FlowerSet class"""
    def __init__(self):
        self.flowers_set = set()
        # self.flowers_type = None

    def __hash__(self):
        """ return hash(self) """
        return hash(frozenset(self.flowers_set))

    def add_flower(self, flower0: Flower):
        """ add flower to FlowerSet """
        if isinstance(flower0, Flower):
            self.flowers_set.add(flower0)
        else:
            raise ValueError('not correct val of flower')


class Bucket:
    """ Bucket class """
    def __init__(self):
        self.set_of_flower_sets = set()
        self.prise = 0

    def add_set(self, flowers_set: FlowerSet):
        """ add FlowerSet to Bucket """
        if isinstance(flowers_set, FlowerSet):
            self.set_of_flower_sets.add(flowers_set)
            for flower0 in flowers_set.flowers_set:
                self.prise += flower0.price
        else:
            raise ValueError('not correct val of flowers_set')

    def total_price(self):
        """ return total prise of Bucket """
        return self.prise
