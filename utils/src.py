class Category:
    total_categories = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
        Category.total_categories += 1

    def add_product(self, product):
        self.products.append(product)

class Product:
    total_unique_products = 0

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        Product.total_unique_products += 1