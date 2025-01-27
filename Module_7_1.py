from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = float(weight)
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop(Product):
    __file_name = 'product.txt'
    def __init__(self, name):
        super().__init__(self, name)



    def add(self, *products):
        for prod in products:
            if prod in products:
                return f'Продукт {self.name} уже есть в магазине'
            else:
                file = open(self.__file_name, 'a')
                pprint(file.write(prod))
                file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        pprint(file.read())
        file.close()
        return f'{self.__file_name}'




s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')

p2 = Product('Spaghetti', 3.4, 'Groceries')

p3 = Product('Potato', 5.5, 'Vegetables')


print(p2) # __str__



s1.add(p1, p2, p3)



print(s1.get_products())

















