from src import Category, Product

if __name__ == "__main__":
    # Пример использования
    category1 = Category("Electronics", "Gadgets and devices")
    product1 = Product("Smartphone", "High-end smartphone", 999.99)

    category1.add_product(product1)

    print(category1)
    print(product1)

