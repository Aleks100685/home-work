class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
        Category.total_categories += 1

    def add_product(self, product):
        self.products.append(product)
        Category.total_unique_products += 1

    def __str__(self):
        return f"Category: {self.name}, Description: {self.description}, Products: {len(self.products)}"

class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, Description: {self.description}, Price: {self.price}"




