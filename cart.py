class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})

    def show_cart(self):
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            print(
                f"{product.name} - Kolicina: {quantity} - Cena po komadu: {product.price}"
            )

    def total_price(self):
        total = 0
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            total += product.price * quantity
        return total
