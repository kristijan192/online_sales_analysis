from product import Product
from product_manager import ProductManager

def main():
    manager = ProductManager()
    
    # Dodavanje:
    product1 = Product("Laptop", 1200.99, 5)
    product2 = Product("Smartphone", 799.50, 10)
    product3 = Product("Headphones", 150.00 ,15)

    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)

    # Prikaz:
    manager.display_products()

    # Ukupna vrednost:
    manager.total_value()

if __name__ == "__main__":
    main()
