import unittest
from utils.main import Product
from utils.main import Category

class TestProductAndCategory(unittest.TestCase):
    def test_product_initialization(self):
        product = Product("Ноутбук", "Мощный ноутбук", 999.99, 5)
        self.assertEqual(product.name, "Ноутбук")


    def test_category_initialization(self):
        category = Category("Электроника", "Электронные устройства")
        self.assertEqual(category.name, "Электроника")


if __name__ == "__main__":
    unittest.main()