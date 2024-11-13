class ProductManager:
    discount = 50

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.stock = 0  # Changed to an integer to track stock count

    def apply_discount(self):
        discounted_price = self.price - ProductManager.discount
        print(f"Price after discount = {discounted_price}")
        return discounted_price  # Return the discounted price for use elsewhere

    def update_stock(self, quantity=1):  # Default to adding 1 to stock
        self.stock += quantity  # Increase stock by the quantity passed
        print(f"{self.stock} left in stock")

    def display_product(self):
        discounted_price = self.apply_discount()  # Call the method to get discounted price
        print(f"{self.name} : $ {discounted_price} \n{self.stock} left in stock")

# Create an instance of ProductManager
prod1 = ProductManager("iphone case", 70)

# Call the methods correctly
prod1.apply_discount()
prod1.update_stock(5)  # Update stock with a quantity (e.g., 5 items added)
prod1.display_product()

prod1.update_stock()