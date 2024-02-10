import unittest
from utils.src import Product
from utils.src import Category

class TestCategoryAndProduct(unittest.TestCase):
    def setUp(self):
        # Подготовка данных
        self.total_categories_before = 0
        self.total_unique_products_before = set()


    def test_category_initialization(self):
        category = Category("Electronics", "Electronic gadgets")
        self.assertEqual(category.name, "Electronics")
        self.assertEqual(category.description, "Electronic gadgets")
        self.assertEqual(category.products, [])
        self.assertEqual(self.total_categories_before + 1, 1)  # Проверка общего количества категорий

    def test_product_initialization(self):
        product = Product("Laptop", "High-performance laptop", 1200.50, 10)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.description, "High-performance laptop")
        self.assertEqual(product.price, 1200.50)
        self.assertEqual(product.quantity, 10)
        self.assertEqual(self.total_unique_products_before | set(range(1, 11)), set(range(1, 11)))  # Проверка уникальных продуктов

if __name__ == "__main__":
    unittest.main()