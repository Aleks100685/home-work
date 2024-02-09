class Product:
    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.price = price  # цена с копейками, например, 19.99
        self.quantity_in_stock = quantity_in_stock  # количество в штуках


class Category:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []  # список товаров в данной категории

    def add_product(self, product):
        """Добавляет товар в категорию."""
        self.products.append(product)

    def display_products(self):
        """Выводит информацию о товарах в категории."""
        print(f"Товары в категории {self.name}:")
        for product in self.products:
            print(f"{product.name} - {product.price} руб., {product.quantity_in_stock} шт.")


# Пример использования классов:

# Создаем товары
product1 = Product("Ноутбук", "Мощный ноутбук", 799.99, 10)
product2 = Product("Смартфон", "Современный смартфон", 399.99, 20)

# Создаем категории
electronics_category = Category("Электроника", "Бытовая электроника")
gadgets_category = Category("Гаджеты", "Различные гаджеты")

# Добавляем товары в соответствующие категории
electronics_category.add_product(product1)
gadgets_category.add_product(product2)

# Выводим информацию о товарах в каждой категории
electronics_category.display_products()
gadgets_category.display_products()