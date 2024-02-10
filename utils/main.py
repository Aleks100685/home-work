from src import Category, Product

if __name__ == "__main__":
    # Пример использования
    category1 = Category("Electronics", "Electronic gadgets")
    product1 = Product("Laptop", "High-performance laptop", 1200.50, 10)
    category1.add_product(product1)

    category2 = Category("Books", "Literary masterpieces")
    product2 = Product("Book1", "Bestseller", 20.00, 50)
    category2.add_product(product2)

    print("Total categories:", Category.total_categories)
    print("Total unique products:", len(Category.total_unique_products))

