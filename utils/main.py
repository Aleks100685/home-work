from src import Category, Product

if __name__ == "__main__":
    # Пример использования
    product1 = Product("product1", "Description 1", 10)
    product2 = Product("product2", "Description 2", 15)

    category1 = Category("Category 1", "Category Description 1")
    category1.add_product(product1)
    category1.add_product(product2)

    print(Category.total_categories)
    print(Product.total_unique_products)

