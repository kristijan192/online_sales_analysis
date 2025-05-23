from product import Product
from product_manager import ProductManager
from cart import Cart


def main():
    manager = ProductManager()

    product1 = Product("Laptop", 1200.99, 5)
    product2 = Product("Smartphone", 799.50, 10)
    product3 = Product("Headphones", 150.00, 15)

    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)

    manager.display_products()

    print(f"Ukupna vrednost svih proizvoda: {manager.total_value()}")

    cart = Cart()
    cart.add_product(product1, 1)
    cart.add_product(product2, 2)

    print("\nSadržaj korpe:")
    cart.show_cart()

    print(f"Ukupna cena u korpi: {cart.total_price()}")


if __name__ == "__main__":
    main()
