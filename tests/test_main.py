import unittest
from utils.src import Product
from utils.src import Category

class TestCategoryAndProduct(unittest.TestCase):
    def setUp(self):
        Category.total_categories = 0
        Product.total_unique_products = 0

    def test_category_initialization(self):
        category1 = Category("Electronics", "Electronic devices")
        self.assertEqual(Category.total_categories, 1)

    def test_product_initialization(self):
        product1 = Product("Laptop", "High-performance laptop", 1200)
        self.assertEqual(Product.total_unique_products, 1)

    def test_total_categories_and_unique_products(self):
        category1 = Category("Electronics", "Electronic devices")
        product1 = Product("Laptop", "High-performance laptop", 1200)
        self.assertEqual(Category.total_categories, 1)
        self.assertEqual(Product.total_unique_products, 1)

if __name__ == "__main__":
    unittest.main()