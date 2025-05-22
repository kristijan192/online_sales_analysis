from product import Product

class ProductManager:
      def __init__(self):
            self.products = []
      
      def add_product(self, product):
            self.products.append(product)
            print(f"Product '{product.name}' added.")

      def display_products(self):
            if not self.products:
                  print("No products available")
            else:
                  for product in self.products:
                      product.display_info()
      
      def total_value(self):
            total = sum(product.price * product.quantity for product in self.products)
            print(f"Total value of all products: ${total}")
            return total
      