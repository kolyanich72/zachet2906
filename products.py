import openpyxl
from random import randint as rndm_n, uniform as rndm_flt


wb = openpyxl.reader.excel.load_workbook(filename="tyres.xlsx")


class IdCounter:
    def __init__(self):
        self._id = None
        self._id = self.get_new_id()

    def current_id(self):
        return self._id

    def get_new_id(self):
        if self._id is not None:
            self._id += 1
        else:
            self._id = 0
        return self._id

    def get_new_minus_id(self):
        if self._id is not None or 0 < self._id:
            self._id -= 1
        else:
            raise ValueError
        return self._id


class Product:
    _counter = IdCounter()

    def __init__(self, name: str, price: float, rating: float):
        self._id = self._counter.get_new_id()
        self.set_new_name = name
        self.set_price = price
        self.set_rating = rating

    def __repr__(self):
        return f"id: {self._id}, name: {self.__name}, price: {self._price}, rating: {self._rating}"

    def __str__(self):
        return f"id: {self._id}  автошины: {self.__name}, цена: {self._price}"

    @property
    def prod_name(self):
        return self.__name

    @prod_name.setter
    def set_new_name(self, value: str):
        self.check_name(value)
        self.__name = value

    @property
    def price_(self):
        return self._price

    @price_.setter
    def set_price(self, value):
        self.check_dig_type(value)
        self._price = value

    @property
    def rating_(self):
        return self._rating

    @rating_.setter
    def set_rating(self, value):
        self.check_dig_type(value)
        self._rating = value

    @staticmethod
    def check_name(value):
        if not isinstance(value, str):
            raise TypeError("имя - это строка")

    @staticmethod
    def check_dig_type(value):
        if not isinstance(value, (int, float)):
            raise TypeError


class ProductGenerator:

    def __init__(self):
        global wb
        wb.active = 0
        self.sheet = wb.active
        self.str_name = 'A'
        self.str_price = 'G'

    def get_product(self):
        """из файла получает в случайном порядке товар и цену,
                    рейтинг также назначется случайным образом """
        x = rndm_n(0, 1048)
        var_name = self.str_name + str(x)
        var_price = self.str_price + str(x)
        goods_name = self.sheet[var_name].value
        goods_price = round(self.sheet[var_price].value, 2)
        goods_rating = rndm_n(0, 11)
        pr = Product(goods_name, goods_price, goods_rating)
 #       print(goods_name, "   ", goods_price, "   ", goods_rating)
        return pr
