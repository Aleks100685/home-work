import unittest
from utils.src import Product
from utils.src import Category

class TestCategoryAndProduct(unittest.TestCase):

    def setUp(self):
        # Этот метод будет вызван перед каждым тестом
        Category.total_categories = 0
        Category.total_unique_products = 0

    def test_category_initialization(self):
        # Проверка инициализации категории
        category = Category("Electronics", "Gadgets and devices")
        self.assertEqual(Category.total_categories, 1)

    def test_product_initialization(self):
        # Проверка инициализации продукта
        product = Product("Smartphone", "High-end smartphone", 999.99)
        self.assertEqual(Category.total_unique_products, 0)

    def test_add_product_to_category(self):
        # Проверка добавления продукта в категорию
        category = Category("Electronics", "Gadgets and devices")
        product = Product("Smartphone", "High-end smartphone", 999.99)
        category.add_product(product)
        self.assertEqual(len(category.products), 1)
        self.assertEqual(Category.total_unique_products, 1)

if __name__ == '__main__':
    unittest.main()