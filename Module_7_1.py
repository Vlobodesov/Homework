from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop(Product):
    __file_name = 'product.txt'
    def __init__(self):
    def get_products(self):
        open(self.__file_name, 'r')
        pprint(self.__file_name.read())
        self.__file_name.close()
        return f'{self.__file_name}'

    def add(self,*products):
        if self.products not in self.__file_name:















